###############
### M A I N ###
###############

# This is the main function from which the surface can be seen from the window.
#
# This file can only be runned as __main__ and not as a module; therefore, it will be an empty file
# if it is runned as a module


import pygame, sys

from Entity import *
from Collision import *

def main():
    """This is the main function which contains the Game Loop"""

    pygame.init()

    # Random
    held = 0

    # Window
    size = width, height = 960, 540
    surface = pygame.display.set_mode(size, pygame.DOUBLEBUF)# | pygame.FULLSCREEN)

    # Clock
    clock = pygame.time.Clock()

    #Initialize
    # character = Character([1,1], [100,100], [100,100,100], surface, 100, 100000000)
    o0 = Orb0([0, 250], [40, 40], [0, 255, 0], surface, 1000000000, 100000000)
    o1 = Orb1([41, 250], [40, 40], [0, 0, 255], surface, 1, 100000000)
    o2 = Orb3([200, 250], [40, 40], [255, 0, 0], surface, 1, 100000000)
    o21 = Orb2([241, 250], [40, 40], [255, 0, 0], surface, 1, 100000000)
    o22 = Orb2([282, 250], [40, 40], [255, 0, 0], surface, 1, 100000000)
    o23 = Orb2([323, 250], [40, 40], [255, 0, 0], surface, 1, 100000000)
    o24 = Orb2([364, 250], [40, 40], [255, 0, 0], surface, 1, 100000000)
    # o25 = Orb2([405, 250], [40, 40], [255, 0, 0], surface, 1, 100000000)
    # o26 = Orb2([446, 250], [40, 40], [255, 0, 0], surface, 1, 100000000)
    o3 = Orb2([487, 250], [40, 40], [0, 255, 255], surface, 1, 100000000)
    o4 = Orb4([600, 250], [40, 40], [255, 0, 255], surface, 100000000000, 100000000)


    # Game Loop
    while True:

        # Framerate
        clock.tick(120)

        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit()

        if pygame.key.get_pressed()[pygame.K_SPACE] and not held or pygame.key.get_pressed()[pygame.K_RSHIFT]:
            held = 1

            # Draw
            # character.draw()
            o0.draw()
            o1.draw()
            o2.draw()
            o21.draw()
            o22.draw()
            o23.draw()
            o24.draw()
            # o25.draw()
            # o26.draw()
            o3.draw()
            o4.draw()

            # Collision
            collision(CollisionBox.entity_group)

            # Update and Fill
            pygame.display.flip()
            surface.fill((0, 0, 0))

        elif not pygame.key.get_pressed()[pygame.K_SPACE] and held:
            held = 0


if __name__ == "__main__":
    main()