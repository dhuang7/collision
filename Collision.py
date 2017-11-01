#########################
### C O L L I S I O N ###
#########################


# Contains the Collision System
# 
# This system will detect and compute what happens after a collision of
# on or more objects.


import pygame, operator
from Math import *
from Vector import *

def single_collision(o1, o2):
    if pygame.sprite.collide_rect(o1.box, o2.box):
        if o1.pos[0] < o2.pos[0]:
            left, right = o1, o2
        else:
            left, right = o2, o1

        # if right.pos[0] - left.pos[0] - Position(1, left.dim[0]) < right.pos[0] + Position(1, right.dim[0]) - left.pos[0]:
        p1 = right.pos[0].magnitude * right.pos[0].direction
        p2 = left.pos[0].magnitude * left.pos[0].direction + left.dim[0]
        # else:
            # p1 = right.pos[0].magnitude * right.pos[0].direction + right.dim[0]
            # p2 = left.pos[0].magnitude * left.pos[0].direction

        v1 = right.vel[0].direction * right.vel[0].magnitude
        v2 = left.vel[0].direction *  left.vel[0].magnitude

        try:
            time = time_of_collision(p1, v1, p2, v2)
        except ZeroDivisionError:
            time = 0

        v1f, v2f = collision_velocity(left.mass, left.vel[0], right.mass, right.vel[0])
        left.vel[0].magnitude = v1f.magnitude
        left.vel[0].direction = v1f.direction
        right.vel[0].magnitude = v2f.magnitude
        right.vel[0].direction = v2f.direction

        left.collision_box(1 - time)
        right.collision_box(1 - time)

import sys
def collision(group):
    no_collision = 0
    previous_dct = {elem:None for elem in group}

    while no_collision != len(group):
        no_collision = 0

        for elem in group:

            collided_lst = pygame.sprite.spritecollide(elem, group, False)

            try:
                collided_lst.remove(elem)
            except ValueError:
                pass

            try:
                possible_collide = previous_dct[elem]
                collided_lst.remove(possible_collide)
                previous_dct[possible_collide] = elem
            except ValueError:
                pass

            if len(collided_lst) > 0:
                collided_dct = {collided:abs(elem.pos[0] - collided.pos[0]) for collided in collided_lst}# change later to time not closest position
                collided_sorted_lst = sorted(collided_dct.items(), key=operator.itemgetter(1))
                closest_collided = collided_sorted_lst[0][0]

                single_collision(elem.parent, closest_collided.parent)

                previous_dct[closest_collided] = elem

                no_collision = 0
            else:
                no_collision += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()