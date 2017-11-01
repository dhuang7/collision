###################
### V E C T O R ###
###################


# Contains the Vector classes
# 
# These Vectors are all initiated such that they are relative to the entity they are describing;
# as a result, they do not have their own position value, since Vectors are still the same
# regardless of the position of the Vectors.


class Vector:
    """A single variable Vector that has direction and magnitude"""

    def __init__(self, direction, magnitude):
        self._direction = direction
        self.magnitude = magnitude

    def create_vector(vector_type, value):
        """This creates a vector using a scalar value

        >>> x = Vector.create_vector("Vector", 10)
        >>> x.direction, x.magnitude
        (1.0, 10)
        """
        if value == 0:
            return globals()[vector_type](0, 0)
        else:
            return globals()[vector_type](value/abs(value), abs(value))

    @property
    def direction(self):
        if self.magnitude == 0:
            return 0
        else:
            return self._direction

    @direction.setter
    def direction(self, value):
        self._direction = value

    def __add__(self, other):
        """Basic left side addition with Vectors

        Look at __radd__ for doctests
        """
        result = self.direction*self.magnitude + other.direction*other.magnitude
        if result == 0:
            return type(self)(0, 0)
        return type(self)(result/abs(result), abs(result))

    def __radd__(self, other):
        """Basic right side addition with Vectors

        >>> x, add_x = Vector(1, 10), Vector(-1, 4)
        >>> new_x = add_x + x
        >>> new_x.direction, new_x.magnitude
        (1.0, 6)
        """
        return self + other

    def __sub__(self, other):
        """Basic left side subtraction with Vectors

        look at __rsub__ for doctests
        """
        return self + -1*other

    def __rsub__(self, other):
        """Basic right side addition with Vectors

        >>> x, sub_x = Vector(1, 10), Vector(-1, 4)
        >>> new_x = sub_x - x
        >>> new_x.direction, new_x.magnitude
        (-1.0, 14.0)
        """
        return other + -1*self

    def scalar_mul(self, other):
        """This is multiplication of a scalar and a Vector

        >>> x = Vector(-1, 4)
        >>> new_x = x.scalar_mul(9)
        >>> new_x.direction, new_x.magnitude
        (-1.0, 36)
        """
        if other == 0:
            return type(self)(0, 0)
        return type(self)(self.direction*(other/abs(other)), abs(self.magnitude*other))

    def dot_product(self, other):
        """This is scalar product of two Vectors

        >>> x, y = Vector(-1, 9), Vector(1, 4)
        >>> x.dot_product(y)
        -36
        """
        return self.direction*self.magnitude * other.direction*other.magnitude

    def __mul__(self, other):
        """This is the left side default scalar multiplication or dot product

        >>> x = Vector(-1, 4)
        >>> new_x = x * 9
        >>> new_x.direction, new_x.magnitude
        (-1.0, 36)

        Look at __rmul__ for more doctests
        """
        if isinstance(other, (int, float)):
            return self.scalar_mul(other)
        if isinstance(other, Vector):
            return self.dot_product(other)

    def __rmul__(self, other):
        """This is the right side default scalar multiplication or dot product

        >>> x = Vector(-1, 4)
        >>> new_x = -8 * x
        >>> new_x.direction, new_x.magnitude
        (1.0, 32)

        >>> x, y = Vector(-1, 9), Vector(1, 4)
        >>> x * y
        -36
        """
        return self * other

    def __truediv__(self, other):
        """This is left side default scalar multiplication only

        >>> x = Vector(-1, 6)
        >>> new_x = x/2
        >>> new_x.direction, new_x.magnitude
        (-1.0, 3.0)
        """
        return self * (1/other)

    def __pow__(self, power):
        """This is dot product of itself

        >>> x = Vector(-1, 6)
        >>> x ** 2
        36
        """
        if power % 2 == 0:
            return self.magnitude ** power
        return type(self)(self.direction, self.magnitude ** power)

    def __abs__(self):
        """This is the absolute value of a vector

        >>> x = Vector(-1, 6)
        >>> abs(x)
        6
        """
        return self.magnitude

    def __lt__(self, other):
        """This is the less than operator

        >>> left, right = Vector(-1, 10), Vector(1, 23)
        >>> left < right
        True
        >>> left = Vector(1, 23)
        >>> left < right
        False
        >>> left = Vector(1, 24)
        >>> left < right
        False
        """
        return self.direction * self.magnitude < other.direction * other.magnitude

    def __le__(self, other):
        """This is the less than or equal to operator

        >>> left, right = Vector(-1, 10), Vector(1, 23)
        >>> left <= right
        True
        >>> left = Vector(1, 23)
        >>> left <= right
        True
        >>> left = Vector(1, 24)
        >>> left <= right
        False
        """
        return self.direction * self.magnitude <= other.direction * other.magnitude

    def __eq__(self, other):
        """This is the equal to operator

        >>> left, right = Vector(-1, 10), Vector(1, 23)
        >>> left == right
        False
        >>> left = Vector(1, 23)
        >>> left == right
        True
        >>> left = Vector(1, 24)
        >>> left == right
        False
        """
        return self.direction * self.magnitude == other.direction * other.magnitude

    def __ge__(self, other):
        """This is the greater than or equal to operator

        >>> left, right = Vector(-1, 10), Vector(1, 23)
        >>> left >= right
        False
        >>> left = Vector(1, 23)
        >>> left >= right
        True
        >>> left = Vector(1, 24)
        >>> left >= right
        True
        """
        return self.direction * self.magnitude >= other.direction * other.magnitude

    def __gt__(self, other):
        """This is the greater than operator

        >>> left, right = Vector(-1, 10), Vector(1, 23)
        >>> left > right
        False
        >>> left = Vector(1, 23)
        >>> left > right
        False
        >>> left = Vector(1, 24)
        >>> left > right
        True
        """
        return self.direction * self.magnitude > other.direction * other.magnitude


