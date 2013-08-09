#!/usr/bin/env python

def createTag(rdf, researchernode, researcherobj):
    """
    <foaf:img>
      <foaf:Image rdf:about="http://www.neuroscience.ox.ac.uk/directory/paul-broca/image_mini">
        <dc:title>A picture of Paul Broca</dc:title>
      </foaf:Image>
    </foaf:img>
    
    msd.researcher: I think we need to check whether the image is there or not...
    
    """
    
    

    
    if researcherobj.getImageCaption():
        #check that this exists...
        img = rdf.createElement('foaf:img')
        imgsrc = rdf.createElement('foaf:Image')
        
        res_path = researcherobj.absolute_url()
        if res_path:
            
            imgsrc.setAttribute('rdf:about', res_path + '/image_mini')
            
        imgsrctitle = rdf.createElement('dc:title')
        imgsrctitle.appendChild(rdf.createTextNode(researcherobj.getImageCaption()))
        
        imgsrc.appendChild(imgsrctitle)
        img.appendChild(imgsrc)
        researchernode.appendChild(img)
    

