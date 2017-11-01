###############
### M A T H ###
###############


# Contains miscellaneous math operations
#
# These math functions create easy abstractions to remove unnecessary calculations.


def piecewise_func(variable, *args):
    """Takes in an variable name and a list of (boolean strings, functions)
    and returns a resulting piecewise function that takes in one variable 
    given by the parameter variable.

    >>> pw_function = piecewise_func('x', 
    ...     ('x < 10', lambda x: 'less than 10'), 
    ...     ('x == 10', lambda x: 'equal to 10'), 
    ...     ('10 < x', lambda x: 'greater than 10')
    ... )
    >>> pw_function(9)
    'less than 10'
    >>> pw_function(10)
    'equal to 10'
    >>> pw_function(11)
    'greater than 10'
    """
    def result_func(t):
        """If string eval to True, it returns the respective function called on t"""
        locals()[variable] = t
        for interval, func in args:
            if eval(interval):
                return func(t)
        assert False, 'func(' + variable + ') does not exist'
    return result_func

def collision_velocity(m1, v1, m2, v2):
    """Calculates the final velocities of two entities in an elastic collision

    >>> collision_velocity(8, 6, 4, -3)
    (0.0, 9.0)
    """
    v1f = v1*((m1-m2)/(m1+m2)) + v2*((2*m2)/(m1+m2))
    v2f = v1*((2*m1)/(m1+m2)) + v2*((m2-m1)/(m1+m2))
    return v1f, v2f

def time_of_collision(p1, v1, p2, v2):
    """This calculates the time at which the objects intersect. This is a more
    complex version of distance = rate * time

    >>> velocities, points = (10, -10), (0, 100)
    >>> time_of_collision(points[0], velocities[0], points[1], velocities[1])
    5.0
    """
    rate = v1 - v2
    distance = p2 - p1

    return distance/rate

def pythagorean_c(a, b):
    """This is the pythagorean theorem solving for the hypotenuse

    >>> pythagorean_c(3, 4)
    5.0
    """
    return (a**2 + b**2)**(1/2)

def pythagorean_b(a, c):
    """This is the pythagorean theorem solving for a side

    >>> pythagorean_b(3, 5)
    4.0
    """
    return (c**2 - a**2)**(1/2)

def point_of_intersection(s1, p1, s2, p2):
    """This returns the point of intersection of two lines

    >>> point_of_intersection(1, (0,0), -1, (2,0))
    (1.0, 1.0)
    """
    b1 = p1[1] - s1 * p1[0]
    b2 = p2[1] - s2 * p2[0]
    x = (b1 - b2)/(s2 - s1)
    y = s1 * x + b1
    return x, y