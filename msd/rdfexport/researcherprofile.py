from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Acquisition import aq_inner, aq_parent, aq_self
from DateTime import DateTime
from AccessControl import Unauthorized
from xml.dom.minidom import *

from msd.rdfexport.researcher.helper import departments, themes
from msd.rdfexport.researcher import researchernode
from rdfexporter import RdfExporter

from msd.rdfexport.interfaces import IHarvestable




""" 
Outputs a single Researchers with all its metadata as well as some extra information on themes and organisations connected to that researcher 
Extends RdfExporter for the DOM document setup 
Uses resesarchernode for the <res:researcher> node
"""    
class ResearcherProfileDocument(BrowserView, RdfExporter):



    def __call__(self):
        # create DOM document.  Add all the namespaces of various vocabs - foaf, bio, etc
        rdf = self.createDomDocWithNamespaces()       
        self.addDateModified(rdf)
        # the data object
        obj = IHarvestable(self.context)
        # add <res:researcher> node - this is the main stuff
        researchernode.createResearcherNode(obj,rdf)
            
        #related information: departments, themes, subthemes which relate to this reasearcher                      
        #!departments.addDepartmentsToDocument(rdf, obj.getUnits())                        
        #!themes.addThemesToDocument(rdf, obj.getThemes1() )                              
        #themes.addSubThemesToDocument(rdf, obj.getThemes3() ) 
                        
        self.context.REQUEST.response.setHeader('Content-Type', 'application/rdf+xml')
        #return rdf.toprettyxml()
        return rdf.toxml()    


    def addDateModified(self, rdf):
        about = rdf.createElement('rdf:Description')
        about.setAttribute('rdf:about',"")
        modified = rdf.createElement('dcterms:modified')
        modified.appendChild(rdf.createTextNode(self.context.ModificationDate()))
        about.appendChild(modified)        
        rdf.documentElement.appendChild(about)
        

""" 
Outputs a list of ALL Researchers with basic metadata. 
Extends RdfExporter for the DOM document setup 
Uses resesarchernode for the multiple <res:researcher> nodes
"""
class AllResearchersProfilesDocument(BrowserView, RdfExporter):  
    
    def __call__(self):
        
        # create DOM document.  Add all the namespaces of various vocabs - foaf, bio, etc
        rdf = self.createDomDocWithNamespaces()

        # query for all Researchers
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        query = {}
        query['portal_type'] = 'Person'        
        researcher_objs = portal_catalog.searchResults(query)
        
        # for each researcher, create an <rdf:Researcher> node with contents 
        for researcher_obj in researcher_objs:
            obj = researcher_obj.getObject()
            researchernode.createResearcherNode(obj,rdf)
        
        # return xml to browser
        self.context.REQUEST.response.setHeader('Content-Type', 'application/rdf+xml')
        return rdf.toxml()        
    
    

      
  

    
    
            

        
