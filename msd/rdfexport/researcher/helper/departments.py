#!/usr/bin/env python

from msd.rdfexport.researcher.helper import map_departmenturis, webpresence

def createTag(rdf, researchernode, researcherobj):
    
    """
    <foaf:member rdf:resource="http://www.clneuro.ox.ac.uk/"/>
    <foaf:member rdf:resource="http://www.psy.ox.ac.uk/"/>
    <foaf:member rdf:resource="http://www.path.ox.ac.uk/"/>
    
    msd.researcher - as for college the map_departmenturis could be provided by
    msd.researchbase (what happens if additional departments have been added in the
    researchbase setup tool?)
    
    
    
    """
# get the department or unit of the current website. This is a bit of a problem because
# we won't necessarily have the title of that department - but it might make sense to make
# a field specifically for that in msd.researchbase
    
    absolute_url = researcherobj.absolute_url()
    split_url = absolute_url.split('/')
    dept_url = split_url[2]
    pos_dept_url = 'http://' + dept_url
#    pos_dept_url = 'http://www.primarycare.ox.ac.uk'
    
    if map_departmenturis.lookupDept(pos_dept_url):
        
        memOf = rdf.createElement('foaf:member')
        memOf.setAttribute('rdf:resource', pos_dept_url)
        researchernode.appendChild(memOf)
        
    
    res_depts = researcherobj.getUnits()
    
    if res_depts:
    
        for dept in res_depts:                    
            
            depturl = map_departmenturis.lookupURL(dept)
            memOf = rdf.createElement('foaf:member')
            memOf.setAttribute('rdf:resource', depturl)
            researchernode.appendChild(memOf)
            
            
          
def addDepartmentsToDocument(rdf, deptsList):        

    """
    <foaf:Organization rdf:about="http://www.psy.ox.ac.uk/">
        <dc:title>Department of Experimental Psychology</dc:title>       
        <dcterms:isPartOf rdf:resource="http://www.medsci.ox.ac.uk/"/>
        
        ---- not available yet ------
        <con:address>South Parks Road, Oxford, OX1 3UD</con:address>
        <con:phone>+44 (0)1865 271444</con:phone>
        <foaf:based_near>
          <geo:Point>
            <geo:lat>51.83333</geo:lat>
            <geo:long>-1.25</geo:long>
          </geo:Point>
        </foaf:based_near>
        

        <foaf:homepage>....
        --- see webpresence.py -----
     

      </foaf:Organization>
    """ 
     
        
    for dept in deptsList:
        
        
        depturl = map_departmenturis.lookupURL(dept)

        deptentry = rdf.createElement('foaf:Organization')
        deptentry.setAttribute('rdf:about',depturl)
        depttitle = rdf.createElement('dc:title')
        depttitle.appendChild(rdf.createTextNode(dept))      
        deptpartof = rdf.createElement('dcterms:isPartOf')
        deptpartof.setAttribute('rdf:resource',"http://www.medsci.ox.ac.uk")        
        deptentry.appendChild(depttitle)
        deptentry.appendChild(deptpartof)
        
        webpresence.addWebPresenceElement(rdf, deptentry, dept)
        
        rdf.documentElement.appendChild(deptentry)          
            
    