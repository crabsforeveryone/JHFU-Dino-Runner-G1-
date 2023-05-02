import random as rd
from dino_runner.components.obstacles.obstacles import Obstacle

class Cactus(Obstacle):
    def __init__(self, image):
        self.type = rd.randint(0, 2)
        self.image = image[self.type]
        super().__init__(image, self.type)
        self.rect.y = 330