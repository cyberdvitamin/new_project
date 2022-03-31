import pygame, math, random
from pygame import mixer

pygame.mixer.init()

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1280, 720))

# Background
background = pygame.image.load('assets/images/background.png')

# Background Sound
# music = mixer.music.load('background.wav')
music = pygame.mixer.Sound('assets/audio/background.wav')
music.set_volume(0.01)
music.play(-1)
# mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption('Akatsuki')
icon = pygame.image.load('assets/images/Akatsuki game Icon.png')
pygame.display.set_icon(icon)

# Player
class Player:
    image = pygame.image.load('assets/images/spaceship.png')
    x = 672
    y = 600
    x_change = 0
    y_change = 0

    def player_output(x, y):
        screen.blit(Player.image, (x, y))

    def isCollision(enemyX, enemyY, playerX, playerY):
        distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
        if distance < 64:
            return True
        else:
            return False

    def mouse_move(x, y):
        pygame.mouse.set_visible(False)
        Player.x = x - 32
        Player.y = y - 32

    '''def keyboard_move():
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            Player.y_change = -10
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            Player.y_change = 10
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            Player.y_change = -10
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            Player.y_change = 10
        if event.key == pygame.K_SPACE:
            if Bullet.state == "ready":
                Bullet.sound()'''

# Enemy
class Enemy:
    x = []
    y = []
    x_change = []
    y_change = []
    num_of_enemies = 6
    image = []
    for i in range(num_of_enemies):
        image.append(pygame.image.load('assets/images/enemy.png'))
    for i in range(num_of_enemies):
        x.append(random.randint(0, 1216))
        y.append(random.randint(50, 320))
        x_change.append(4)
        y_change.append(70)

    def enemy_output(x, y, i):
        screen.blit(Enemy.image[i], (x, y))

    def isCollision(enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
        if distance < 27:
            return True
        else:
            return False


# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

# Bullet
class Bullet:
    image = pygame.image.load('assets/images/bullet.png')
    x = 0
    y = Player.y
    x_change = 0
    y_change = 20
    state = "ready"

    def bullet_move(self):
        self.x += self.x_change
        self.y += self.y_change

    def fire(x, y):
        Bullet.state
        Bullet.state = "fire"
        screen.blit(Bullet.image, (x + 16, y + 10))

    def sound():
        sound = mixer.Sound('assets/audio/laser.wav')
        sound.set_volume(0.02)
        sound.play()
        # Get the current X coordinates of the spaceship
        Bullet.x = Player.x
        Bullet.fire(Bullet.x, Bullet.y)

    def movement():
    # Bullet Movement
        if Bullet.y <= 0:
            Bullet.y = Player.y
            Bullet.state = "ready"

        if Bullet.state == "fire":
            Bullet.fire(Bullet.x, Bullet.y)
            Bullet.y -= Bullet.y_change

# Score
class Score:
    score_value = 0
    font = pygame.font.Font('assets/fonts/buttershine.otf', 32)
    textX = 10
    textY = 10
    def show_score(x, y):
        score = Score.font.render('Score: ' + str(Score.score_value), True, (0, 128, 0))
        screen.blit(score, (x, y))


# Game Over text
over_font = pygame.font.Font('assets/fonts/buttershine.otf', 64)
game_over = False


def game_over_text(x, y):
    global game_over
    over_text = over_font.render('GAME OVER', True, (255, 0, 0))
    screen.blit(over_text, (440, 296))
    over_text = over_font.render('Press R to Play again!', True, (0, 128, 0))
    screen.blit(over_text, (300, 396))
    game_over = True


# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))
    # Background Image
    screen.blit(background, (0, 0))

    # Mouse variables
    x_mouse, y_mouse = pygame.mouse.get_pos()
    Player.mouse_move(x_mouse, y_mouse)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


        # if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Player.y_change = -10
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Player.y_change = 10
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Player.y_change = -10
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Player.y_change = 10
            if event.key == pygame.K_SPACE:
                if Bullet.state == "ready":
                    Bullet.sound()
            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0]:
                if Bullet.state == "ready":
                    Bullet.sound()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                Player.y_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Player.x_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                Player.x_change = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r and game_over:
                for i in range(Enemy.num_of_enemies):
                    Enemy.image.append(pygame.image.load("assets/images/enemy.png"))
                    Enemy.x.append(random.randint(0, 1216))
                    Enemy.y.append(random.randint(50, 320))
                game_over = False

    # Checking for boundaries of spaceship, so it doesn't go out of bounds
    Player.x += Player.x_change
    Player.y += Player.y_change

    if Player.x <= 0:
        Player.x = 0
    elif Player.x >= 1216:
        Player.x = 1216

    if Player.y <= 0:
        Player.y = 0
    elif Player.y >= 656:
        Player.y = 656

    # Enemy Movement
    for i in range(Enemy.num_of_enemies):
        # Game Over
        collisionPlayer = Player.isCollision(Enemy.x[i], Enemy.y[i], Player.x, Player.y)
        if Enemy.y[i] > 656 or collisionPlayer:
            for j in range(Enemy.num_of_enemies):
                Enemy.y[j] = 2000
                game_over_text(640, 360)
                break
            game_over_text(640, 360)
            break

        Enemy.x[i] += Enemy.x_change[i]
        if Enemy.x[i] <= 0:
            Enemy.x_change[i] = 3
            Enemy.y[i] += Enemy.y_change[i]
        elif Enemy.x[i] >= 1216:
            Enemy.x_change[i] = -3
            Enemy.y[i] += Enemy.y_change[i]

        # Collision
        collision = Enemy.isCollision(Enemy.x[i], Enemy.y[i], Bullet.x, Bullet.y)
        if collision:
            explosion_Sound = mixer.Sound('assets/audio/explosion.wav')
            explosion_Sound.set_volume(0.04)
            explosion_Sound.play()
            Bullet.y = Player.y
            Bullet.state = "ready"
            Score.score_value += 1
            Enemy.x[i] = random.randint(0, 1216)
            Enemy.y[i] = random.randint(50, 320)

        Enemy.enemy_output(Enemy.x[i], Enemy.y[i], i)

    Bullet.movement()

    Player.player_output(Player.x, Player.y)
    Score.show_score(Score.textX, Score.textY)
    pygame.display.update()