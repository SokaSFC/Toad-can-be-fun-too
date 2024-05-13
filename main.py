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

class Game():
    def __init__(self):
        self.player = Player()
        self.pressed = {

        }


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 550

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

player = Player()
game = Game()

    # Loop
run = True
while run:

    # Event Handler
        # Draw on screen
    screen.blit(bg_image, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    screen.blit(ground_image, (0, 600))
    screen.blit(ground_image, (600, 600))

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()


        # Screen Update
    pygame.display.flip()

        # Closing While Quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

pygame.quit()
