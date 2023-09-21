import pygame
import random

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tulipanes version suyari')

# Clase para representar un tulipán
class Tulipan:
    def __init__(self, x, y):
        self.image = pygame.image.load("tulipan.png")  # Carga la imagen del tulipán
        self.image = pygame.transform.scale(self.image, (100, 100))  # Escala la imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, self.rect)

# Define las coordenadas para formar la letra "S"
s_coordinates = [
    #para la letra S
    (200, 300),(210, 300), (220, 300),  (230, 300),(240, 300), (250, 300),  (260, 300),(270, 300),(280, 300),   (290, 300),
    (200, 310),
    (200, 320),
    (200, 330),
    (200, 340),
    (200, 350),
    (200, 360), (210, 360), (220, 360), (230, 360), (240, 360), (250, 360), (260, 360), (270, 360), (280, 360), (290, 360),
    (290, 370),
    (290, 380),
    (290, 390),
    (290, 400),
    (290, 410),
    (290, 420),(210, 420), (220, 420), (230, 420), (240, 420), (250, 420), (260, 420), (270, 420), (280, 420), (290, 420),(200, 420),
      #para la letra U
    (350, 300),
    (350, 310),
    (350, 320),
    (350, 330),
    (350, 340),
    (350, 350),
    (350, 360),
    (350, 370),
    (350, 380),
    (350, 390),
    (350, 400),
    (350, 410),
    (350, 420),(360, 420),(370, 420),(380, 420),(390, 420),(400, 420),(410, 420),(420, 420),(430, 420),(440, 420),
    (440, 300),
    (440, 310),
    (440, 320),
    (440, 330),
    (440, 340),
    (440, 350),
    (440, 360),
    (440, 370),
    (440, 380),
    (440, 390),
    (440, 400),
    (440, 410),
]

# Lista de tulipanes formando la letra "S"
tulipanes = [Tulipan(x, y) for x, y in s_coordinates]

# Cargar la imagen del balón
ball = pygame.image.load("voley.png")
# Escalar la imagen del balón
ball = pygame.transform.scale(ball, (50, 50))
# Obtener el rectángulo que rodea al balón
ball_rect = ball.get_rect()
# Definir la velocidad inicial del balón en el eje x y el eje y
ball_speed_x = 7
ball_speed_y = -10

# Ángulo de rotación inicial
angle = 0

# Cargar una fuente de texto
font = pygame.font.Font(None, 24)  # Cambia "None" al nombre de una fuente si deseas usar una fuente específica

# Texto dividido en varias líneas
text_lines = [
    "Quiero recordarte lo fuerte y valiente que eres, Tu luz interior ",
    "brilla incluso en las sombras. No estás sola en esto :D"
   
]

# Renderizar las líneas de texto
text_surfaces = [font.render(line, True, (0, 0, 0)) for line in text_lines]

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Llenar la pantalla de blanco

    for tulipan in tulipanes:
        tulipan.draw()

    # Actualizar la posición del balón
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Rebotar en los bordes
    if ball_rect.left < 0 or ball_rect.right > width:
        ball_speed_x = -ball_speed_x
    if ball_rect.top < 0 or ball_rect.bottom > height:
        ball_speed_y = -ball_speed_y

    # Rotar el balón
    angle += 1  # Incrementa el ángulo de rotación
    ball_rotated = pygame.transform.rotate(ball, angle)
    ball_rect_rotated = ball_rotated.get_rect(center=ball_rect.center)

    # Dibujar el balón en la pantalla
    screen.blit(ball_rotated, ball_rect_rotated)
    
    y_position = 100  # Posición vertical inicial del texto
    for text_surface in text_surfaces:
        screen.blit(text_surface, (150, y_position))  # Cambia las coordenadas para ajustar la posición del texto
        y_position += text_surface.get_height() + 5  # Añadir un pequeño espacio entre líneas


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
