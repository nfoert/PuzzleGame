import pygame

class Character:
    def __init__(self, x, y, image, screen):
        self.x = x
        self.y = y
        self.screen = screen
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(image, (64, 64))
        self.direction_now = "right"
        

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def direction(self, direction="right"):
        '''
        direction accepts 'right' or 'left'
        '''

        if direction == "right" and self.direction_now == "left":
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction_now = "right"

        if direction == "left" and self.direction_now == "right":
            self.image = pygame.transform.flip(self.image, True, False)
            self.direction_now = "left"