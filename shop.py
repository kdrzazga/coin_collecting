import colors
import translator
import pygame

pygame.mixer.init()


class Shop:
    class Item:
        buying_sound_effect = pygame.mixer.Sound('resources/sounds/effects/buying.mp3')

        def __init__(self, name, price, description, icon_path):
            self.name: str = name
            self.price: int = price
            self.description: str = description
            self.icon_path = icon_path

        def __str__(self):
            return self.name

    def __init__(self, language):
        self.items = []
        self.language = language

    def add_item(self, item):
        self.items.append(item)

    def buy_item(self, item, money):
        if item in self.items and money >= item.price:
            money -= item.price
            self.items.remove(item)
            buying_sound_effect = pygame.mixer.Sound('resources/sounds/effects/buying.mp3')
            buying_sound_effect.play()
            return money

    def display_items(self, screen, font, language):
        text = font.render(translator.available_items[language], True, colors.white)
        screen.blit(text, (100, 75))
        for i, item in enumerate(self.items):
            text2 = font.render(f'{item.name}, {translator.price[self.language]}: {item.price} ({item.description})',
                                True, colors.white)
            icon = pygame.image.load(item.icon_path)
            screen.blit(icon, (50, 100 + i * 20))
            screen.blit(text2, (75, 105 + i * 20))
