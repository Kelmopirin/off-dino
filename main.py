import random

import pygame

from AIDino import AIDino
from obstacles import ObstacleCourse


WIDTH, HEIGHT = 800, 600
POPULATION_SIZE = 10
HEADER_HEIGHT = 40
LANE_HEIGHT = (HEIGHT - HEADER_HEIGHT) / POPULATION_SIZE
DINO_SCALE = 0.5
CACTUS_SCALE = 0.42


def create_population(previous_population=None):
    population = [
        AIDino(
            x=140,
            ground_y=round(HEADER_HEIGHT + index * LANE_HEIGHT + 5),
            scale=DINO_SCALE,
        )
        for index in range(POPULATION_SIZE)
    ]

    if previous_population is None:
        return population

    ranked = sorted(previous_population, key=lambda dino: dino.fitness, reverse=True)
    parents = ranked[: max(2, POPULATION_SIZE // 3)]
    population[0].nn = ranked[0].nn.clone()

    for dino in population[1:]:
        parent_a, parent_b = random.sample(parents, 2)
        dino.nn = parent_a.nn.crossover(parent_b.nn)

    return population


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dino - evolúciós neurális háló")
    font = pygame.font.Font(None, 24)
    small_font = pygame.font.Font(None, 18)
    clock = pygame.time.Clock()

    population = create_population()
    course = ObstacleCourse(WIDTH, DINO_SCALE, CACTUS_SCALE)
    generation = 1
    best_fitness = 0.0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(60)
        course.update(dt)
        for dino in population:
            dino.update(course.current, course.speed, dt, WIDTH)

        if not any(dino.alive for dino in population):
            best_fitness = max(best_fitness, max(dino.fitness for dino in population))
            population = create_population(population)
            course.reset()
            course.increase_speed(0.03)
            generation += 1

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (240, 240, 240), (0, 0, WIDTH, HEADER_HEIGHT))
        status = font.render(
            f"Generáció: {generation}   Élők: "
            f"{sum(dino.alive for dino in population)}/{POPULATION_SIZE}   "
            f"Legjobb túlélés: {best_fitness:.1f} s",
            True,
            (30, 30, 30),
        )
        screen.blit(status, (10, 11))

        for index, dino in enumerate(population):
            lane_top = HEADER_HEIGHT + index * LANE_HEIGHT
            ground_line_y = round(lane_top + LANE_HEIGHT - 3)
            pygame.draw.line(
                screen,
                (210, 210, 210),
                (0, ground_line_y),
                (WIDTH, ground_line_y),
                1,
            )
            label = small_font.render(
                f"{index + 1:02}  {dino.fitness:.1f}s",
                True,
                (40, 40, 40) if dino.alive else (150, 70, 70),
            )
            screen.blit(label, (8, round(lane_top + 3)))
            dino.dino.draw(screen, hitbox=True)
            course.current.draw(screen, hitbox=True, y=dino.dino.ground_y)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
