import pygame
import sys

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_SPEED = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ping Pong')

# Define the ball and paddles
ball = pygame.Rect(SCREEN_WIDTH//2 - BALL_SIZE//2, SCREEN_HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
player_paddle = pygame.Rect(SCREEN_WIDTH - PADDLE_WIDTH, SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
computer_paddle = pygame.Rect(0, SCREEN_HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Player paddle follows mouse position
    mouse_y = pygame.mouse.get_pos()[1]
    player_paddle.y = mouse_y - PADDLE_HEIGHT//2
    
    # Ensure player paddle stays within screen bounds
    if player_paddle.top < 0:
        player_paddle.top = 0
    if player_paddle.bottom > SCREEN_HEIGHT:
        player_paddle.bottom = SCREEN_HEIGHT
    
    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y = -ball_speed_y
    
    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_speed_x = -ball_speed_x
    
    # Ball goes out of bounds (left or right)
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball.x = SCREEN_WIDTH//2 - BALL_SIZE//2
        ball.y = SCREEN_HEIGHT//2 - BALL_SIZE//2
        ball_speed_x = BALL_SPEED_X if ball_speed_x < 0 else -BALL_SPEED_X
    
    # Simple AI for computer paddle: follow the ball
    if ball.y < computer_paddle.centery:
        computer_paddle.y -= PADDLE_SPEED
    if ball.y > computer_paddle.centery:
        computer_paddle.y += PADDLE_SPEED
    
    # Ensure computer paddle stays within screen bounds
    if computer_paddle.top < 0:
        computer_paddle.top = 0
    if computer_paddle.bottom > SCREEN_HEIGHT:
        computer_paddle.bottom = SCREEN_HEIGHT
    
    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, computer_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)
