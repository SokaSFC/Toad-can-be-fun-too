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

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('platform.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1200, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('/Users/user/Documents/Data Science/Code/Files Organizer/Toad is fun as well/images/projectile.png')
        self.image = pygame.transform.scale(self.image,(26, 22))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x - 20
        self.rect.y = player.rect.y + 32
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        if self.rect.x > 1200:
            self.remove()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = player_image
        self.image = pygame.transform.scale(self.image,(37, 64))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 550
        self.vy = 0
        self.on_ground = True

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def jump(self):
        if self.on_ground:
            self.vy = -15
            self.on_ground = False

    def update(self):
        self.vy += 1
        self.rect.y += self.vy
        if self.rect.y >= 536:
            self.rect.y = 536
            self.vy = 0
            self.on_ground = True

player = Player()
game = Game()

    # Loop
run = True
while run:

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

            elif event.key == pygame.K_UP:
                game.player.jump()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        # Draw on screen
    screen.blit(bg_image, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    screen.blit(ground_image, (0, 600))
    screen.blit(ground_image, (600, 600))

    game.player.all_projectiles.draw(screen)
    
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    game.player.update()
        # Screen Update
    pygame.display.update()

pygame.quit()
