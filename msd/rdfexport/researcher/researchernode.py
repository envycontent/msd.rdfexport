
from msd.rdfexport.researcher.helper import utilities, base, researchsummary, image, assistant, departments,  webauth, themes, collaborators, funding, awards, college, keywords, publications
""" 
Creates: <res:Researcher>
            <stuff:stuff>
         </res:Researcher>          
Uses the /helper/ classes to add stuff 

1. there's a utility to generate a researcher node of some sort even if the oxford username is empty
2. We need to add the last modified date to the node - so that we can give an indication
of when this was last edited.

TO DO: look up an appropriate tag for last modified - probably a DC metadata tag

 
""" 
def createResearcherNode(obj,rdf):
#       create researcher node
    researcherNode = rdf.createElement('res:Researcher')    
    resNodeID = createSafeNodeID(obj)
    researcherNode.setAttribute('rdf:nodeID', resNodeID)                                    
    rdf.documentElement.appendChild(researcherNode)
    
#       adds the one liner literals
    base.createTag(rdf, researcherNode, obj)       
#       adds the research summary details
    researchsummary.createTag(rdf, researcherNode, obj)   
#       adds the image
    image.createTag(rdf, researcherNode, obj)      
#       adds the assistant
    assistant.createTag(rdf, researcherNode, obj)                    
#       adds a list of departments of which this researcher is a member             
    departments.createTag(rdf, researcherNode, obj)           
#       adds webauth account username       
    webauth.createTag(rdf, researcherNode, obj)            
#       adds themes on which this researcher works       
    themes.createTag(rdf, researcherNode, obj)          
#       adds collaborators      
    collaborators.createTag(rdf, researcherNode, obj)         
#    adds funding sources   (funding node points at researcher so needs doc element instead of res element and nodeID to hook together safely)
    funding.createFundingNodes(rdf, rdf.documentElement, resNodeID, obj)
#   adds awards     
    awards.createTag(rdf, researcherNode, obj)            
#   adds college
    college.createTag(rdf, researcherNode, obj)  
#   adds keywords and methodologies
    keywords.createTag(rdf, researcherNode, obj)   
#   adds publications
    publications.createTag(rdf, researcherNode, obj)  
 
def createSafeNodeID(obj): 
    # just in case oxfordid does not exist 
    return obj.getOxford_username() + '_' + utilities.createNodeID(obj.getLast_name())

