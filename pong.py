import pygame
import time
import random

#Definiciones globales
pygame.init()

dancho = 800
dalto = 600

black = (0,0,0)
white = (255,255,255)

jancho = 20
jalto = 50

pancho = 10
palto = 10

gameDisplay = pygame.display.set_mode((dancho,dalto))
pygame.display.set_caption('Me robe un Pong!')

reloj = pygame.time.Clock()

def text_objects(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def message_display(text,x,y):
    largetext = pygame.font.Font('freesansbold.ttf',40)
    TextSurf, TextRect = text_objects(text, largetext)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)

def game_loop():
    px = 395
    py = 295

    movpx = 5
    movpy = 5
    
    j1posx = 50
    j1posy = 50
    j2posx = 750
    j2posy = 50

    j1mov = 0
    j2mov = 0

    puntos1 = 0
    puntos2 = 0
    quien = ""


    #Aca va el juego
#PINTAR FONDO
    gameDisplay.fill(black)
#PINTAR Marco
    pygame.draw.rect(gameDisplay, white, [j1posx, j1posy, jancho, jalto])
    pygame.draw.rect(gameDisplay, white, [j2posx, j2posy, jancho, jalto])
    pygame.draw.rect(gameDisplay, white, [px, py, pancho, pancho])

    salir = False

    while not salir:

        pygame.draw.rect(gameDisplay, black, [j1posx, j1posy, jancho, jalto])
        pygame.draw.rect(gameDisplay, black, [j2posx, j2posy, jancho, jalto])
        pygame.draw.rect(gameDisplay, black, [px, py, pancho, pancho])
        #Tapar puntaje anterior
        pygame.draw.rect(gameDisplay, black, [120, 10, 50, 50])
        pygame.draw.rect(gameDisplay, black, [620, 10, 50, 50])



        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    pygame.quit()
                    quit()
                
                if event.key == pygame.K_DOWN:
                    j2mov = 15
#                    print("arrow down")
                elif event.key == pygame.K_UP:
                    j2mov = -15
#                    print("arrow up")
                
                if event.key == pygame.K_a:
                    j1mov = 15
#                    print("q down")
                elif event.key == pygame.K_q:
                    j1mov = -15
#                    print("a up")
                
#            if event.type == pygame.KEYUP:
#                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
#                    j2mov = 0
#                if event.key == pygame.K_q or event.key == pygame.K_a:
#                    j2mov = 0

        if ((px+pancho) >= j2posx):
            if (py >= j2posy) and (py <= (j2posy+jalto)):
                movpx = -5
            else:
                if (puntos1 < 5):
                    px = 395
                    py = 295
                    puntos1 += 1
                    time.sleep(1)
                else:
                    quien = "Jugador 1"
                    #print(quien)
                    salir = True

        if (px <= (j1posx+jancho)):
            if (py >= j1posy) and (py <= (j1posy+jalto)):
                movpx = 5
            else:
                if (puntos2 < 5):
                    px = 395
                    py = 295
                    puntos2 += 1
                    time.sleep(1)
                else:
                    quien = "Jugador 2"
                    #print(quien)
                    salir = True

        if (j2mov > 0):
            if (j2posy < 550 ):
                j2posy = j2posy + j2mov
        elif (j2mov < 0):
            if (j2posy > 50 ):
                j2posy = j2posy + j2mov

        if (j1mov > 0):
            if (j1posy < 550 ):
                j1posy = j1posy + j1mov
        elif (j1mov < 0):
            if (j1posy > 50 ):
                j1posy = j1posy + j1mov

        if (px < 780):
            px = px + movpx

        if (movpy > 0):
            if (py < 580):
                py = py + movpy
            else:
                movpy = -5
                py = py + movpy
        else:
            if (py > 20):
                py = py + movpy
            else:
                movpy = 5
                py = py + movpy
        
        #Puntaje1
        message_display(str(puntos1),150,40)
        #Puntaje 2
        message_display(str(puntos2),650,40)
        #Jugador1
        pygame.draw.rect(gameDisplay, white, [j1posx, j1posy, jancho, jalto])
        #Jugador2
        pygame.draw.rect(gameDisplay, white, [j2posx, j2posy, jancho, jalto])
        #LaPelota!
        pygame.draw.rect(gameDisplay, white, [px, py, pancho, pancho])


        pygame.display.update()
        reloj.tick(60)
    print("Salgo al return")
    return quien

def main():
    #Cuerpo del programa que llama al juego
    ganador = game_loop()
    #print("ganador")
    #print(ganador)
    mensaje = "El ganador fue: " + ganador 
    print(mensaje)
    gameDisplay.fill(black)
    message_display(mensaje,400,300)
    pygame.display.update()
    time.sleep(5)
    pygame.quit()
    quit()



if __name__ == "__main__":
    main()