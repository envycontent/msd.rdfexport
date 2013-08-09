#!/usr/bin/env python

"""
For the moment we're not using this, but it would be nice to do so
at some point. It isn't really relevant to the researcher RDF export, the
idea would be to export details of a web-presence, to compile a complete directory
of websites in the Medical Sciences Division. 

"""
       
        
def addWebPresenceElement(rdf, deptElement, deptName):        
           
    """
    <foaf:Organization rdf:about="http://www.psy.ox.ac.uk/">
    
    <foaf:homepage>
      <res:WebPresence>
        <dc:title>Department of Experimental Psychology Website</dc:title>
        <dc:creator>
          <foaf:Person>
            <foaf:mbox>anne.bowtell@medsci.ox.ac.uk</foaf:mbox>
          </foaf:Person>
        </dc:creator>
      </res:WebPresence>
    </foaf:homepage>
    """          
    
    #TODO - this will be real data in the future
    standardWebmaster = 'webmaster@medsci.ox.ac.uk'
    
    
    homepageProp = rdf.createElement('foaf:homepage')
    deptElement.appendChild(homepageProp)

    wpElem = rdf.createElement('res:WebPresence')
    homepageProp.appendChild(wpElem)
    
    title = rdf.createElement('dc:title')
    title.appendChild(rdf.createTextNode(deptName + ' Website'))
    wpElem.appendChild(title)
          
    creator = rdf.createElement('dc:creator')
    wpElem.appendChild(creator)      
    person = rdf.createElement('foaf:Person')
    creator.appendChild(person)      
    mbox = rdf.createElement('foaf:mbox')
    person.appendChild(mbox)
    mbox.appendChild(rdf.createTextNode(standardWebmaster))       
    
   