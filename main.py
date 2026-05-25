import pygame

print('Setup start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for envet in pygame.event.get():
        if envet.type == pygame.QUIT:
            pygame.quit()  # Close Window
            quit()  # end pygame
