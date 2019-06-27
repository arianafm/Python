import pygame
import sys
from pygame.locals import *

#Ancho y alto de la ventana.
WIDHT = 640
HEIGHT = 480

def main():
	screen = pygame.display.set_mode((WIDHT,HEIGHT))
	#Nombre de la ventana.
	pygame.display.set_caption("Prueba pygame.")

	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT :
				sys.exit(0)

	return 0

#Para ver si estamos en el flujo principal.
if __name__ == '__main__':
	pygame.init() #Inicializalo antes de llamar al main.
	main()