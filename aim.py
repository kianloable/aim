import pygame
import sys
import random
import time

# --- Settings ---
WIDTH, HEIGHT = 1650, 850
FPS = 120
TARGET_RADIUS = 25
SPAWN_DELAY = 0.1  # seconds before next target appears after hit

BG_COLOR = (30, 30, 30)
TARGET_COLOR = (200, 50, 50)
TEXT_COLOR = (240, 240, 240)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times New Roman", 28, bold=True)

score = 0
targets = []
last_spawn = time.time()

def spawn_target():
    x = random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS)
    y = random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)
    targets.append((x, y))

spawn_target()

running = True
while running:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos
            for t in targets[:]:
                tx, ty = t
                if (mx - tx)**2 + (my - ty)**2 <= TARGET_RADIUS**2:
                    targets.remove(t)
                    score += 1
                    last_spawn = time.time()

    # spawn new target if none present for a while
    if len(targets) == 0 and time.time() - last_spawn >= SPAWN_DELAY:
        spawn_target()

    screen.fill(BG_COLOR)

    # draw target(s)
    for tx, ty in targets:
        pygame.draw.circle(screen, TARGET_COLOR, (tx, ty), TARGET_RADIUS)

    # draw score
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()