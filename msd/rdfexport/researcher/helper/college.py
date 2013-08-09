#!/usr/bin/env python

import map_collegeuris

def createTag(rdf, researchernode, researcherobj):
    
    """
    <foaf:member>
      <aiiso:College rdf:about="http://www.all-souls.ox.ac.uk/">
        <dc:title>All Souls College, Oxford</dc:title>
      </aiiso:College>
    </foaf:member>
    
    Notes for msd.researcher. The look up for colleges is currently done
    with the map_collegeuris.py - but could be switched to the utility
    available in msd.researchbase
    
    TO DO - find out why college isn't mapped over to ORA
    
    """
    
    res_college = researcherobj.getCollege()
    
    if res_college and res_college <> "none":
        
        memberProp = rdf.createElement('foaf:member')
        researchernode.appendChild(memberProp)
        
        collegeOb = rdf.createElement('aiiso:College')        
        memberProp.appendChild(collegeOb)
        
        collurl = map_collegeuris.lookupCollege(res_college)                
        if collurl:    
            collegeOb.setAttribute('rdf:about', collurl)
            
        title = rdf.createElement('dc:title')
        title.appendChild(rdf.createTextNode(res_college))
        collegeOb.appendChild(title)
        
        
        
        
#        if res_college:
#            
#            collurl = self.lookupCollege(res_college)
#            collegetags = [{'level':1, 'tag':'res:college'},
#                           {'level':2, 'tag':'res:College','att':['rdf:about',collurl]},
#                           {'level':3, 'tag':'dc:title','text':res_college},]                            
#                
#            self.processTags(rdf,collegetags,researcher)       