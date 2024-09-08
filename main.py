import random

import pygame

import colors
import translator
from collectable import Collectable
from functions import *
from shop import Shop
from event import Event
from gift import Gift

christmas = Event('christmas', (12,), (21, 22, 23, 24, 25, 26, 27))
gift1 = None
if christmas.active():
    gift1 = Gift()

display_menu(['Polski', 'English', 'Русский', 'Español'])
choices_dict = {1: 'PL',
                2: 'EN',
                3: 'RU',
                4: 'ES'}
while True:
    try:
        choice = int(input('Choose the number of your language: '))
        if choice in choices_dict:
            lan = choices_dict[choice]
            break
        else:
            print('\nInvalid language\n')
    except ValueError:
        print("Please type in a number.")

# inicjalizacje
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)
screen_size = screen.get_size()
screen_center = (screen_size[0] / 2, screen_size[1] / 2)

coin1 = Collectable(screen)

shop = Shop(lan)
shop.add_item(Shop.Item(translator.yellow_skin[lan], 10, translator.yellow_skin_description[lan],
                        'resources/images/item_icons/yellow_skin.png'))
shop.add_item(Shop.Item(translator.more_stamina[lan], 15, translator.more_stamina_description[lan],
                        'resources/images/item_icons/more_stamina.png'))

# początkowe statystyki
coins = 0
player_color = colors.red

if gift1 is not None:
    coins += gift1.coins
    player_color = gift1.color

stamina: float = 100
max_stamina = 100
stamina_regeneration = 0.1

player_radius = 30

player_x, player_y = screen_center

pygame.display.set_caption(translator.game_name[lan])

font = pygame.font.SysFont(None, 24)


def update_coins_text():
    return font.render(f"{translator.coins[lan]}: {coins}", True, colors.white)


def update_stamina_text():
    return font.render(f'{translator.stamina[lan]}: {int(stamina)}', True, colors.white)


clock = pygame.time.Clock()

playing = True
resting = False
shop_checker = False


def check_boundaries():
    global player_x, player_y
    if player_x < 10:
        player_x = 10
    if player_x > screen_size[0] - 10:
        player_x = screen_size[0] - 10
    if player_y < 10:
        player_y = 10
    if player_y > screen_size[1]:
        player_y = screen_size[1]


def buy_yellow_color():
    global coins, player_color
    if shop.items[0].name == translator.yellow_skin[lan]:
        if coins >= 10:
            coins = shop.buy_item(shop.items[0], coins)
            player_color = colors.yellow


def buy_more_stamina(max_stamina_local):
    global coins
    if shop.items[0].name == translator.more_stamina[lan]:
        if coins >= 15:
            coins = shop.buy_item(shop.items[0], coins)
            max_stamina_local += 20
            if max_stamina_local <= 480:
                shop.add_item(
                    Shop.Item(translator.more_stamina[lan], 15, translator.more_stamina_description[lan],
                              'resources/images/item_icons/more_stamina.png'))
    elif shop.items[1].name == translator.more_stamina[lan]:
        if coins >= 15:
            coins = shop.buy_item(shop.items[1], coins)
            max_stamina_local += 20
            if max_stamina_local <= 480:
                shop.add_item(
                    Shop.Item(translator.more_stamina[lan], 15, translator.more_stamina_description[lan],
                              'resources/images/item_icons/more_stamina.png'))
            # przedmiot można kupić wiele razy jeżeli twoja maksymalna energia jest mniejsza niż 500
    return max_stamina_local


while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            playing = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            shop_checker = not shop_checker
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            buy_yellow_color()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            max_stamina = buy_more_stamina(max_stamina)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
            coins += 10  # do testowania

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and stamina > 0:
        speed = 10
        running = True
    else:
        speed = 5
    if not (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
        running = False
        resting = True

    if running:
        stamina -= 1
        resting = False
        if stamina < 0:
            stamina = 0
    else:
        if resting and stamina < max_stamina:
            stamina += stamina_regeneration
            resting = False

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= speed
        resting = False
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += speed
        resting = False
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= speed
        resting = False
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += speed
        resting = False

    check_boundaries()

    screen.fill(colors.black)

    coins_text_surface = update_coins_text()
    stamina_text_surface = update_stamina_text()
    screen.blit(coins_text_surface, (15, 10))
    screen.blit(stamina_text_surface, (screen_size[0] - 155, 20))

    coin1.draw()
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    if coin1.check_collision((player_x, player_y), player_radius):
        coins += 1
        coin1.rect.x = random.randint(0, screen.get_width() - coin1.image.get_width())
        coin1.rect.y = random.randint(0, screen.get_height() - coin1.image.get_height())
        coin1.sound_effect.play()
    if shop_checker:
        shop.display_items(screen, font, lan)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
