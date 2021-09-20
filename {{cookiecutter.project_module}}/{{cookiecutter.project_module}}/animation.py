import pygame

# define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

class Rectangle(pygame.sprite.Sprite):
    """
    Rectangle is a simple sprite
    """
    def __init__(self, screen, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.screen = screen

class Animator():
    """
    The Animator class manages the animation of sprites
    """
    def __init__(self, screen, width, height):
        self.screen = screen

        self.all_sprites = pygame.sprite.Group()
        self.rectangle = Rectangle(screen, width, height)
        self.all_sprites.add(self.rectangle)

        return

    def animate(self):
        """
        animate draws the next frame
        """
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

        return
