import pygame
#Punto de referencia del objeto en pygame es arriba a la izquierda. (0,0)

pygame.init()

altoVentana = 228
anchoVentana = 510

ventana = pygame.display.set_mode((anchoVentana,altoVentana))
fondo = pygame.image.load('Sprites/desierto.png')

#Coordenadas para el objeto:
x = 0
y = 158
anchoDinosaurio = 40
altoDiosaurio = 60

velocidad = 5

estadoSaltando = False

juegocorriendo = True

while juegocorriendo:
	pygame.time.delay(50)
	#Es como si fuese un listener.
	#Está atento a la interacción con el usuario.
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			juegocorriendo = False

	teclas = pygame.key.get_pressed() #Cuando una tecla sea presionada se guardará en teclas


	if teclas[pygame.K_LEFT] and x > (velocidad): #Cuando presiones esa tecla, haz una acción
		#Cambiaremos de posición por lo que cambiaremos su valor en x:
		x = x - velocidad
		#x -= velocidad

	if teclas[pygame.K_RIGHT] and x < (anchoVentana - anchoDinosaurio):
		x = x + velocidad

	if teclas[pygame.K_SPACE]:
		estadoSaltando = True

		
	ventana.blit(fondo,(0,0)) #Fondo, coordenadas.
	pygame.draw.rect(ventana,(82,213,163),(x,y,anchoDinosaurio,altoDiosaurio))
	pygame.display.update()

pygame.quit()


		