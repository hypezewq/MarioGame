import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Главное меню Mario")

# Шрифты
font = pygame.font.SysFont('Arial', 50)
font_small = pygame.font.SysFont('Arial', 30)

# Тексты для кнопок
start_text = font.render("Начать игру", True, WHITE)
quit_text = font_small.render("Выйти из игры", True, WHITE)
background = pygame.image.load("super-mario-bros.jpg")
# Функция для отображения главного меню
def main_menu():
    running = True
    while running:
        screen.blit(background, (0, 0), area=pygame.Rect(0, 0, 800, 800))


        # Кнопка "Start Game"
        start_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, 250, 300, 70)
        pygame.draw.rect(screen, RED, start_button_rect)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 260))

        # Кнопка "Quit"
        quit_button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 150, 350, 300, 40)
        pygame.draw.rect(screen, RED, quit_button_rect)
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, 360))

        pygame.display.flip()

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    ...
                    # Здесь будет код для начала игры
                elif quit_button_rect.collidepoint(event.pos):
                    running = False

    pygame.quit()
    sys.exit()

# Запуск главного меню
if __name__ == "__main__":
    main_menu()
