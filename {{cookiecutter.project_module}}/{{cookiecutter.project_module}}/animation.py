import pygame

# define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

"""
Rectangle is a simple sprite
"""
class Rectangle(pygame.sprite.Sprite):
    def __init__(self, screen, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.screen = screen

"""
The Animator class manages the animation of sprites
"""
class Animator():
    def __init__(self, screen, width, height):
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.rectangle = Rectangle(screen, width, height)
        self.all_sprites.add(self.rectangle)

        return

    """
    animate draws the next frame
    """
    def animate(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

        return
