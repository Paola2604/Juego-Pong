import pygame
from pygame.locals import *
import sys
import  detalles
import preguntar

# Constantes
WIDTH = 700
HEIGHT = 480
WHITE = (255, 255, 255)

# Clases
class Bola(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/ballFrance.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]

    def actualizar(self, time, pala_jug, pala_jug2, puntos):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time

        if self.rect.left <= 0:
            puntos[0] += 1
            self.reset_ball()
        if self.rect.right >= WIDTH:
            puntos[1] += 1
            self.reset_ball()

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed[1] = -self.speed[1]

        if pygame.sprite.collide_rect(self, pala_jug) or pygame.sprite.collide_rect(self, pala_jug2):
            self.speed[0] = -self.speed[0]
            
            
            
            

    def reset_ball(self):
        self.rect.centerx = WIDTH / 2
        self.rect.centery = HEIGHT / 2
        self.speed = [0.5, -0.5]

class Pala(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("imagenes/DIBU.png", transparent=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 0.5

    def mover(self, time, keys):
        if keys[K_q]:
            sys.exit(0)
        if self.rect.top >= 0 and keys[K_z]:
            self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT and keys[K_x]:
            self.rect.centery += self.speed * time
    def mover2(self, time, keys):
        if keys[K_q]:
            sys.exit(0)
        if self.rect.top >= 0 and keys[K_UP]:
            self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT and keys[K_DOWN]:
            self.rect.centery += self.speed * time


# Funciones
def load_image(filename, transparent=False):
    try:
        image = pygame.image.load(filename)
    except pygame.error:
        raise SystemExit
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, pygame.RLEACCEL)
    return image

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")
    
    # Cargar y redimensionar la imagen "CANCHA.png"
    background_image = load_image('imagenes/CANCHA.png')
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    
    bola = Bola()
    bola2 = Bola()
    bola3 = Bola()
    clock = pygame.time.Clock()
    pala_jug = Pala(30)
    pala_jug2 = Pala(665)
    puntos = [0, 0]
    cant_colision=0
    
    while True:
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                guardar_detalle(numero1,numero0)
                sys.exit(0)
                
        observacion =""
        
        if pygame.sprite.collide_rect(bola,pala_jug):
            observacion="(1,1)"
            cant_colision=cant_colision+1
            coordenada=(bola.rect.centerx),(bola.rect.centery)
            if(cant_colision==2):
                preguntar.guardarresp()
                numero1=int(numero1)
                puntos[1]=(det_puntos(numero1))
            detalle_colisiones(coordenada,observacion)
        elif(pygame.sprite.collide_rect(bola,pala_jug2)):
            observacion="(1,2)"
            coordenada=(bola.rect.centerx),(bola.rect.centery)
            detalle_colisiones(coordenada,observacion)
        if pygame.sprite.collide_rect(bola2,pala_jug):
            observacion="(2,1)"
            cant_colision=cant_colision+1
            coordenada=(bola2.rect.centerx),(bola.rect.centery)
            detalle_colisiones(coordenada,observacion)
        elif(pygame.sprite.collide_rect(bola2,pala_jug2)):
           observacion="(2,2)"
           coordenada=(bola2.rect.centerx),(bola.rect.centery)
           detalle_colisiones(coordenada,observacion)
        if pygame.sprite.collide_rect(bola3,pala_jug):
            observacion="(3,1)"
            coordenada=(bola3.rect.centerx),(bola.rect.centery)
            detalle_colisiones(coordenada,observacion)
        elif(pygame.sprite.collide_rect(bola3,pala_jug2)):
            observacion="(3,2)"
            coordenada=(bola3.rect.centerx),(bola.rect.centery)
            detalle_colisiones(coordenada,observacion)

              
        # Limpia la pantalla con el color de fondo
        screen.fill((0, 0, 0))  # Rellena con color negro (puedes ajustar el color)
        
        # Dibuja la imagen redimensionada en la pantalla
        screen.blit(background_image, (0, 0))
        
        bola.actualizar(-10, pala_jug, pala_jug2, puntos)
        bola2.actualizar(10, pala_jug, pala_jug2, puntos)
        bola3.actualizar(-time, pala_jug, pala_jug2, puntos)
        pala_jug.mover(time, keys)
        pala_jug2.mover2(time, keys)
        pala_jug2.mover2(time, keys)
        pala_jug2.mover2(time, keys)
        
        
        
        numero1= str(puntos[1])#SUMA PUNTOS
        numero0 = str(puntos[0])

  
        font = pygame.font.Font(None, 36)
        text1 = font.render("P_A: " + numero1, 1, WHITE)
        text2 = font.render("P_B: " + numero0, 1, WHITE)

        screen.blit(text1, (20, 0))
        screen.blit(text2, (560, 0))
        screen.blit(bola.image, bola.rect)
        screen.blit(bola2.image, bola2.rect)
        screen.blit(bola3.image, bola3.rect)
        screen.blit(pala_jug.image, pala_jug.rect)
        screen.blit(pala_jug2.image, pala_jug2.rect)
        

        
        
        
        pygame.display.flip()
   
def guardar_detalle(numero1,numero0):
    with open("archivos/compartir_usuario.txt","r",encoding="utf-8") as archivo_partida:
        linea=archivo_partida.readline()
        lista=linea.strip().split(",")
        if lista !="":
            cod=lista[0]
            partida=lista[1]
            fecha=lista[2]
    detalles.detalle(cod,partida,numero1,numero0,fecha)
    
def detalle_colisiones(coordenada,observacion):
        with open("archivos/compartir_usuario.txt","r",encoding="utf-8") as archivo_partida:
            linea=archivo_partida.readline()
            lista=linea.strip().split(",")
            if lista !="":
                cod=lista[0]
                partida=lista[1]
                fecha=lista[2]
        detalles.colisiones(cod,partida,fecha,coordenada,observacion)
    
def det_puntos(puntos):
    with open("archivos/maestro_pregunta.txt","r",encoding="utf-8") as archivo:
        linea=archivo.readline()
        if(linea!=""):
            lista=linea.strip().split(",")
            rta=lista[2]
            if(rta=="a"or rta=="A") or (rta=="c"or rta=="C"):
                puntos= puntos - 20
            elif(rta=="B"or rta=="b"):
                puntos= puntos + 50
            
    return puntos
            
    