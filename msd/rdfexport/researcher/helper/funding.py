#!/usr/bin/env python


def createFundingNodes(rdf, documentElement, resNodeID, researcherobj):  
    
    """
    <funding:FundingBody>
      <foaf:homePage rdf:resource="http://www.mrc.ac.uk/"/>
      <dc:title>Medical Research Council</dc:title>
      <funding:provides>
        <funding:Grant>
          <funding:funds rdf:nodeID="PaulBroca"/>
          <funding:startDate>1844-01-01</funding:startDate>
          <funding:endDate>1844-01-01</funding:endDate>
        </funding:Grant>
      </funding:provides>
    </funding:FundingBody>
    
    much the same for msd.researcher, note that the url isn't validated at entry
    so may need checking here
    
    """
    for fund in researcherobj.getFundingSources():
        
        fundingBody = rdf.createElement('funding:FundingBody')    
        documentElement.appendChild(fundingBody)
        
        fbname = rdf.createElement('dc:title')
        fbname.appendChild(rdf.createTextNode(fund['fundingbody'])) 
        fundingBody.appendChild(fbname)       
        fburl = rdf.createElement('foaf:homePage')
        fburl.setAttribute('rdf:resource',fund['url']) 
        fundingBody.appendChild(fburl)
        
        provides = rdf.createElement('funding:provides')
        fundingBody.appendChild(provides)
        grant = rdf.createElement('funding:Grant')
        provides.appendChild(grant)
        
        funds = rdf.createElement('funding:funds')
        funds.setAttribute('rdf:nodeID', resNodeID)
        grant.appendChild(funds)
        
        
        sdate = rdf.createElement('funding:startDate')
        grant.appendChild(sdate)
        sdate.appendChild(rdf.createTextNode(fund['startYear']))
 
        edate = rdf.createElement('funding:endDate')
        grant.appendChild(edate)
        edate.appendChild(rdf.createTextNode(fund['endYear']))  
              
        
        
       
        
#    
#def createTag(rdf, researchernode, researcherobj):
#         
#    
#    """
#    <foaf:fundedBy>
#      <res:Grant>
#        <ical:dtstart rdf:parseType="Resource">
#          <ical:date>1844-01-01</ical:date>
#        </ical:dtstart>
#        <ical:dtend rdf:parseType="Resource">
#          <ical:date>1880-31-12</ical:date>
#        </ical:dtend>
#        <foaf:fundedBy>
#          <res:FundingBody>
#            <foaf:homePage rdf:resource="http://www.mrc.ac.uk/"/>
#            <dc:title>Medical Research Council</dc:title>
#          </res:FundingBody>
#        </foaf:fundedBy>
#      </res:Grant>
#    </foaf:fundedBy>
#    """
#
#     
#    for fund in researcherobj.getFundingSources():
#        
#        pfb = rdf.createElement('foaf:fundedBy')
#        researchernode.appendChild(pfb)
#        
#        grant = rdf.createElement('res:Grant')
#        pfb.appendChild(grant)
#        
#        start = rdf.createElement('ical:dtstart')
#        grant.appendChild(start)
#        sdate = rdf.createElement('ical:Date')
#        start.appendChild(sdate)
#        sdate.appendChild(rdf.createTextNode(fund['startYear']))
#        
#        end = rdf.createElement('ical:dtend')
#        grant.appendChild(end)
#        edate = rdf.createElement('ical:Date')
#        end.appendChild(edate)
#        edate.appendChild(rdf.createTextNode(fund['endYear']))  
#          
#        gfb = rdf.createElement('foaf:fundedBy')
#        grant.appendChild(gfb)
#        fundingBody = rdf.createElement('res:FundingBody')
#        gfb.appendChild(fundingBody)
#        
#        fbname = rdf.createElement('dc:title')
#        fbname.appendChild(rdf.createTextNode(fund['fundingbody'])) 
#        fundingBody.appendChild(fbname)
#        
#        fburl = rdf.createElement('foaf:homePage')
#        fburl.setAttribute('rdf:resource',fund['url']) 
#        fundingBody.appendChild(fburl)
#        
        
    
#    res_funding = obj.getFundingSources()
#    if res_funding:
#        for fund in res_funding:
#            fundingbody = fund['fundingbody']
#            fundurl = fund['url']
#            fundstart = fund['startYear']
#            fundend = fund['endYear']
#            fundingtags = [{'level':1, 'tag':'foaf:fundedBy'},
#                            {'level':2, 'tag':'res:Grant'},
#                            {'level':3, 'tag':'ical:dtstart','att':['rdf:parseType','Resource']},
#                            {'level':4, 'tag':'ical:date','text':fundstart},
#                            {'level':3, 'tag':'ical:dtend','att':['rdf:parseType','Resource']},
#                            {'level':4, 'tag':'ical:date','text':fundend},
#                            {'level':3, 'tag':'foaf:fundedBy'},
#                            {'level':4, 'tag':'res:FundingBody'},
#                            {'level':5, 'tag':'foaf:homePage', 'att':['rdf:resource',fundurl]},
#                            {'level':5, 'tag':'dc:title', 'text':fundingbody},]
#                                
#            self.processTags(rdf,fundingtags,researcher)