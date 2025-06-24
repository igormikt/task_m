import pygame
import sys
import random
from pathlib import Path
import warnings

# Глобальное подавление предупреждения pkg_resources
warnings.filterwarnings("ignore", category=UserWarning,
                        message="pkg_resources is deprecated as an API")

# Инициализация Pygame
try:
    pygame.init()
    pygame.mixer.init()
except pygame.error as pygame_err:
    print(f"Ошибка инициализации Pygame: {pygame_err}")
    sys.exit(1)

# Настройки окна
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Загрузка шрифта
try:
    game_font = pygame.font.Font(None, 74)  # Используем другое имя переменной
except pygame.error as font_err:
    print(f"Ошибка загрузки шрифта: {font_err}")
    game_font = pygame.font.SysFont("arial", 74)


# Загрузка звука
def load_sound_file(filename):
    """Безопасная загрузка звука с уникальным именем параметра"""
    try:
        sound_path = Path(__file__).parent / filename
        if sound_path.exists():
            return pygame.mixer.Sound(sound_path)
        return None
    except (pygame.error, OSError) as sound_err:  # Уникальное имя переменной
        print(f"Ошибка загрузки звука {filename}: {sound_err}")
        return None


hit_effect = load_sound_file("hit.wav")  # Уникальное имя переменной


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)


class Player(Paddle):
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed


class Opponent(Paddle):
    def auto_move(self, ball_rect):
        if self.rect.centery < ball_rect.centery - 20:
            self.rect.y += self.speed
        elif self.rect.centery > ball_rect.centery + 20:
            self.rect.y -= self.speed


class Ball:
    def __init__(self, x, y, radius):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.radius = radius
        self.speed_x = 0
        self.speed_y = 0
        self.reset()

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = 4 * random.choice((1, -1))

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y
            if hit_effect:
                hit_effect.play()

    def check_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.speed_x = -self.speed_x * 1.05
            self.speed_y += random.uniform(-1, 1)
            if hit_effect:
                hit_effect.play()

    def draw(self):
        pygame.draw.circle(screen, WHITE, self.rect.center, self.radius)


# Основная функция игры
def main():
    # Создаем объекты
    player = Player(30, SCREEN_HEIGHT // 2 - 50, 15, 100, 5)
    opponent = Opponent(SCREEN_WIDTH - 45, SCREEN_HEIGHT // 2 - 50, 15, 100, 5)
    game_ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10)

    # Счет
    player_score = 0
    opponent_score = 0

    # Игровой цикл
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        player.move()
        opponent.auto_move(game_ball.rect)
        game_ball.move()
        game_ball.check_collision(player)
        game_ball.check_collision(opponent)

        # Голы
        if game_ball.rect.left <= 0:
            opponent_score += 1
            game_ball.reset()
        elif game_ball.rect.right >= SCREEN_WIDTH:
            player_score += 1
            game_ball.reset()

        # Отрисовка
        screen.fill(BLACK)
        pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

        player.draw()
        opponent.draw()
        game_ball.draw()

        # Счет
        score_text = game_font.render(f"{player_score} : {opponent_score}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()