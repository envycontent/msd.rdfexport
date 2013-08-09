from zope.interface import Interface

class IRDFExport (Interface):
    """
    A layer specific to this product. Is registered using browserlayer.xml
    """

class ITransform(Interface):
    """An adapter that allows to rewrite links and the like in
    outgoing messages.
    """
    def __call__(text, subscription):
        """Return transformed text
        """


class IHarvestable(Interface):
    """An adapter that allows object to be rdf exported """

    
    #base
    def getStrTitle(self):
        """ Honorific Tittle of the person. Example: Dr """
        
    def title_or_id(self):
        """ Name of the person. Title or id of the object """
        
    def getFirst_name(self):
        """ First name of the person """
        
    def getLast_name(self):
        """ Last name of the person """
        
    def getEmail(self):
        """ Email of the person """
        
    def getUrl(self):
        """ Homepage of the person """
        
    def getLetters_after_name(self):
        """ Letters after the person's name. Named postNominals in the rdf. """

    def getContact_address(self):
        """ Contact address of the person """
        
    def getPhone(self):
        """ Phonenumber of the person """
        
    def getAlternate_phone(self):
        """ Alternative phone number """
    
    def getFax(self):
        """ Fax number """
        
    def getUniv_job_title(self):
        """ Job titles. """
        
    def getJob_title(self):
        """ Job title """

    #assistant
    def getPa_phone(self):
        """ PA phonenumber """
        
    def getPa_fax(self):
        """ PA fax """
        
    def getPa_email(self):
        """ PA email """
        
    def getPa_name(self):
        """ PA name """
        
    #awards
    def getAcademicBackground(self):
        """ Academic background, awards etc. """
        
    #collaborators
    def getGroupMembers(self):
        """ Current collaborators """
        
    def getPastGroupMembers(self):
        """ Past collaborators """
        
    def getAllCollaborators(self):
        """ Other collaborators """
        
    #college
    def getCollege(self):
        """ College """
        
    #departments
    def getUnits(self):
        """ Units """
        
    #funding
    def getFundingSources(self):
        """ Funding sources """
        
    #image
    def getImageCaption(self):
        """ Caption of the image """
    
    #keywords
    def getThemes2(self):
        """ Themes 2 """

    def getThemes3(self):
        """ Themes 3 """
        
    def getThemes4(self):
        """ Themes 4 """
    
    def getThemes5(self):
        """ Themes 5 """
            
            
    #publications
    #TODO: publications.py wasn't finished yet?

    #researchsummary
    
    #Maybe this is not needed as it comes from the default archetypes?
#    def Description(self):
#        """ Description """
        
    def getSummary(self):
        """ Research summary """
        
    def getBiography(self):
        """ Biography """
    
    #themes
    def getThemes1(self):
        """ Themes 1 """
    
    #webauth
    def getOxford_username(self):
        """ Online account username """
    
    