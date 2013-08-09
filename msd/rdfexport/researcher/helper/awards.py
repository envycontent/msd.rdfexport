#!/usr/bin/env python
# -*- coding: utf-8 -*-

        
def createTag(rdf, researchernode, researcherobj):
    
    """
    <res:holdsAward>
      <res:Award>
        <dc:title>Fellowship</dc:title>
        <res:awardedBy>
          <foaf:Organization rdf:about="http://www.academie-francaise.fr/">
            <dc:title>Acad̩mie Fran̤aise</dc:title>
          </foaf:Organization>
        </res:awardedBy>
        <ical:dtstart rdf:parseType="Resource">
          <ical:date>1874-01-01</ical:date>
        </ical:dtstart>
        <ical:dtend rdf:parseType="Resource">
          <ical:date>1880-31-12</ical:date>
        </ical:dtend>
      </res:Award>
    </res:holdsAward>
    
    msd.researcher - note the TODO below. I've added a URL field 
    to the getAcademicBackground datagrid field, note that this isn't validated
    on data entry
    
    TODO - I'm wondering if the rdf:about attribute can be omitted - yes fine - blank node
    
    """
    ## TODO ##
    awardingOrganizationURL = "http://nourl.as.yet"
 
 
    for award in researcherobj.getAcademicBackground():
        
        holdsAward = rdf.createElement('res:holdsAward')
        researchernode.appendChild(holdsAward)
        
        awardel = rdf.createElement('res:Award')
        holdsAward.appendChild(awardel)
        
        awardTitle = rdf.createElement('dc:title')
        awardTitle.appendChild(rdf.createTextNode(award['award']))
        awardel.appendChild(awardTitle)

        if award['startYear']:
        
            start = rdf.createElement('ical:dtstart')
            start.setAttribute('rdf:parseType', 'Resource')
            awardel.appendChild(start)
            sdate = rdf.createElement('ical:Date')
            start.appendChild(sdate)
            sdate.appendChild(rdf.createTextNode(award['startYear']))
        
        if award['endYear']:
        
            end = rdf.createElement('ical:dtend')
            end.setAttribute('rdf:parseType', 'Resource')
            awardel.appendChild(end)
            edate = rdf.createElement('ical:Date')
            end.appendChild(edate)
            edate.appendChild(rdf.createTextNode(award['endYear']))  
          
        if award['institution']:
        
            by = rdf.createElement('res:awardedBy')
            awardel.appendChild(by)
            orgn = rdf.createElement('foaf:Organisation')
            by.appendChild(orgn)
        
            #orgn.setAttribute('rdf:about', awardingOrganizationURL)
        
            orgname = rdf.createElement('dc:title')
            orgname.appendChild(rdf.createTextNode(award['institution'])) 
            orgn.appendChild(orgname)
        
        
#    #awards
#    
#    if res_awards:
#        for award in res_awards:
#            
#            awardtype = award['award']
#            awardurl = "http://nourl.as.yet"
#            awardorg = award['institution']
#            datestart = award['startYear']
#            dateend = award['endYear']
#            
#            awardtags = [{'level':1,'tag':'res:holdsAward'},
#                    {'level':2,'tag':'res:Award'},
#                    {'level':3, 'tag':'dc:title','text':awardtype},
#                    {'level':3, 'tag':'res:awardedBy'},
#                    {'level':4, 'tag':'foaf:Organization', 'att':['rdf:about',awardurl]},
#                    {'level':5,'tag':'dc:title','text':awardorg},
#                    {'level':3, 'tag':'ical:dtstart','att':['rdf:parseType','Resource']},
#                    {'level':4, 'tag':'ical:date','text':datestart},
#                    {'level':3, 'tag':'ical:dtend','att':['rdf:parseType','Resource']},
#                    {'level':4, 'tag':'ical:date','text':dateend},]
#            
#            
#                    
#            self.processTags(rdf,awardtags,researcher)     