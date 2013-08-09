#!/usr/bin/env python
# 
# 

from Products.CMFCore.utils import getToolByName

def createTag(rdf, researchernode, researcherobj):
    """
    <foaf:publications>    
      <rdf:Seq> 
        <rdf:li>
            <bibo:Document>
                <bibo:pmid>11111111</bibo:pmid>
            </bibo:Document>

        </rdf:li>
        <rdf:li>
            <bibo:Document>
                <bibo:pmid>22222222</bibo:pmid>
            </bibo:Document>
        </rdf:li>        
      </rdf:Seq>
    </foaf:publications>
    
    msd.researcher, this won't be relevant as we'll be getting publications
    from elsewhere, however for Plone 3 sites using CMFBibAT this will still be useful
    
    
    """
   
    #   TODO: Get list of publications from somewhere 
    #
    #   FAKE LIST | 
    #             V    
    pubidList = getResearchPubs(researcherobj.context)


    pubEl = rdf.createElement('foaf:Publications')
    researchernode.appendChild(pubEl)
    seq = rdf.createElement('rdf:Seq')
    pubEl.appendChild(seq)
    
    for pubid in pubidList:
        li = rdf.createElement('rdf:li')
        seq.appendChild(li)
        doc = rdf.createElement('bibo:Document')
        li.appendChild(doc)
        bibo = rdf.createElement('bibo:pmid')
        doc.appendChild(bibo)
        bibo.appendChild(rdf.createTextNode(str(pubid)))

def getResearchPubs(researcherobj):
	
	# all of this really ought to go in RDSLocal somewhere
	# first try any bibliography lists
	# then try any back references

    contentFilter = {'portal_type' : 'BibliographyList'}
    selection = researcherobj.getFolderContents(contentFilter=contentFilter)
    pubsall = researcherobj.getBRefs('authorOf')
	
    res = []
    pubmedlist = []
    mtool = getToolByName(researcherobj, 'portal_membership')

    if selection:
        
    	for item in selection:
            biblist_obj = item.getObject()
            
            outgoing = biblist_obj.getReferences_list()
            incoming = []
            # if you want to show up the items which point to this one, too, then use the
            # line below
            #incoming = context.getBRefs('relatesTo') 
            
            in_out = outgoing+incoming
            for d in range(len(in_out)):
                try:
    				obj = in_out[d]
                except Unauthorized:
                		continue
            	if obj not in res:
    				if mtool.checkPermission('View', obj):
    						res.append(obj)
    
    if pubsall:
    	for item in pubsall:
    		res.append(item)
    	
    for pub in res:
    	
    	pubmedlist.append(pub.PMID())
    	
    return pubmedlist

	    	#do something with res...