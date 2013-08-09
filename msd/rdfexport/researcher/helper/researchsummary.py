#!/usr/bin/env python
# 
from msd.rdfexport import utils


def createTag(rdf, researchernode, researcherobj):
    
    """
    <dc:description rdf:parseType="Literal">
      Paul Broca: Neuroanatomy, neuropathology, and the localisation of 
      cortical functions, in particular the neuropsychology of the aphasias
    </dc:description>
    
    <res:researchSummary rdf:parseType="Literal">
      My current research focuses upon the localisation of higher cortical 
      functions, in particular speech and language, in humans. Through the 
      consideration of lesion patients ...
    </res:researchSummary>
    
    <res:biography>
      I was a brilliant student. I entered medical school in Paris when I was 
      only 17 years old ...
    </res:biography>
    
    msd.researcher - the main aim here is to pass the HTML markup intact to the rdf file
    also any internal links need to be turned into absolute links. This is a serious hack
    at the moment using BeautifulSoup - better ideas would be very welcome. Especially as this
    will be a common problem with any syndicated content.

    """

#description
        
    description = rdf.createElement('dc:description')
    description.setAttribute('rdf:parseType','Literal')
    description.appendChild(rdf.createTextNode(researcherobj.Description()))
    researchernode.appendChild(description)
    
    res_summary = researcherobj.getSummary()
    res_biography = researcherobj.getBiography()
    absolute_url = researcherobj.absolute_url()

    

    if res_summary:
        res_summary_fixed = utils.fix_urls(res_summary, absolute_url)
        resSummary = rdf.createElement('res:researchSummary')
        resSummary.setAttribute('rdf:parseType','Literal')
        resSummary.appendChild(rdf.createCDATASection(res_summary_fixed))
       # we don't want to create CDATA so parse the string
       # wrap it in a div first so that it doesn't throw an error
       # at least in ElementTree it would
        
        #innerhtml = u'<div>' + res_summary + u'</div>'
        #innerhtml = u'<?xml version="1.0" encoding="UTF-8"?><div><p>Hello</p></div>'
        #innerelement = parseString(innerhtml)
        #clonedelement = innerelement.documentElement.firstChild.cloneNode(1)
        #resSummary.appendChild(clonedelement)
        researchernode.appendChild(resSummary)
        
    if res_biography:
        res_biography_fixed = utils.fix_urls(res_biography, absolute_url)
        resBiog = rdf.createElement('res:biography')
        resBiog.setAttribute('rdf:parseType','Literal')
        resBiog.appendChild(rdf.createCDATASection(res_biography_fixed))
        researchernode.appendChild(resBiog)
    


