#!/usr/bin/env python

def createTag(rdf, researchernode, researcherobj):
    """
    <foaf:holdsAccount>
      <foaf:OnlineAccount>
        <foaf:accountServiceHomepage rdf:resource="http://webauth.ox.ac.uk"/>
        <foaf:accountName>pb123</foaf:accountName>
      </foaf:OnlineAccount>
    </foaf:holdsAccount>
    """
    
    res_accUsername = researcherobj.getOxford_username()
    
    
    if res_accUsername:
        
        holdsac = rdf.createElement('foaf:holdsAccount')
        researchernode.appendChild(holdsac)
        
        acc = rdf.createElement('foaf:OnlineAccount')
        holdsac.appendChild(acc)
        
        acchp = rdf.createElement('foaf:accountServiceHomepage')
        acchp.setAttribute('rdf:resource', 'http://webauth.ox.ac.uk')
        acc.appendChild(acchp)
        
        accname = rdf.createElement('foaf:accountName')
        accname.appendChild(rdf.createTextNode(res_accUsername))
        acc.appendChild(accname)
        
        
        #acctags = [{'level':1,'tag':'foaf:holdsAccount'},
        #          {'level':2, 'tag':'foaf:OnlineAccount'},
        #          {'level':3, 'tag':'foaf:accountServiceHomepage', 'att':['rdf:resource','http://webauth.ox.ac.uk']},
        #          {'level':3, 'tag':'foaf:accountName','text':res_accUsername},]
        #              
        #self.processTags(rdf,acctags,researcher)        