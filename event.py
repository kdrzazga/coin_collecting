from datetime import datetime
import pygame
import random


class Event:
    def __init__(self, name, months: tuple, days: tuple):
        self.months = months
        self.days = days
        self.name = name

    def __str__(self):
        return self.name

    def active(self):
        if datetime.now().month in self.months and datetime.now().day in self.days:
            return True
        else:
            return False


class Gift:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('resources/images/gift.png')
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, screen.get_height() - self.rect.height)
        self.prizes = ['2 coins', '3 coins', 'Custom color', 'random item']
