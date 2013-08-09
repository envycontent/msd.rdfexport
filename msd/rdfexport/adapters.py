import zope.interface

from msd.rdfexport.interfaces import IHarvestable

class BaseHarvestableResearcher(object):
    """
    Base adapter class to be used with IHarvestable interface. Made so that it works with RDSLocal researcher as it is.
    """

    zope.interface.implements(IHarvestable)

    def __init__(self, context):
        # Each adapter takes the object itself as the contruction
        # parameter and possibly provides other parameters for the
        # interface adaption
        self.context = context


    def getFolderContents(self):
        
        return self.context.getFolderContents()

    def getStrTitle(self):

        return self.context.getStrTitle()
    
    def title_or_id(self):
        
        return self.context.title_or_id()
    
    def getFirst_name(self):
        
        return self.context.getFirst_name()

    def getLast_name(self):
        
        return self.context.getLast_name()
        
    def getEmail(self):
        
        return self.context.getEmail()
    
    def absolute_url(self):
        
        return self.context.absolute_url()
    
    def getUrl(self):
        
        return self.context.getUrl()
    
    def getLetters_after_name(self):
        
        return self.context.getLetters_after_name()
    
    def getContact_address(self):
        
        return self.context.getContact_address()
    
    def getPhone(self):
        
        return self.context.getPhone()
    
    def getAlternate_phone(self):
        
        return self.context.getAlternate_phone()
    
    def getFax(self):
        
        return self.context.getFax()
    
    def getUniv_job_title(self):
        
        return self.context.getUniv_job_title()
    
    def getJob_title(self):
        
        return self.context.getJob_title()

    #assistant.py
    def getPa_phone(self):
        """ PA phonenumber """
        
        return self.context.getPa_phone()
    
    def getPa_fax(self):
        """ PA fax """
        
        return self.context.getPa_fax()
        
    def getPa_email(self):
        """ PA email """
    
        return self.context.getPa_email()
    
    def getPa_name(self):
        """ PA name """
        
        return self.context.getPa_name()
    
    #awards.py
    
    #awards
    def getAcademicBackground(self):
        """ Academic background, awards etc. """
        
        return self.context.getAcademicBackground()
    
    #collaborators
    def getGroupMembers(self):
        """ Current collaborators """
        
        return self.context.getGroupMembers()
        
    def getPastGroupMembers(self):
        """ Past collaborators """
        
        return self.context.getPastGroupMembers()
        
    def getAllCollaborators(self):
        """ Other collaborators """
        
        return self.context.getAllCollaborators()
        
    #college
    def getCollege(self):
        """ College """
        
        return self.context.getCollege()
        
    #departments
    def getUnits(self):
        """ Units """
        
        return self.context.getUnits()
    
    #funding
    def getFundingSources(self):
        """ Funding sources """
    
        return self.context.getFundingSources()
        
    #image
    def getImageCaption(self):
        """ Caption of the image """
    
        return self.context.getImageCaption()
    
    #keywords
    def getThemes2(self):
        """ Themes 2 """

        return self.context.getThemes2()
    
    def getThemes3(self):
        """ Themes 3 """
    
        return self.context.getThemes3()
        
    def getThemes4(self):
        """ Themes 4 """
    
        return self.context.getThemes4()
    
    def getThemes5(self):
        """ Themes 5 """
        
        return self.context.getThemes5()
            
    
    #Maybe this is not needed as it comes from the default archetypes?
    def Description(self):
        """ Description """
        
        return self.context.Description()
    
    def getSummary(self):
        """ Research summary """
    
        return self.context.getSummary()
        
    def getBiography(self):
        """ Biography """
    
        return self.context.getBiography()
    
    #themes
    def getThemes1(self):
        """ Themes 1 """
    
        return self.context.getThemes1()
    
    #webauth
    def getOxford_username(self):
        """ Online account username """
    
        return self.context.getOxford_username()