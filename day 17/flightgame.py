import pygame
import random

# Initialize the game
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flight Game")

# Load images
plane_img = pygame.image.load("plane.png")
plane_img = pygame.transform.scale(plane_img, (70, 50))
background_img = pygame.image.load("background.png")
obstacle_img = pygame.image.load("obstacle.png")

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Game variables
plane_x = width // 4
plane_y = height // 2
plane_speed = 5
obstacle_width = 70
obstacle_height = 50
obstacle_x = width
obstacle_y = random.randint(0, height - obstacle_height)
obstacle_speed = 7
score = 0

# Main game loop
running = True
while running:
    window.fill(white)
    window.blit(background_img, (0, 0))
    
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control the plane
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and plane_y > 0:
        plane_y -= plane_speed
    if keys[pygame.K_DOWN] and plane_y < height - 50:
        plane_y += plane_speed
    if keys[pygame.K_LEFT] and plane_x > 0:
        plane_x -= plane_speed
    if keys[pygame.K_RIGHT] and plane_x < width - 70:
        plane_x += plane_speed

    # Move the obstacle
    obstacle_x -= obstacle_speed
    if obstacle_x < -obstacle_width:
        obstacle_x = width
        obstacle_y = random.randint(0, height - obstacle_height)
        score += 1

    # Check for collision
    plane_rect = pygame.Rect(plane_x, plane_y, 70, 50)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if plane_rect.colliderect(obstacle_rect):
        running = False

    # Draw plane and obstacle
    window.blit(plane_img, (plane_x, plane_y))
    window.blit(obstacle_img, (obstacle_x, obstacle_y))

    # Draw the score
    score_text = small_font.render(f"Score: {score}", True, black)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    pygame.time.delay(30)

# Game over
window.fill(white)
game_over_text = font.render("Game Over", True, black)
final_score_text = small_font.render(f"Final Score: {score}", True, black)
window.blit(game_over_text, (width // 2 - 150, height // 2 - 50))
window.blit(final_score_text, (width // 2 - 100, height // 2))
pygame.display.flip()
pygame.time.delay(3000)

pygame.quit()
