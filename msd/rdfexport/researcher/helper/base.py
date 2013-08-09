#!/usr/bin/env python
from AccessControl import Unauthorized

        
def createTag(rdf, researchernode, researcherobj):
    
    """    
    <foaf:title>Dr</foaf:title>
    <foaf:name>Paul Broca</foaf:name>
    <foaf:firstName>Paul</foaf:firstName>
    <foaf:surname>Broca</foaf:surname>
    <foaf:mbox>paul.broca@all-souls.ox.ac.uk</foaf:mbox>
    <foaf:mbox_sha1sum>c2f3f3a091374803cfcfe6f3fa7960130d4a0a7c</foaf:mbox_sha1sum>
    <foaf:homepage rdf:resource="http://www.neuroscience.ox.ac.uk/directory/paul-broca/"/>
    <foaf:homepage rdf:resource="http://www.ox.ac.uk/surgicalpathology/paulbroca.html"/>
   
    <res:postNominals>MD</res:postNominals>
    
    <con:address>All Souls College, Radcliffe Square, Oxford, OX1 4AL</con:address>
    <con:phone>01865 123456</con:phone>
    <con:fax>01865 234567</con:fax>
    
    <res:statusString>Fellow of All Souls College</res:statusString>
    <res:statusString>Professor of Surgical Pathology</res:statusString>
    
    Comments:
    
    I'm not sure if we've ever implemented the mbox_sha1sum - although I would like to do it
    it isn't urgent
    
    the exception for unauthorized is appropriate to RDSLocal (where we used PrivacyField)
    but not necessary for msd.researcher
    
    """
      
    #title 
    #msd.researcher - getHonorific   
    strTitle = rdf.createElement('foaf:title')
    strTitle.appendChild(rdf.createTextNode(researcherobj.getStrTitle()))
    researchernode.appendChild(strTitle)
    
    #name
    name = rdf.createElement('foaf:name')
    name.appendChild(rdf.createTextNode(researcherobj.title_or_id()))
    researchernode.appendChild(name)
    
    #firstname    
    fname = rdf.createElement('foaf:firstName')
    fname.appendChild(rdf.createTextNode(researcherobj.getFirst_name()))
    researchernode.appendChild(fname)
    
    #surname
    sname = rdf.createElement('foaf:surname')
    sname.appendChild(rdf.createTextNode(researcherobj.getLast_name()))
    researchernode.appendChild(sname)
    
    #email
    try:
        res_email = researcherobj.getEmail()
    except Unauthorized:
        res_email = None 
    if res_email:
            mbox = rdf.createElement('foaf:mbox')
            mbox.appendChild(rdf.createTextNode(res_email))
            researchernode.appendChild(mbox)
    
    #homepage 1  
    homepage = rdf.createElement('foaf:homepage')
    homepage.setAttribute('rdf:resource', researcherobj.absolute_url())
    researchernode.appendChild(homepage)

    #homepage - 2
    res_personalurl = researcherobj.getUrl()        
    if res_personalurl:
        homepage1 = rdf.createElement('foaf:homepage')
        homepage1.setAttribute('rdf:resource', res_personalurl)
        researchernode.appendChild(homepage1)
        

    
    
    #letters after name
    res_letters = researcherobj.getLetters_after_name()
    if res_letters:
        lan = rdf.createElement('res:postNominals')
        lan.appendChild(rdf.createTextNode(res_letters))
        researchernode.appendChild(lan)
      

    #address
    res_address = researcherobj.getContact_address()
    if res_address:
        address = rdf.createElement('con:address')
        address.appendChild(rdf.createTextNode(res_address))
        researchernode.appendChild(address)    

    #phone
    try:
        res_phone = researcherobj.getPhone()
    except Unauthorized:
        res_phone = None       
    if res_phone:
        tel = rdf.createElement('con:phone')
        tel.appendChild(rdf.createTextNode(res_phone))
        researchernode.appendChild(tel)
        
    #alt phone
    #msd.researcher - not available
    try:
        res_alternate_phone = researcherobj.getAlternate_phone()
    except Unauthorized:
        res_alternate_phone = None
    if res_alternate_phone:
        tel = rdf.createElement('con:phone')
        tel.appendChild(rdf.createTextNode(res_alternate_phone))
        researchernode.appendChild(tel)
        

    #fax
    try:
        res_fax = researcherobj.getFax()
    except Unauthorized:
        res_fax = None            
    if res_fax:
        fax = rdf.createElement('con:fax')
        fax.appendChild(rdf.createTextNode(res_fax))
        researchernode.appendChild(fax)

    #job titles
    # these two have been merged into one field in msd.researcher - getJob_titles
    res_univjt = researcherobj.getUniv_job_title()   
    if res_univjt:
        univJT = rdf.createElement('res:statusString')
        univJT.appendChild(rdf.createTextNode(res_univjt))
        researchernode.appendChild(univJT)
        
    res_deptjt = researcherobj.getJob_title()
    if res_deptjt:
        deptJT = rdf.createElement('res:statusString')
        deptJT.appendChild(rdf.createTextNode(res_deptjt))
        researchernode.appendChild(deptJT) 
      
        

        