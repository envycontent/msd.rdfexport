#!/usr/bin/env python

from msd.rdfexport.researcher.helper import utilities
        
def createTag(rdf, researchernode, researcherobj):
    
    """  
    <dc:subject>aphasia</dc:subject>    
    <dc:subject>prefrontalcortex</dc:subject>    
    <dc:subject>microscopy</dc:subject> 
    
    msd.researcher: this is where it gets really complicated ugh
    
    there are two ways of providing keywords. The first here, is simple dc:subject
    this should be populated from getKeywords1 | getKeywords2 | getKeywords3 | getKeywords4
    | getKeywords5
    
    the second is in the themes.py function, I've documented more there.
    
       
    """
    res_keywords = []
    res_keywords.extend(researcherobj.getThemes2())
    res_keywords.extend(researcherobj.getThemes3())
    res_keywords.extend(researcherobj.getThemes4())
    res_keywords.extend(researcherobj.getThemes5())

           
    for keyword in res_keywords:
        entry = rdf.createElement('dc:subject')
        researchernode.appendChild(entry)
        entry.appendChild(rdf.createTextNode(keyword))


