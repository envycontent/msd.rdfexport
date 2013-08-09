#!/usr/bin/env python

def createTag(rdf, researchernode, researcherobj):
    """
    <res:collaboratesWith>
      <res:Researcher>
        <foaf:homepage rdf:resource="http://www.britannica.com/eb/article-9076566/Carl-Wernicke"/>
        <foaf:name>Karl Wernicke</foaf:name>
        <dc_identifier>md5 hash goes here</dc_identifier>
      </res:Researcher>
    </res:collaboratesWith>
    
    
    In msd.researcher there is one single datagrid field - getCollaborators - column names are the same
    We are also storing the email address, which could be added to the foaf profile.
    However, I don't want to start harvesting the email address until I've had a discussion with 
    ORA about this
    
    Just spoken to Anusha, we will use dc_identifier and pass the email address in the RDF as an MD5 hash
    this gives us a certain level of security - not perfect, but Anusha can also store as a hash and use
    the email as an identifier
    
    """
    

    #current collaborators    
    addCollaborators(rdf, researchernode, researcherobj.getGroupMembers())
    #past collaborators
    addCollaborators(rdf, researchernode, researcherobj.getPastGroupMembers())
    #other collaborators
    addCollaborators(rdf, researchernode, researcherobj.getAllCollaborators())


        
def addCollaborators(rdf, researchernode, groupMembers):        
        
        for mem in groupMembers:
            
            memurl = mem['url']
            memfullname = mem['fullName']
            
            collabwith = rdf.createElement('res:collaboratesWith')
            researchernode.appendChild(collabwith)
            
            pers = rdf.createElement('res:Researcher')
            collabwith.appendChild(pers)
            
            if mem['url']:
            
                hp = rdf.createElement('foaf:homepage')
                hp.setAttribute('rdf:resource',memurl)
                pers.appendChild(hp)    
    
            name = rdf.createElement('foaf:name')
            name.appendChild(rdf.createTextNode(memfullname))
            pers.appendChild(name)
            
    
    #if res_groupMembers:
    #    
    #    for mem in res_groupMembers:
    #        memurl = mem['url']
    #        memfullname = mem['fullName']
    #        
    #        memtags = [{'level':1,'tag':'res:collaboratesWith'},
    #                    {'level':2, 'tag':'res:Researcher'},
    #                    {'level':3, 'tag':'foaf:homepage', 'att':['rdf:resource',memurl]},
    #                    {'level':3, 'tag':'foaf:name','text':memfullname},]
    #        
    #        self.processTags(rdf,memtags,researcher)
    #    
    #if res_pastMembers:
    #
    #    for mem in res_pastMembers:
    #        memurl = mem['url']
    #        memfullname = mem['fullName']
    #        
    #        memtags = [{'level':1,'tag':'res:collaboratesWith'},
    #                    {'level':2, 'tag':'res:Researcher'},
    #                    {'level':3, 'tag':'foaf:homepage', 'att':['rdf:resource',memurl]},
    #                    {'level':3, 'tag':'foaf:name','text':memfullname},]
    #        
    #        self.processTags(rdf,memtags,researcher)
    #    
    #if res_others:
    #
    #    for mem in res_others:
    #        memurl = mem['url']
    #        memfullname = mem['fullName']
    #        
    #        memtags = [{'level':1,'tag':'res:collaboratesWith'},
    #                    {'level':2, 'tag':'res:Researcher'},
    #                    {'level':3, 'tag':'foaf:homepage', 'att':['rdf:resource',memurl]},
    #                    {'level':3, 'tag':'foaf:name','text':memfullname},]
    #        
    #        self.processTags(rdf,memtags,researcher)
    