import pygame
import sys

# Инициализация Pygame
pygame.init()

# Основные параметры окна
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ФПС
clock = pygame.time.Clock()
FPS = 60


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)


class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Столкновение с верхом и низом
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -self.speed_y

    def check_collision(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.speed_x = -self.speed_x

    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.rect.centerx, self.rect.centery), self.radius)

    def reset(self):
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x *= -1  # Меняем направление после сброса


# Создание объектов
player = Paddle(30, SCREEN_HEIGHT // 2 - 50, 15, 100, 5)
opponent = Paddle(SCREEN_WIDTH - 45, SCREEN_HEIGHT // 2 - 50, 15, 100, 5)
ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 10, 4, 4)

# Счет
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение ракеток
    player.move(pygame.K_w, pygame.K_s)
    opponent.move(pygame.K_UP, pygame.K_DOWN)

    # Движение мяча
    ball.move()

    # Проверка столкновений
    ball.check_collision(player)
    ball.check_collision(opponent)

    # Проверка выхода мяча за границы
    if ball.rect.left <= 0:
        opponent_score += 1
        ball.reset()
    elif ball.rect.right >= SCREEN_WIDTH:
        player_score += 1
        ball.reset()

    # Отрисовка
    screen.fill(BLACK)

    # Рисование разделительной линии
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Рисование объектов
    player.draw()
    opponent.draw()
    ball.draw()

    # Отображение счета
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(opponent_text, (3 * SCREEN_WIDTH // 4, 20))

    # Обновление экрана
    pygame.display.flip()

    # Контроль ФПС
    clock.tick(FPS)

pygame.quit()
sys.exit()