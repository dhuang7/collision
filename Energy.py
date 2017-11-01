###################
### E N E R G Y ###
###################


# Contains the Energy classes and Work
# 
# The Energy class will be directly calculated into the Collision system. All systems
# are going to be closed systems such that Energy is always conserved. This with 
# momentum will allow for accurate calculations during Collision.
# Work is included because the simplistic definition of Energy is the ability to do 
# work


from Vector import *


class Work:
    """The Summation of all the variable forces given each change in distance.
    Work is the change in Energy of a given object"""

    def __init__(self, force, position):
        """Calculates the work that has been done

        >>> force = Force(5, Acceleration(1, 2))
        >>> position = Position(1, 10)
        >>> Work(force, position).work
        100
        """
        self.force = force
        self.position = position
        self.work = force * position


class Energy:#(dict):
    """Energy describes the amount of force an object can exert. The Energy 
    class contains several methods to calculate different forms of Energy. 
    The Energy class inherits from dict."""

    def calc_kinetic(self, mass, velocity):
        """Calculates the Kinetic Energy of an object and saves in its 
        dictionary

        >>> energy = Energy()
        >>> energy.calc_kinetic(5, Velocity(-1, 10))
        250.0
        >>> energy['kinetic']
        250.0
        """
        result = .5 * mass * (velocity ** 2)
        #self['kinetic'] = self.get('kinetic', 0) + result
        return result

    def calc_potential(self):
        """This is a place holder:
        One could calculate the Energy in an object the moment a force is acting on it.
        Such way will save computation. One could calculate by waiting for how long the
        object moved and force. One could then do computation with Work."""