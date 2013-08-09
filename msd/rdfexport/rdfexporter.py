#!/usr/bin/env python

from xml.dom.minidom import *

class RdfExporter:
    
    def createDomDocWithNamespaces(self):
     
        implementation = getDOMImplementation()
        rdf = implementation.createDocument('http://www.w3.org/1999/02/22-rdf-syntax-ns#','rdf:RDF',None)
        rdf.documentElement.setAttribute('xmlns:rdfs','http://www.w3.org/2000/01/rdf-schema#')
        rdf.documentElement.setAttribute('xmlns:rdf','http://www.w3.org/1999/02/22-rdf-syntax-ns#')
        rdf.documentElement.setAttribute('xmlns:bio','http://purl.org/vocab/bio/0.1/')
        rdf.documentElement.setAttribute('xmlns:foaf','http://xmlns.com/foaf/0.1/')
        rdf.documentElement.setAttribute('xmlns:geo','http://www.w3.org/2003/01/geo/wgs84_pos#')
        rdf.documentElement.setAttribute('xmlns:dc','http://purl.org/dc/elements/1.1/')
        rdf.documentElement.setAttribute('xmlns:con','http://www.w3.org/2000/10/swap/pim/contact#')
        rdf.documentElement.setAttribute('xmlns:dcterms','http://purl.org/dc/terms/')
        rdf.documentElement.setAttribute('xmlns:ical','http://www.w3.org/2002/12/cal/ical#')       
        # old namespace: http://www.medsci.ox.ac.uk/vocab/researcher/0.1/
        rdf.documentElement.setAttribute('xmlns:res','http://purl.oclc.org/oxford/researcher/')
        rdf.documentElement.setAttribute('xmlns:funding','http://vocab.ouls.ox.ac.uk/projectfunding/projectfunding#')
        rdf.documentElement.setAttribute('xmlns:aiiso','http://purl.org/vocab/aiiso/schema#')
        rdf.documentElement.setAttribute('xmlns:bibo','http://purl.org/ontology/bibo/')        
                
        return rdf