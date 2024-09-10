import random

from colors import *


class Gift:
    def __init__(self):
        self.coins = 0
        self.color = red
        colors = (green, blue, magenta, yellow, cyan)

        prize = random.randint(1, 2)

        if prize <= 1:
            coins = random.randint(1, 5)
            print(f"Gift of {coins} coins.")
            self.coins = coins
        else:
            color_number = random.randint(0, len(colors) - 1)
            c = colors[color_number]
            print(f"Gift - new color {c}.")
            self.color = c
