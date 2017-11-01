###################
### E N T I T Y ###
###################


# Contains the Entity classes
#
# These classes are the objects that will be blit onto surfaces. These objects are related to the
# Vector class by being the center of their own coordinate system. Each object will have the ability
# to calculate where it was and where it will be based on where it currently is. This is to better
# the accuracy of the Collision System


import pygame, math, random

from Vector import *
from Energy import *
from Math import *


class Entity(pygame.sprite.Sprite):
    """This is the default entity class"""

    def __init__(self, pos, dim, color, surface, mass, tensile_strength):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [Vector.create_vector("Position", elem) for elem in pos]
        self.dim = list(dim)
        self.color = list(color)
        self.surface = surface
        self.mass = mass
        self.vel = [Velocity(0, 0), Velocity(0, 0)]
        self.tensile_strength = tensile_strength # temporary

    def point_on_edge(self, slope, point):
        """This returns a point on the edge that is intersected by the given line"""
        return 0, 0


class Box(Entity):
    """Anything that appears on screen as a rectangle will be a descendent of this class"""

    def draw(self, size=None, frames=None):
        self.rect = pygame.Rect([round(pos.direction*pos.magnitude) for pos in self.pos], self.dim)
        pygame.draw.rect(self.surface, self.color, self.rect)


class Orb(Entity):
    """Anything that appears on screen as a circle will be a descendent of this class"""

    def point_on_edge(self, slope, point):
        """This is for circles only"""
        y_inter = point[1] - s1 * point[0]
        h, k = [round(pos.direction*pos.magnitude + self.radius) for pos in self.pos]
        a = m**2 + 1
        b = 2*(m*(y_inter-k) - h)
        c = (y_inter-k)**2 - self.radius**2 + h**2
        x1, x2 = (-b + (b**2 - 4*a*c)**(1/2))/(2*a), (-b - (b**2 - 4*a*c)**(1/2))/(2*a)
        y1, y2 = x1 * slope + y_inter, x2 * slope + y_inter
        return (x1, y1), (x2, y2)

    def draw(self, size=None, frames=None):
        self.rect = pygame.Rect([round(pos.direction*pos.magnitude) for pos in self.pos], self.dim)
        self.radius = sum(self.dim)/4
        pygame.draw.circle(self.surface, self.color, [round(pos.direction*pos.magnitude + self.radius) for pos in self.pos], round(self.radius))


class MovingOrb(Orb):
    """This is a circle that moves"""

    def calc_position(self, time=1):
        """This calculates the position of this object a certain time later or earlier

        >>> character = Character([10, 5], [20, 35], (0,0,0), None, 10, 10)
        >>> character.vel[0].direction, character.vel[1].direction = 1, 1
        >>> character.vel[0].magnitude, character.vel[1].magnitude = 5, 7
        >>> [pos.direction*pos.magnitude for pos in character.calc_position(2)]
        [20.0, 19.0]
        >>> [pos.direction*pos.magnitude for pos in character.calc_position(-2)]
        [0, -9.0]
        """
        return [vel.calc_position(time) + pos for vel, pos in zip(self.vel, self.pos)]

    def move(self, size=None, frames=None):
        self.pos = self.calc_position()

    def draw(self, size=None, frames=None):
        self.move(size, frames)
        super().draw(size, frames)


class CollisionBox(pygame.sprite.Sprite):
    """Collision area of moving object"""

    entity_group = pygame.sprite.Group()#[]

    def __init__(self, pos, dim, color, surface):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [Vector.create_vector("Position", elem) for elem in pos]
        self.dim = list(dim)
        self.color = list(color)
        self.surface = surface
        self.parent = None
        self.entity_group.add(self)

    def draw(self):
        self.rect = pygame.Rect([round(pos.direction*pos.magnitude) for pos in self.pos], self.dim)
        # pygame.draw.rect(self.surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), self.rect)


class Collidable(MovingOrb):
    """A circle that is collidable"""

    def __init__(self, pos, dim, color, surface, mass, tensile_strength):
        super().__init__(pos, dim, color, surface, mass, tensile_strength)
        self.box = CollisionBox(pos, dim, color, surface)
        self.box.parent = self

    def collision_box(self, scale=1):
        pos_value = self.pos[0].magnitude * self.pos[0].direction

        if self.vel[0].direction == 1:
            self.box.pos[0] = Vector.create_vector("Position", pos_value)
            self.box.dim[0] = self.vel[0].magnitude + self.dim[0]*scale
        elif self.vel[0].direction == -1:
            self.box.pos[0] = Vector.create_vector("Position", pos_value - self.vel[0].magnitude*scale)
            self.box.dim[0] = self.vel[0].magnitude + self.dim[0]*scale
        else:
            self.box.pos[0] = Vector.create_vector("Position", pos_value)
            self.box.dim[0] = self.dim[0]

        self.box.draw()

    def draw(self, size=None, fps=None):
        super().draw()
        self.collision_box()


class Character(MovingOrb):
    """This is a circle that is moveable by keyboard inputs"""

    def move(self, size=None, frames=None):
        key_press = [pygame.key.get_pressed()[elem] for elem in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]]
        if key_press[0]:
            self.vel[1].direction, self.vel[1].magnitude = -1, 5
        if key_press[1]:
            self.vel[1].direction, self.vel[1].magnitude = 1, 5
        if key_press[2]:
            self.vel[0].direction, self.vel[0].magnitude = -1, 5
        if key_press[3]:
            self.vel[0].direction, self.vel[0].magnitude = 1, 5

        if not any(key_press[:2]) or all(key_press[:2]):
            self.vel[1].direction, self.vel[1].magnitude = 0, 0
        if not any(key_press[2:]) or all(key_press[2:]):
            self.vel[0].direction, self.vel[0].magnitude = 0, 0

        super().move()


class Orb0(Collidable):
    """This is a circle that moves"""

    def __init__(self, pos, dim, color, surface, mass, tensile_strength):
        super().__init__(pos, dim, color, surface, mass, tensile_strength)
        self.vel[0].direction, self.vel[0].magnitude = 0, 0


class Orb1(Collidable):
    """This is a circle that moves"""
    def __init__(self, pos, dim, color, surface, mass, tensile_strength):
        super().__init__(pos, dim, color, surface, mass, tensile_strength)
        self.vel[0].direction, self.vel[0].magnitude = 1, 10


class Orb2(Collidable):
    """This is a circle that moves"""
    def __init__(self, pos, dim, color, surface, mass, tensile_strength):
        super().__init__(pos, dim, color, surface, mass, tensile_strength)
        self.vel[0].direction, self.vel[0].magnitude = 0, 0


class Orb3(Collidable):
    """This is a circle that moves"""
    def __init__(self, pos, dim, color, surface, mass, tensile_strength):
        super().__init__(pos, dim, color, surface, mass, tensile_strength)
        self.vel[0].direction, self.vel[0].magnitude = 0, 0


class Orb4(Collidable):
    """This is a circle that moves"""
    def __init__(self, pos, dim, color, surface, mass, tensile_strength):
        super().__init__(pos, dim, color, surface, mass, tensile_strength)
        self.vel[0].direction, self.vel[0].magnitude = 0, 0