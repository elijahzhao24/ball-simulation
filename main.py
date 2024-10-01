import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Bouncing Inside a Solid Circle with Gravity")

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set the center and radius of the solid circular boundary
CENTER = (WIDTH // 2, HEIGHT // 2)
CIRCLE_RADIUS = 200

# Define ball properties
ball_radius = 15
ball_color = RED
ball_pos = [random.randint(CENTER[0] - CIRCLE_RADIUS + ball_radius, CENTER[0] + CIRCLE_RADIUS - ball_radius), 
            random.randint(CENTER[1] - CIRCLE_RADIUS + ball_radius, CENTER[1] + CIRCLE_RADIUS - ball_radius)]
ball_vel = [random.choice([-4, 4]), random.choice([-2, 2])]  # Random initial velocity

# Gravity constant (affects the downward acceleration)
GRAVITY = 0.05

# Define clock to control frame rate
clock = pygame.time.Clock()

# Function to calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Function to handle ball collision with the solid circle boundary
def handle_collision():
    dist_from_center = distance(ball_pos, CENTER)

    # If the ball hits the inner boundary of the solid circle
    if dist_from_center + ball_radius >= CIRCLE_RADIUS:
        # Calculate the normal vector (from the center of the circle to the ball's position)
        normal_x = (ball_pos[0] - CENTER[0]) / dist_from_center
        normal_y = (ball_pos[1] - CENTER[1]) / dist_from_center

        # Reflect the velocity in the direction of the normal
        dot_product = ball_vel[0] * normal_x + ball_vel[1] * normal_y
        ball_vel[0] -= 2 * dot_product * normal_x
        ball_vel[1] -= 2 * dot_product * normal_y

        # Reposition the ball to be exactly on the boundary
        ball_pos[0] = CENTER[0] + normal_x * (CIRCLE_RADIUS - ball_radius)
        ball_pos[1] = CENTER[1] + normal_y * (CIRCLE_RADIUS - ball_radius)

        # Apply damping to simulate energy loss on bounce
        ball_vel[0] *= 0.9  # Horizontal velocity damping
        ball_vel[1] *= 0.9  # Vertical velocity damping

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw the solid circle (the boundary)
    pygame.draw.circle(screen, BLACK, CENTER, CIRCLE_RADIUS, 2)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Apply gravity (increase vertical velocity)
    ball_vel[1] += GRAVITY

    # Move the ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Check for collisions with the circular boundary
    handle_collision()

    # Check for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
