import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING
#las clases que van a ser visibles son sprites de la clase sprite


JUMP_VELOCITY = 8.5
DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"
POS_X = 80
POS_Y = 310
class Dinosaur(Sprite):

    
    #las clases visibles deben tener al menos tres metodos en general; draw, update y ¿eventes?
    def __init__(self):

        #representacion del dino
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = POS_X
        self.rect.y = POS_Y

        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = 8.5
    
    def update(self, user_input): 
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.rect.y = 345
            self.duck()
            
        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP] and self.action != DINO_JUMPING:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN] and self.action != DINO_JUMPING:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING    
        
        if self.step >= 10:
            self.step = 0

        
    def jump(self):
        self.image = JUMPING
        self.rect.y = -self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -JUMP_VELOCITY:
            self.rect.y = 310
            self.action = DINO_RUNNING
            self.jump_velocity = JUMP_VELOCITY
    def run(self):
            self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
            self.step += 1
            self.rect.y = POS_Y

    def duck(self):
        self.image = DUCKING[0] if self.step < 5 else DUCKING[1]
        self.step += 1


    def draw(self, screen):
        #blit recibe la posicion para dibujar y la imagen
        screen.blit(self.image, (self.rect.x, self.rect.y))

