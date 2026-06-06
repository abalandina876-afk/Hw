import pygame
import random
import sys

# Ініціалізація pygame
pygame.init()

# Розміри вікна гри
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20

# Кольори
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Налаштування екрану
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Класична Змійка (До 67 очок)")
clock = pygame.time.Clock()

# Шрифти
font = pygame.font.SysFont("Arial", 25)
victory_font = pygame.font.SysFont("Arial", 70, bold=True)


def get_random_color():
    """Генерує випадковий яскравий колір для змії"""
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))


def generate_food():
    """Генерує випадкові координати для яблука, вирівняні по сітці"""
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    return [x, y]


def draw_text(text, font, color, surface, x, y, center=False):
    """Функція для малювання тексту на екрані"""
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = (x, y)
    else:
        text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def main():
    # Початкові налаштування гри
    snake = [[100, 100], [80, 100], [60, 100]]  # Тіло змії
    snake_color = get_random_color()  # Початковий колір

    direction = "RIGHT"
    change_to = direction

    score = 0
    game_over = False
    victory = False

    # Створення першого яблука
    apple = generate_food()

    while True:
        # Обробка натискання клавіш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if direction != "DOWN":
                        change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if direction != "UP":
                        change_to = "DOWN"
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if direction != "RIGHT":
                        change_to = "LEFT"
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if direction != "LEFT":
                        change_to = "RIGHT"
                # Перезапуск гри на ПРОБІЛ після програшу або перемоги
                elif event.key == pygame.K_SPACE and (game_over or victory):
                    main()

        if not game_over and not victory:
            # Оновлюємо напрямок руху
            direction = change_to

            # Розрахунок нових координат голови змії
            head = list(snake[0])
            if direction == "UP":
                head[1] -= CELL_SIZE
            elif direction == "DOWN":
                head[1] += CELL_SIZE
            elif direction == "LEFT":
                head[0] -= CELL_SIZE
            elif direction == "RIGHT":
                head[0] += CELL_SIZE

            # Додаємо нову голову вперед
            snake.insert(0, head)

            # Перевірка: чи з'їла змія яблуко?
            if head == apple:
                score += 1
                snake_color = get_random_color()  # Новий колір при кожному поїданні
                apple = generate_food()
                # Перевірка, щоб яблуко не з'явилося всередині самої змії
                while apple in snake:
                    apple = generate_food()
            else:
                # Якщо яблуко не з'їли, видаляємо хвіст
                snake.pop()

            # Нова умова перемоги: рахунок 67
            if score >= 67:
                victory = True

            # Програш: врізалися в стінку
            if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
                game_over = True

            # Програш: врізалися в своє тіло
            if head in snake[1:]:
                game_over = True

        # --- Малювання на екрані ---
        screen.fill(BLACK)

        # Малюємо змію
        for segment in snake:
            pygame.draw.rect(screen, snake_color, pygame.Rect(segment[0], segment[1], CELL_SIZE - 2, CELL_SIZE - 2))

        # Малюємо червоне яблуко
        pygame.draw.rect(screen, RED, pygame.Rect(apple[0], apple[1], CELL_SIZE - 2, CELL_SIZE - 2))

        # Відображення поточного рахунку (тепер до 67)
        draw_text(f"Рахунок: {score}/67", font, WHITE, screen, 10, 10)

        # Екран перемоги (VICTORY зеленим кольором)
        if victory:
            draw_text("VICTORY", victory_font, GREEN, screen, WIDTH // 2, HEIGHT // 2, center=True)
            draw_text("Натисни ПРОБІЛ, щоб зіграти знову", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 60,
                      center=True)

        # Екран програшу
        if game_over:
            draw_text("ГРА ЗАКІНЧЕНА", victory_font, RED, screen, WIDTH // 2, HEIGHT // 2, center=True)
            draw_text("Натисни ПРОБІЛ, щоб спробувати ще раз", font, WHITE, screen, WIDTH // 2, HEIGHT // 2 + 60,
                      center=True)

        pygame.display.flip()

        # Швидкість гри
        clock.tick(10)


if __name__ == "__main__":
    main()