import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD

class ObstacleManager:
    def __init__(self):
        self.posibles = [SMALL_CACTUS, LARGE_CACTUS]
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(self.posibles[random.randint(0, 1)]))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                game.player = False

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)




            