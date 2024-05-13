
import pygame
pygame.init()

    # Window:
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Toad can be fun as well")

    # Images Importations: 
        # Background Images:
bg_image = pygame.image.load('/Users/user/Documents/Data Science/Code/Files Organizer/Toad is fun as well/images/bg.png').convert_alpha()

        # Player Sprites
player_image = pygame.image.load('/Users/user/Documents/Data Science/Code/Files Organizer/Toad is fun as well/images/toad_sized.png').convert_alpha()

        # Plateforms Images
ground_image = pygame.image.load('/Users/user/Documents/Data Science/Code/Files Organizer/Toad is fun as well/images/ground.png').convert()

    #player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = player_image
        self.rect = self.image.get_rect()

player = Player()

    # Loop
run = True
while run:

    # Event Handler
        # Draw on screen
    screen.blit(bg_image, (0, 0))
    screen.blit(player_image, (0, 0))


        # Player Moves
    key = pygame.key.get_pressed()
    if key[pygame.K_q] == True:
        player.move_ip(-3, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(3, 0)
    elif key[pygame.K_z] == True:
        player.move_ip(0, -3)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 3)

        # Screen Update
    pygame.display.flip()

        # Closing While Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
