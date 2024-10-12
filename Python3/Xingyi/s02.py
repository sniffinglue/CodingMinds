# classes:
    # It is like a Cats in general are a class fro example, eachone of them is differnt 
# Object -> Jessy is an object from class cat which has orange color, 2 years of age and meowing sound 

# Method vs Attributes:
# Actions(stuff that we do) vs stuff we have 

# OOP -> Object Oriented Programming 

import pygame

pygame.init()
clock = pygame.time.Clock() # The clock tracks how fast the game is running.
screen = pygame.display.set_mode((500, 500))

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
                                            #R,   G,   B      X,  Y,  W,  H
  pygame.display.update()
  white_square = pygame.draw.rect(screen, (193, 238, 238), (10, 10, 50, 50))# surface, color, rect dimensions	
  clock.tick(60)
