"""My Game"""

import pygame

{% if cookiecutter.add_animation == 'y' -%}
import {{ cookiecutter.project_name.lower().replace(' ', '_').replace('-', '_') }}.animation
{% endif %}

# These set the height and width of the game window
WIDTH = 360
HEIGHT = 480

# This sets the frames per second and is used to advance the clock
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("{{ cookiecutter.project_name }}")
clock = pygame.time.Clock()

{% if cookiecutter.add_animation == 'y' -%}
animator = my_game.animation.Animator(screen, WIDTH, HEIGHT)
{% endif %}

running = True

"""
The core game loop
The game keeps running while running is True.
If you want the game to exit set running to False
"""
while running:
    # advance the game clock
    clock.tick(FPS)

    for event in pygame.event.get():
        # Pressing escape will quit the game
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
            running = False

        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    {% if cookiecutter.add_animation == 'y' -%}
    animator.animate()
    {% endif %}

# Quit pygame at the end
pygame.quit()
