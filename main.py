'''
Puzzle Game
Move the character by using the left and right arrow keys

Credit https://www.pinterest.com/pin/748653138043874684/ for the character inspiration
'''


import pygame
import character # character.py

# Define the background image (Sorry for the bad art)
image = './images/1.png'
image = pygame.image.load(image)

# Setup the screen
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Puzzle Game") 

# Setup the character
char = character.Character(10, 10, "./images/character.png", screen)

# Setup the clock
clock = pygame.time.Clock()



# Start the game
pygame.init()

running = True
while running:
    for event in pygame.event.get():
        pygame.display.flip() 
        if event.type == pygame.QUIT: # Quit
            running = False

        if event.type == pygame.KEYDOWN: # If key down
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]: # If right arrow key pressed, move the character and set direction of character to the right
                char.x = char.x + 10
                char.direction("right")

            if keys[pygame.K_LEFT]: # If left arrow key pressed, move the character and set direction of character to the left
                char.x = char.x - 10
                char.direction("left")

        screen.blit(image, (0, 0))
        char.draw() # Redraw the character with it's position
        
        pygame.display.flip() 
        
        clock.tick(120)