class Position(Vector):
    """Single variable Position Vector"""

    def __init__(self, direction, distance):
        super().__init__(direction, distance)

    def calc_velocity(self, time=1):
        """This calculates the velocity of the object given a certain time

        >>> pos_x = Position(1, 10)
        >>> vel_x = pos_x.calc_velocity(2)
        >>> vel_x.direction
        1.0
        >>> vel_x.magnitude
        5.0
        """
        return Velocity(self.direction*(time/abs(time)), self.magnitude/abs(time))


class Velocity(Vector):
    """Single variable Velocity Vector"""

    def __init__(self, direction, speed):
        super().__init__(direction, speed)

    def calc_position(self, time=1):
        """This calculates the position of the object given a certain time

        >>> vel_x = Velocity(1, 10)
        >>> pos_x = vel_x.calc_position(2)
        >>> pos_x.direction
        1.0
        >>> pos_x.magnitude
        20
        """
        return Position(self.direction*(time/abs(time)), self.magnitude*abs(time))

    def calc_acceleration(self, time=1):
        """This calculates the velocity of the object given a certain time

        >>> vel_x = Velocity(1, 10)
        >>> accel_x = vel_x.calc_acceleration(2)
        >>> accel_x.direction
        1.0
        >>> accel_x.magnitude
        5.0
        """
        return Acceleration(self.direction*(time/abs(time)), self.magnitude/abs(time))


class Acceleration(Vector):
    """Single variable Acceleration Vector"""

    def __init__(self, direction, magnitude):
        super().__init__(direction, magnitude)

    def calc_velocity(self, time=1):
        """This calculates the velocity of the object given a certain time

        >>> accel_x = Acceleration(1, 10)
        >>> vel_x = accel_x.calc_velocity(2)
        >>> vel_x.direction
        1.0
        >>> vel_x.magnitude
        20
        """
        return Velocity(self.direction*(time/abs(time)), self.magnitude*abs(time))


class Momentum(Vector):
    """Single variable Momentum Vector, descriptor of Velocity"""

    def __init__(self, mass, velocity):
        super().__init__(velocity.direction, mass*velocity.magnitude)
        self.mass = mass
        self.velocity = velocity
        
    def calc_force(self, time=1):
        """This calculates the velocity of the object given a certain time

        >>> mom_x = Momentum(5, Velocity(1, 2))
        >>> force_x = mom_x.calc_force(2)
        >>> force_x.direction
        1.0
        >>> force_x.magnitude
        5.0
        """
        return Momentum(self.mass, self.velocity.calc_acceleration(time))


class Force(Vector):
    """Single variable Force Vector, descriptor of Acceleration"""

    def __init__(self, mass, acceleration):
        super().__init__(acceleration.direction, mass*acceleration.magnitude)
        self.mass = mass
        self.acceleration = acceleration
        
    def calc_momentum(self, time=1):
        """This calculates the momentum of the object given a certain time

        >>> force_x = Force(5, Acceleration(1, 2))
        >>> mom_x = force_x.calc_momentum(2)
        >>> mom_x.direction
        1.0
        >>> mom_x.magnitude
        20
        """
        return Momentum(self.mass, self.acceleration.calc_velocity(time))