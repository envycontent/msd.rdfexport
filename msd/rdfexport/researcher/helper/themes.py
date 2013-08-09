#!/usr/bin/env python

## Method for adding res:worksOn connectors to a <res:Researcher> node ##
def createTag(rdf, researchernode, researcherobj):
    """
    <res:worksOn rdf:resource="http://www.medsci.ox.ac.uk/research/themes/neuro"/>
    <res:worksOn rdf:resource="http://www.medsci.ox.ac.uk/research/themes/infection"/>
    
    OK. Here we have to add 'Themes' which are categorizations like keywords, but there is
    more information provided about them elsewhere.
    
    The source of these will be:
    
    1. the getKeywords field that has the MSD Research Theme keyword vocabulary
    (NB it won't matter if this field has also been used to populate dc:subject - see
    keywords.py - a little duplication will be fine)
    
    2. Any relations of the type: researchers_in_theme
    
    The code below has been divided up into themes and subthemes - which isn't necessary
    
    effectively: 
    
    <res:worksOn rdf:resource = either the URL for the MSD theme, which it should be possible
    to look up from the list of themes in utilities OR the URL for the theme content item the researcher
    is related to.
    
    The theme url utilities below aren't relevant at all.
    
    
    TO DO: actually check whether this is relevant.
    
    """
    #msd.researcher - this is not necessarily getKeywords1, it is whichever of the
    #keywords fields has the MSD Research Themes keyword vocabulary assigned to it
    
    
    res_themes = researcherobj.getThemes1()  
    if res_themes:   
        for theme in res_themes:
            themeurl = createThemeURL(theme)           
            entry = rdf.createElement('res:worksOn')
            entry.setAttribute('rdf:resource',themeurl)
            researchernode.appendChild(entry)   
               
           
            
            
            
### Methods for adding big <res:ResearchTheme> nodes to the document ###           
def addThemesToDocument(rdf, themesList):
    """
    <res:ResearchTheme rdf:about="http://www.medsci.ox.ac.uk/research/themes/infection">
      <dc:title>Infection and Immunology</dc:title>
    </res:ResearchTheme>
    """
    for theme in themesList:       
        themeurl = createThemeURL(theme)
        rt = rdf.createElement('res:ResearchTheme')
        rt.setAttribute('rdf:about',themeurl)        
        title = rdf.createElement('dc:title')       
        title.appendChild(rdf.createTextNode(theme))  
        rt.appendChild(title)
        rdf.documentElement.appendChild(rt)  
 
  
def addSubThemesToDocument(rdf, themesList):
    """
    <res:ResearchTheme rdf:about="http://www.neuroscience.ox.ac.uk/themes/scbn">
      <dc:title>Systems, Cognitive and Behavioural Neuroscience</dc:title>
      <dcterms:partOf rdf:resource="http://www.medsci.ox.ac.uk/research/themes/neuro" />
    </res:ResearchTheme>
    """
    for theme in themesList:       
        themeurl = createSubThemeURL(theme)
        rt = rdf.createElement('res:ResearchTheme')
        rt.setAttribute('rdf:about',themeurl)        
        title = rdf.createElement('dc:title')       
        title.appendChild(rdf.createTextNode(theme))  
        rt.appendChild(title)
        rdf.documentElement.appendChild(rt)  
        ## TODO : isPartOf.  Need themes hierarchy data.
        ## HACK for now, all part of neuroscience
        parent = rdf.createElement('dcterms:isPartOf')
        parent.setAttribute('rdf:resource','http://www.medsci.ox.ac.uk/research/themes/neuro')
        rt.appendChild(parent)







###  Theme URL utilities ####

def createThemeURL(name):
    return "http://www.medsci.ox.ac.uk/research/themes/" + cleanThemeName(name)

def createSubThemeURL(name):
    ## TODO : isPartOf.  Need themes hierarchy data.
    ## HACK for now, all part of neuroscience
    return "http://www.neuroscience.ox.ac.uk/subthemes/" + cleanThemeName(name)    
    
def cleanThemeName(name):
    return name.lower().replace(' ','-').replace(',','')
    