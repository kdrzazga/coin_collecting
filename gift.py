import random

from colors import *


class Gift:
    def __init__(self):
        self.coins = None
        self.color = None
        colors = (green, blue, magenta, yellow, cyan)

        r = random.randint(1, 2)

        if r <= 1:
            coins = random.randint(1, 5)
            print(f"Gift of {coins} coins.")
            self.initialize(red, coins)
        else:
            color_number = random.randint(0, len(colors))
            c = colors[color_number]
            print(f"Gift - new color {c}.")
            self.initialize(c, 0)

    def initialize(self, color, coins):
        self.color = color
        self.coins = coins
