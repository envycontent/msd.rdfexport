#!/usr/bin/env python

"""
This is basically a method to provide a 'fake' node ID if we don't have the
WebAuth (aka Oxford Username) field for that user.

Note that ultimately we should be able to look up webauth from the University's LDAP
from email address (which would be nice to do)

"""

def createNodeID(keyword):
    #remove spaces convert to lower case, remove inverted commas
    nodeid = keyword.lower().replace(' ','').replace('\'','')
    #remove brackets
    nodeid = nodeid.replace('(','-').replace(')','')
    #remove forward slashes
    nodeid = nodeid.replace('/','-')
    
    return nodeid