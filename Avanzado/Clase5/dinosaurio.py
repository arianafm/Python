#pip3 install pygame --user

#adriana.proteco@gmail.com

#Dinosaurio de google con pygame
import pygame
from time import sleep

#Inicializamos pygame
pygame.init()

altoVentana=228
anchoVentana=510


#Creamos nuestra ventana
ventana =pygame.display.set_mode((anchoVentana,altoVentana))
pygame.display.set_caption("Mi primer juego con pygame.")
reloj = pygame.time.Clock() #Creamos un objeto Clock que tiene sus propios métodos.

#Guardamos en la variable fondo nuestra imagen del desierto
fondo= pygame.image.load('Sprites/desierto.png')

#Declaramos características de dinosaurio: coordenadas (x, y), ancho, alto y velocidad
spritesDino = [pygame.image.load("Sprites/d1.png"),pygame.image.load("Sprites/d2.png"),pygame.image.load("Sprites/d3.png"),pygame.image.load("Sprites/d4.png")]

gameOver = pygame.image.load("Sprites/game_over.png")

x= 0
y= 158
#anchoDinosaurio=40
#altoDinosaurio=60
#Ahora debemos pasarle el tamaño en pixeles de nuestra imagen.
anchoDinosaurio=44
altoDinosaurio=53
velocidad= 5

#Cactus
cactus = pygame.image.load("Sprites/cactus.png") #Variable que tendrá nuestro cactus. (Declaramos cactus)
xCactus = 325 #Estará mucho más adelante en la pantalla-
yCactus = 160
anchoCactus = 25 
altoCactus = 48


#Variable juegoCorriendo que es verdadero mientras estamos jugando
juegoCorriendo= True
#Variable que nos dice si está saltando o no el dinosaurio
estadoSaltando=False
contadorSalto = 10
contadorPasos = 0 #El contador está en 0 porqué empezará a iterar nuestra lista.

ventana.blit(fondo,(0,0)) #Dibujamos el fondo de la ventana

#Mientras sea verdadero juegoCorriendo
while juegoCorriendo:
	reloj.tick(12) #El 4 viene de los Sprites que tenemos en nuestro dinosaurio.
					#El 12 es para pasarle 3 veces la misma imagen
	#pygame.time.delay(50) #Esta línea es temporal luego declararemos un reloj de pygame
	for evento in pygame.event.get(): #recibimos uno por uno los eventos(interacciones con usuario)
		if evento.type == pygame.QUIT: #Si el evento es QUIT (presionar X de ventana)
			juegoCorriendo=False #El juego ya no está corriendo 

	teclas = pygame.key.get_pressed() #Aquí se guardarán las teclas que vayamos presionando

	if teclas[pygame.K_LEFT] and x>velocidad: #x>velocidad sirve para delimitar movimiento del dinosaurio a la ventana
		x= x-velocidad #Para moverlo cambios su coordenada x
		#x-=velocidad
	if teclas[pygame.K_RIGHT] and x<(anchoVentana-anchoDinosaurio):
		x= x+velocidad
	if teclas[pygame.K_SPACE]:
		estadoSaltando=True
	if estadoSaltando == True:
		if contadorSalto >= -10: #Cuando y es un valor negativo, sube.
			aux = 1
			if contadorSalto < 0:
				aux = -1
			y -= (contadorSalto**2) * aux*.35#Los dos ** corresponden a elevar.
			contadorSalto -= 1
		else:
			estadoSaltando = False
			contadorSalto = 10
		contadorPasos += 1
	if contadorPasos >=4:
		contadorPasos = 0

	rectanguloDino = pygame.Rect(x,y,anchoDinosaurio,altoDinosaurio)
	rectanguloCactus = pygame.Rect(xCactus,yCactus,anchoCactus, altoCactus)

	if rectanguloDino.colliderect(rectanguloCactus):
		ventana.blit(gameOver,(50,50))
		#pygame.display.update()
		pygame.display.flip()#Es un tipo de update que hace refresh en la pantalla
		sleep(2)
		juegoCorriendo = False



	ventana.blit(fondo,(0,0)) #Dibujamos el fondo de la ventana	
	ventana.blit(spritesDino[contadorPasos],(x,y))
	#ventana.blit(spritesDino[contadorPasos//4],(x,y)) #La tupla (x,y) hace referencia a las coordenadas. #//División etnera entre 4. El // le quia todos los decimales a la división
	ventana.blit(cactus,(xCactus,yCactus))


	#pygame.draw.rect(ventana,(82,213,163),(x,y,anchoDinosaurio,altoDinosaurio)) #Dibujamos el dinosaurio (temporalmente un rectangulo)
	#(82,213,163) corresponde al color de nuestro rectangulo en código RGB
	pygame.display.update() #Para que se muestren lo que dibujamos debemos actualizar la pantalla

pygame.quit() #Cerramos pygame
