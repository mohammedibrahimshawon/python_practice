import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Ball settings
ball_width = 15
ball_height = 15
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))

# Paddle settings
paddle_width = 10
paddle_height = 100
paddle_speed = 10

# Scores
player1_score = 0
player2_score = 0

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 74)

# Paddle positions
player1_y = (screen_height - paddle_height) // 2
player2_y = (screen_height - paddle_height) // 2

# Ball position
ball_x = screen_width // 2
ball_y = screen_height // 2

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= paddle_speed
    if keys[pygame.K_s] and player1_y < screen_height - paddle_height:
        player1_y += paddle_speed
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= paddle_speed
    if keys[pygame.K_DOWN] and player2_y < screen_height - paddle_height:
        player2_y += paddle_speed

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= screen_height - ball_height:
        ball_speed_y *= -1

    # Ball collision with paddles
    if (ball_x <= paddle_width and player1_y < ball_y < player1_y + paddle_height) or (
            ball_x >= screen_width - paddle_width - ball_width and player2_y < ball_y < player2_y + paddle_height):
        ball_speed_x *= -1

    # Scoring
    if ball_x <= 0:
        player2_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
    if ball_x >= screen_width - ball_width:
        player1_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))

    # Drawing everything
    screen.fill(black)
    pygame.draw.rect(screen, white, (0, player1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (screen_width - paddle_width, player2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, white, (ball_x, ball_y, ball_width, ball_height))

    player1_text = font.render(str(player1_score), True, white)
    player2_text = font.render(str(player2_score), True, white)
    screen.blit(player1_text, (screen_width // 4, 10))
    screen.blit(player2_text, (screen_width * 3 // 4, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
