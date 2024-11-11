""" A simple social network for tracking connections between people. """


class person: 
    """ A person in the social netwwork.
    
    Attributes: 
        name(str): The person's name 
        connections(set of person): other people in the social network who 
            know this person
        
    """
    def __initi__(self,name):
        """ Initialize a new person object. """
        self.name = name 
        self.connections = set()
        
    def connect(self, person2):
        """ Connect with person2. 
        
        Args: 
            person2 (Person): the other person to connect to. s
        """