import pygame
import random
import math
from pygame import mixer

# Intialize the pygame
pygame.init()
pygame.joystick.init()
is_game_running = True
# score
score_value = 0
track_score = 10
font = pygame.font.Font('freesansbold.ttf', 24)
textX = 10
textY = 10

# game over text
game_over_message = 'Game Over !'
game_over_text = pygame.font.Font('freesansbold.ttf', 64)
game_overX = 190
game_overY = 150

# exit
exit_message = 'Exit'
exit_text = pygame.font.Font('freesansbold.ttf', 64)
exitX = 290
exitY = 320

# play again
play_message = 'Play'
play_text = pygame.font.Font('freesansbold.ttf', 64)
play_gameX = 290
play_gameY = 240

# create screen
screen = pygame.display.set_mode((800, 600))

# event is the activity in the pygame

# background
backgroundImg = pygame.image.load('background.jpg')

# background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = -2
bullet_state = 'ready'

# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
player_change = 2

# enemy
enemy_change = 1
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
total_enemy = 40
num_of_enemy = 5
for i in range(total_enemy):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(2, 730))
    enemyY.append(random.randint(2, 130))
    enemyX_change.append(enemy_change)
    enemyY_change.append(enemy_change)


def show_score(text_x, text_y):
    score = font.render('Score : ' + str(score_value), True, (100, 255, 100))
    screen.blit(score, (text_x, text_y))


def game_over_display(text_x, text_y):
    score = game_over_text.render(game_over_message, True, (255, 50, 50))
    screen.blit(score, (text_x, text_y))


def exit_display(text_x, text_y):
    score = exit_text.render(exit_message, True, (255, 50, 50))
    screen.blit(score, (text_x, text_y))


def play_message_display(text_x, text_y):
    score = play_text.render(play_message, True, (50, 250, 50))
    screen.blit(score, (text_x, text_y))


def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means draw


def enemy(x, y, position):
    screen.blit(enemyImg[position], (x, y))


def bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 25, y))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(((bullet_x-enemy_x)**2) + ((bullet_y-enemy_y)**2))
    if distance < 25:
        return True
    return False


# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB
    # background image
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # keyboard
        if is_game_running:
            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if bullet_state == 'ready':
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.play()
                        bulletX = playerX
                        bulletY = playerY
                        bullet(bulletX, bulletY)
                if event.key == pygame.K_LEFT:
                    playerX_change = -player_change
                if event.key == pygame.K_RIGHT:
                    playerX_change = player_change
                if event.key == pygame.K_UP:
                    playerY_change = -player_change
                if event.key == pygame.K_DOWN:
                    playerY_change = player_change
            if event.type == pygame.KEYUP:
                playerX_change = 0
                playerY_change = 0

            # joystick
            joystick_count = pygame.joystick.get_count()
            pygame.joystick.init()
            for i in range(joystick_count):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                if event.type == pygame.JOYAXISMOTION:
                    axis = joystick.get_axis(0)
                    # print("Axis {} value: {:>6.3f}".format(0, axis))
                    if axis < -0.5:
                        playerX_change = -player_change
                    elif axis > 0.5:
                        playerX_change = player_change
                    else:
                        playerX_change = 0
                if event.type == pygame.JOYAXISMOTION:
                    axis = joystick.get_axis(1)
                    # print("Axis {} value: {:>6.3f}".format(0, axis))
                    if axis < -0.5:
                        playerY_change = -player_change
                    elif axis > 0.5:
                        playerY_change = player_change
                    else:
                        playerY_change = 0
                if event.type == pygame.JOYBUTTONUP:
                    button = joystick.get_button(0)
                    # print("Button {:>2} value: {}".format(0, button))
                    if bullet_state == 'ready':
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.play()
                        bulletX = playerX
                        bulletY = playerY
                        bullet(bulletX, bulletY)

    # bullet movement
    if bulletY <= 0:
        bullet_state = 'ready'
        bulletY = 480

    if bullet_state == 'fire':
        bullet(bulletX, bulletY)
        bulletY += bulletY_change

    # checking for boundary for space
    if 2 <= playerX <= 730:
        playerX += playerX_change
        if playerX <= 2:
            playerX += 2
        if playerX >= 731:
            playerX -= 2
    if 75 <= playerY <= 530:
        playerY += playerY_change
        if playerY <= 75:
            playerY += 2
        if playerY >= 531:
            playerY -= 2

    # enemy movement
    if score_value > track_score:
        track_score += 5 # 5
        if num_of_enemy < 38:
            num_of_enemy += 1
        if num_of_enemy == 38:
            enemy_change = 2
    for i in range(num_of_enemy):
        # game over
        game_over = is_collision(enemyX[i], enemyY[i], playerX, playerY)
        if game_over:
            game_over_display(game_overX, game_overY)
            play_message_display(play_gameX, play_gameY)
            exit_display(exitX, exitY)
            mixer.music.stop()
            is_game_running = False
            break
        if enemyX[i] <= 2:
            enemyX_change[i] = enemy_change
            enemyY[i] += 50
        if enemyX[i] >= 731:
            enemyX_change[i] = -enemy_change
            enemyY[i] += 50
        enemyX[i] += enemyX_change[i]

        # collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bullet_state = 'ready'
            bulletY = 480
            score_value += 1
            enemyX[i] = random.randint(2, 730)
            enemyY[i] = random.randint(2, 130)
        enemy(enemyX[i], enemyY[i], i)

    # update the screen/ game window for any changes
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
    rect_exit = pygame.draw.rect(screen, (255, 0, 0), (290, 320, 130, 60))
    rect_play = pygame.draw.rect(screen, (255, 0, 0), (290, 240, 140, 60))

    if not is_game_running:
        pos = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        if rect_play.collidepoint(pos) and pressed1:
            is_game_running = True
            score_value = 0
            playerX = 370
            playerY = 480
            mixer.music.play(-1)
        if rect_exit.collidepoint(pos) and pressed1:
            exit()

