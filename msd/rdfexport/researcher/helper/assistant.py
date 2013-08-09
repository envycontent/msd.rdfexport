#!/usr/bin/env python
# 
from AccessControl import Unauthorized

def createTag(rdf, researchernode, researcherobj):
    """
    <con:assistant>
      <foaf:Person>
        <foaf:name>Assistant Smith</foaf:name>
        <con:phone>01865 123456</con:phone>
        <con:fax>01865 234567</con:fax>
        <foaf:mbox>assistant.smith@all-souls.ox.ac.uk</foaf:mbox>
      </foaf:Person>
    </con:assistant>
    
    msd.researcher: no changes in the accessors - only difference is that we don't need
    AccessControl because we aren't using Privacy Field
    
    Same question applies about the email address as elsewhere
    
    """
    
    #check to see if PA exists
    try:
        res_paphone = researcherobj.getPa_phone()
    except Unauthorized:
        res_paphone = None
    try:
        res_pafax = researcherobj.getPa_fax()
    except Unauthorized:
        res_pafax = None
    try:
        res_paemail = researcherobj.getPa_email()
    except Unauthorized:
        res_paemail = None
        
    res_paname = researcherobj.getPa_name()
    
    if res_paname or res_paemail or res_paphone:
        has_pa = True
    else:
        has_pa = False
            
            
    if has_pa:
        ass = rdf.createElement('con:assistant')
        
        assperson = rdf.createElement('foaf:Person')
        
        assname = rdf.createElement('foaf:name')
        assname.appendChild(rdf.createTextNode(res_paname))
        assperson.appendChild(assname)
        
        if res_paphone:
            assphone = rdf.createElement('con:phone')
            assphone.appendChild(rdf.createTextNode(res_paphone))
            assperson.appendChild(assphone)
        
        
        if res_pafax:
            assfax = rdf.createElement('con:fax')
            assfax.appendChild(rdf.createTextNode(res_pafax))
            assperson.appendChild(assfax)
        
        if res_paemail:
            assemail = rdf.createElement('foaf:mbox')
            assemail.appendChild(rdf.createTextNode(res_paemail))
            assperson.appendChild(assemail)

        
        ass.appendChild(assperson)
        researchernode.appendChild(ass)    