# -*- coding: utf-8 -*-
"""
Created on Sun Dec 08 18:04:38 2013

@author: nnn
"""

import pygame,random,sys
from math import cos,sin

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 580
numAutos = 3
autosSpriteGroup= pygame.sprite.Group()
global simulando 
simulando = False
class auto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rotation = random.randint(0,360)
        self.image = pygame.transform.rotate(pygame.image.load("../sprites/"+str(random.randint(1,46))+".png").convert_alpha(),self.rotation)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = random.randint(0,600),random.randint(0,500)
        autosSpriteGroup.add(self)
        self.velocity = random.randint(1,10)
    def avanza(self):
        radians = (-1*self.rotation)*0.0174532925
        nx = 1.0*self.velocity*cos(radians)
        ny = 1.0*self.velocity*sin(radians)
        self.rect.left,self.rect.top = self.rect.left-nx,self.rect.top-ny
        collisions  =  pygame.sprite.spritecollide(self,autosSpriteGroup,0)
        if len(collisions)>1:
            for i in collisions:
                i.velocity =0
            
        """if self.velocity!=0:
            for i in  pygame.sprite.spritecollide(self,autosSpriteGroup,0):
                self.velocity = 0
                i.velocity=0"""
        
autos = [ ]
def repaint(screen):
    for i in autos:
        print i
        #screen.blit(i, (random.randint(0,500), random.randint(0,500)))
        screen.blit(i.image, i.rect())
    pygame.display.flip()
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulador")
    #autos = [ pygame.image.load("../sprites/"+str(random.randint(1,46))+".png").convert_alpha() for i in range(3) ]
    pygame.time.set_timer(pygame.USEREVENT+1, 10)
    autos = [ auto() for i in range(numAutos)]
    bol = True
    while bol:
        screen.fill((0,0,0))
        for i in autos:
            #screen.blit(i, (random.randint(0,500), random.randint(0,500)))
            #screen.blit(i.pygameImage,i.getPos())
            screen.blit(i.image,i.rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT+1 and simulando:
               for i in autos:
                   i.avanza()
            if event.type == pygame.QUIT:
                sys.exit()
                bol = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    global simulando
                    simulando =not simulando
                if event.key == 114:
                    autos = [ auto() for i in range(numAutos)]
                print event.key
                    
 
if __name__ == "__main__":
    main()