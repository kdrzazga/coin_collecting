import random
import pygame
import math

class Coin:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('resources/images/coin.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, screen.get_height() - self.rect.height)
        self.sound_effect = pygame.mixer.Sound('resources/sounds/effects/coin.mp3')

    def draw(self):
        self.screen.blit(self.image, self.rect)
    def check_collision(self, other_pos, other_radius):
        center = self.rect.x + self.rect.width // 2, self.rect.y + self.rect.width // 2
        distance = math.sqrt((center[0] - other_pos[0]) ** 2 + (center[1] - other_pos[1]) ** 2)
        coin_radius = self.rect.width // 2
        return distance < coin_radius + other_radius


