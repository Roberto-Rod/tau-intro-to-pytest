
#----------------------------------------------------------
# Class: Accumulator
#----------------------------------------------------------

class Accumulator:

    def __init__(self):
        self._count = 0             # single underscore makes the variable private
    
    @property                       # Get property (similAR TO GETTER AND SETTER IN C#)
    def count(self):
        return self._count
    
    def add(self, more=1):
        self._count += more


