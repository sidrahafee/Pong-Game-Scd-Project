import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 7

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Initialize paddles and ball
paddle1 = pygame.Rect(50, HEIGHT // 2 - 30, 20, 60)
paddle2 = pygame.Rect(WIDTH - 70, HEIGHT // 2 - 30, 20, 60)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_direction = [1, 1]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += PADDLE_SPEED

    # Move the ball
    ball.x += BALL_SPEED * ball_direction[0]
    ball.y += BALL_SPEED * ball_direction[1]

    # Check for collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_direction[1] = -ball_direction[1]

    # Check for collisions with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_direction[0] = -ball_direction[0]

    # Check for scoring
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_direction = [1, 1]
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
