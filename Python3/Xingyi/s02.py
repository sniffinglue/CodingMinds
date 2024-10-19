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
  white_circle = pygame.draw.circle(screen, (193, 238, 238), (150, 150), 70)# surface, color, rect dimensions	
  green_line = pygame.draw.line(screen, (0, 255, 0), (0, 0), (500, 500), 10) # surface, color, start point, end point, width
  yellow_triangle = pygame.draw.polygon(screen, (248, 252, 3), [(10, 300), (40, 200), (70, 300) ]) # surface, color, list of points
  # pink_pentagon = pygame.draw.polygon(screen, (255, 0, 230), [(146, 300), (272, 370), (236, 495), (56, 495), (20, 370)])
  pink_pentagon = pygame.draw.polygon(screen, (255, 0, 230), [(450,250), (350,423), (150,423), (50,250), (150,77), (350,77)])

  
  white_square = pygame.draw.rect(screen, (255, 255, 255), (10, 10, 50, 50))
  teal_square = pygame.draw.rect(screen, (0, 255, 255), (10, 10, 30, 30))
  clock.tick(60)
