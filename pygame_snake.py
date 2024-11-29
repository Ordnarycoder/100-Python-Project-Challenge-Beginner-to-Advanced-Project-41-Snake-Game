import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 720, 480
BLOCK_SIZE = 20
FPS = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

# Font for score
font = pygame.font.SysFont("arial", 25)

def display_score(score):
    """Display the score on the screen."""
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, [10, 10])

def game_over_message():
    """Display a game over message."""
    game_over_text = font.render("Game Over!", True, RED)
    restart_text = font.render("Press Q to Quit or R to Restart", True, RED)
    # Position the lines on the screen
    screen.blit(game_over_text, [WIDTH / 2 - 70, HEIGHT / 2 - 40])
    screen.blit(restart_text, [WIDTH / 2 - 150, (HEIGHT / 2)])




def game_loop():
    # Initial variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    change_to = direction
    food_rect = pygame.Rect(
        random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
        random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE,
        BLOCK_SIZE,
        BLOCK_SIZE
    )
    score = 0
    fps = FPS  # Initial FPS

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # If the direction is valid, update it
        direction = change_to

        # Update the snake's position
        if direction == 'UP':
            snake_pos[1] -= BLOCK_SIZE
        if direction == 'DOWN':
            snake_pos[1] += BLOCK_SIZE
        if direction == 'LEFT':
            snake_pos[0] -= BLOCK_SIZE
        if direction == 'RIGHT':
            snake_pos[0] += BLOCK_SIZE

        # Snake growing mechanism
        head_rect = pygame.Rect(snake_pos[0], snake_pos[1], BLOCK_SIZE, BLOCK_SIZE)

        # Check for food collision
        if head_rect.colliderect(food_rect):
            score += 1
            snake_body.insert(0, list(snake_pos))  # Grow the snake
            # Spawn new food
            food_rect = pygame.Rect(
                random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE
            )
            # Increase the speed
            fps += 1
        else:
            # Move the snake by removing the tail
            snake_body.pop()
            snake_body.insert(0, list(snake_pos))

        # Game over conditions
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            running = False
        for block in snake_body[1:]:
            if snake_pos == block:
                running = False

        # Draw everything
        screen.fill(BLACK)
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, food_rect)  # Draw the food

        # Display the score
        display_score(score)

        # Update the display
        pygame.display.update()

        # Control the game speed
        clock.tick(fps)  # Dynamically updated speed

    # Game over screen
    while not running:
        screen.fill(BLACK)
        game_over_message()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quit
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:  # Restart
                    game_loop()

    # Initial variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = 'RIGHT'
    change_to = direction
    food_rect = pygame.Rect(
        random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
        random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE,
        BLOCK_SIZE,
        BLOCK_SIZE
    )
    score = 0

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # If the direction is valid, update it
        direction = change_to

        # Update the snake's position
        if direction == 'UP':
            snake_pos[1] -= BLOCK_SIZE
        if direction == 'DOWN':
            snake_pos[1] += BLOCK_SIZE
        if direction == 'LEFT':
            snake_pos[0] -= BLOCK_SIZE
        if direction == 'RIGHT':
            snake_pos[0] += BLOCK_SIZE

        # Snake growing mechanism
        # Create the snake's head as a rectangle
        head_rect = pygame.Rect(snake_pos[0], snake_pos[1], BLOCK_SIZE, BLOCK_SIZE)

        # Check for food collision
        if head_rect.colliderect(food_rect):
            score += 1
            snake_body.insert(0, list(snake_pos))  # Grow the snake
            # Spawn new food
            food_rect = pygame.Rect(
                random.randrange(1, WIDTH // BLOCK_SIZE) * BLOCK_SIZE,
                random.randrange(1, HEIGHT // BLOCK_SIZE) * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE
            )
        else:
            # Move the snake by removing the tail
            snake_body.pop()
            snake_body.insert(0, list(snake_pos))

        # Game over conditions
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            running = False
        for block in snake_body[1:]:
            if snake_pos == block:
                running = False

        # Draw everything
        screen.fill(BLACK)
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, food_rect)  # Draw the food

        # Display the score
        display_score(score)

        # Update the display
        pygame.display.update()

        # Control the game speed
        clock.tick(FPS)

    # Game over screen
    while not running:
        screen.fill(BLACK)
        game_over_message()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quit
                    pygame.quit()
                    quit()
                if event.key == pygame.K_r:  # Restart
                    game_loop()

# Start the game
game_loop()
