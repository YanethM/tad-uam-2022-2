
from sre_constants import CATEGORY_NOT_LINEBREAK
from tkinter import messagebox, ttk
import tkinter as tk
import pygame
# Inicializar el modulo de pygame
pygame.init()

# Crear dimensiones del display
window_width = 700
window_height = 600
display_game = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Árboles binarios: YanethM")


def show_selection():
    # Obtener la opción seleccionada.
    selection = combo.get()
    messagebox.showinfo(
        message=f"La opción seleccionada es: {selection}",
        title="Selección"
    )


combo = ttk.Combobox(state="readonly",
                     values=["Python", "C", "C++", "Java"])
combo.place(x=50, y=50)
button = ttk.Button(text="Mostrar selección", command=show_selection)
button.place(x=50, y=100)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 243, 0)
CYAN = (0, 240, 255)
MAGENTA = (255, 0, 151)

# Variable que permitira mantener el display visible
display_game.fill(WHITE)
pygame.draw.circle(display_game,  BLUE, (350, 100), 30)  # Raíz
pygame.draw.circle(display_game,  BLUE, (500, 200), 30)
pygame.draw.circle(display_game,  BLUE, (200, 200), 30)
pygame.draw.circle(display_game,  BLUE, (250, 300), 30)
pygame.draw.circle(display_game,  BLUE, (100, 300), 30)
pygame.draw.circle(display_game,  BLUE, (450, 300), 30)
pygame.draw.circle(display_game,  BLUE, (600, 300), 30)
pygame.draw.circle(display_game,  BLUE, (50, 400), 25)
pygame.draw.circle(display_game,  BLUE, (150, 400), 25)
pygame.draw.circle(display_game,  BLUE, (250, 400), 25)
pygame.draw.circle(display_game,  BLUE, (350, 400), 25)
pygame.draw.circle(display_game,  BLUE, (450, 400), 25)
pygame.draw.circle(display_game,  BLUE, (550, 400), 25)
pygame.draw.circle(display_game,  BLUE, (650, 400), 25)
pygame.draw.circle(display_game,  BLACK, (200, 500), 20)
pygame.draw.circle(display_game,  BLACK, (250, 500), 20)
pygame.draw.circle(display_game,  BLACK, (300, 500), 20)
pygame.draw.circle(display_game,  BLACK, (500, 500), 20)

pygame.draw.line(display_game, BLACK, (350, 100), (500, 200))
pygame.draw.line(display_game, BLACK, (350, 100), (200, 200))
pygame.draw.line(display_game, BLACK, (200, 200), (50, 400))
pygame.draw.line(display_game, BLACK, (200, 200), (150, 300))

fonts = pygame.font.get_fonts()
for font in fonts:
    print(font)

system_font = pygame.font.SysFont('Calibri', 20)
system_text = system_font.render('Reto árboles', True, BLUE, WHITE)
system_text_rect = system_text.get_rect()
system_text_rect.center = (250, 50)


running = True

while(running):
    # La pantalla será visible en todo momento

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display_game.blit(system_text, system_text_rect)
    pygame.display.update()
pygame.mainloop()
pygame.quit()
