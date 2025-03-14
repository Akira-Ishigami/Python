import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Matrix Screensaver")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

font_size = 20  # Diminuído para permitir mais caracteres
font = pygame.font.Font(None, font_size)
akira_font_size = 200
akira_font = pygame.font.Font(None, akira_font_size)
name_font_size = 70
name_font = pygame.font.Font(None, name_font_size)

loading_font_size = 30
loading_font = pygame.font.Font(None, loading_font_size)

names_positions = [
    ("Luciano", (screen_width * 0.1, screen_height * 0.1)),
    ("Cristina", (screen_width * 0.9, screen_height * 0.1)),
    ("Eiko", (screen_width * 0.1, screen_height * 0.3)),
    ("Amanda", (screen_width * 0.9, screen_height * 0.3)),
    ("Ayumi", (screen_width * 0.1, screen_height * 0.5)),
    ("Magalhães", (screen_width * 0.9, screen_height * 0.5)),
    ("Ishigami", (screen_width * 0.5, screen_height * 0.7)),
    ("Taro", (screen_width * 0.5, screen_height * 0.3)),
    ("Yuki", (screen_width * 0.5, screen_height * 0.5)),
    ("Nori", (screen_width * 0.5, screen_height * 0.8)),
    ("Tokyo", (screen_width * 0.2, screen_height * 0.2)),
    ("New York", (screen_width * 0.8, screen_height * 0.2)),
    ("Paris", (screen_width * 0.2, screen_height * 0.4)),
    ("London", (screen_width * 0.8, screen_height * 0.4)),
    ("Sydney", (screen_width * 0.2, screen_height * 0.6)),
    ("Rio de Janeiro", (screen_width * 0.8, screen_height * 0.6)),
    ("São Paulo", (screen_width * 0.5, screen_height * 0.8)),
    ("California", (screen_width * 0.2, screen_height * 0.8)),
    ("Japan", (screen_width * 0.8, screen_height * 0.8)),
    ("Brazil", (screen_width * 0.5, screen_height * 0.4)),
    ("USA", (screen_width * 0.5, screen_height * 0.2)),
]

name_display_duration = 2

akira_interval = 10
akira_duration = 2

current_name_index = 0
name_display_start_time = time.time()
akira_start_time = None

num_columns = screen_width // font_size * 3  # Mais colunas para mais caracteres caindo
drops = [random.randint(-40, 0) for _ in range(num_columns)]  # Posições iniciais mais espaçadas
speeds = [random.randint(1, 2) for _ in range(num_columns)]  # Velocidade diminuída

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"

def random_green():
    return (0, random.randint(128, 255), 0)

def draw_matrix():
    screen.fill(BLACK)
    for i in range(num_columns):
        char = random.choice(characters)
        char_color = random_green()
        char_surface = font.render(char, True, char_color)
        x = i * font_size
        y = drops[i] * font_size
        screen.blit(char_surface, (x, y))
        drops[i] += speeds[i]
        if drops[i] * font_size > screen_height or random.random() > 0.98:
            drops[i] = random.randint(-40, 0)

def draw_names():
    global name_display_start_time, current_name_index
    current_time = time.time()
    name, position = names_positions[current_name_index]
    if current_time - name_display_start_time < name_display_duration:
        alpha = int(255 * (1 - (current_time - name_display_start_time) / name_display_duration))
        text_surface = pygame.Surface((name_font_size * len(name), name_font_size))
        text_surface.fill(BLACK)
        for i, char in enumerate(name):
            if random.random() < 0.1:
                char_surface = name_font.render(random.choice(characters), True, GREEN)
            else:
                char_surface = name_font.render(char, True, GREEN)
            char_rect = char_surface.get_rect(topleft=(i * (name_font_size // 2), 0))
            text_surface.blit(char_surface, char_rect)
        text_surface.set_alpha(alpha)
        text_rect = text_surface.get_rect(center=position)
        screen.blit(text_surface, text_rect)
    else:
        current_name_index = (current_name_index + 1) % len(names_positions)
        name_display_start_time = current_time

def draw_akira(alpha):
    text_surface = pygame.Surface((akira_font_size * 5, akira_font_size))
    text_surface.fill(BLACK)
    for i, char in enumerate("Akira"):
        if random.random() < 0.1:
            char_surface = akira_font.render(random.choice(characters), True, GREEN)
        else:
            char_surface = akira_font.render(char, True, GREEN)
        char_rect = char_surface.get_rect(topleft=(i * (akira_font_size // 2), 0))
        text_surface.blit(char_surface, char_rect)
    text_surface.set_alpha(alpha)
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text_surface, text_rect)

def draw_loading():
    loading_text = loading_font.render("Loading...", True, WHITE)
    loading_rect = loading_text.get_rect(bottomright=(screen_width - 20, screen_height - 20))
    screen.blit(loading_text, loading_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    draw_matrix()
    
    current_time = time.time()

    if akira_start_time is None or current_time - akira_start_time > akira_interval:
        akira_start_time = current_time

    if current_time - akira_start_time < akira_duration:
        alpha = int(255 * (1 - (current_time - akira_start_time) / akira_duration))
        draw_akira(alpha)
    else:
        draw_names()

    draw_loading()
    
    pygame.display.flip()
    pygame.time.delay(100)  # Atraso ajustado para diminuir a velocidade da queda

pygame.quit()
