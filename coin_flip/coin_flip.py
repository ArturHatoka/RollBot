import pyautogui
import time
import numpy as np
import imutils
import cv2
from imgcompare import is_equal, image_diff_percent

from PIL import Image, ImageChops
import os
import threading
from asyncio import Queue
import difflib
import matplotlib.pyplot as plt

from skimage import data
from skimage.feature import match_template

from . import coins_img
from . import game_matrix

pyautogui.hotkey('alt', 'tab')
coins_img = coins_img.get_coins_img()
game_matrix = game_matrix.get_game_matrix()
block_size = game_matrix['block']
game_matrix = game_matrix['matrix']

global coins
global prepend
global cur_coin
global cur_index
global first_index
global second_index


def click():
    pyautogui.mouseDown()
    time.sleep(0.03)
    pyautogui.mouseUp()


def start():
    global first_index, second_index, coins, prepend
    prepend = []
    coins = []
    first_index = 0
    second_index = 1
    while (first_index <= len(game_matrix)) & (second_index <= len(game_matrix)):
        time.sleep(0.5)
        go_click(game_matrix[first_index]['coord'], first_index, 'first')
        first_index += 2
        time.sleep(0.5)
        go_click(game_matrix[second_index]['coord'], second_index, 'second')
        second_index += 2
    else:
        print(coins)
        click()
        coins = []
        prepend = []
        print('exit')
        time.sleep(1)
        return True


def go_click(coord, index, times):
    global cur_index, coins

    pyautogui.moveTo(coord)
    click()
    click()
    pyautogui.moveTo(coord[0], coord[1] + 200)
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'tab')
    coin_name = search_coin(times)
    cur_index = index
    if coin_name:
        coins.append({'name': coin_name, 'id': index})
    print(coin_name)
    # print('id:' + str(index) + ' name:' + coin_name)


def get_img(coord):
    image = pyautogui.screenshot(
        region=(coord[0] - (block_size['width'] - (block_size['width'] / 10)) / 2,
                coord[1] - (block_size['height'] - (block_size['height'] / 10)) / 2,
                120, 120)
    )
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite('pic.png', image)


def get_img2(coord):
    image = pyautogui.screenshot(
        region=(coord[0] - 55, coord[1] - 50, 120, 120)
    )
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite('pic.png', image)


def search_coin(times):
    global cur_coin, coins
    k = 0
    z = 0
    ii = 0
    last_same = 100

    for coin in coins_img:
        coin_coord = pyautogui.locateCenterOnScreen(coin['path'], confidence=0.4)
        if coin_coord:

            get_img2(coin_coord)

            for cn in coins_img:
                is_same = image_diff_percent('pic.png', cn['path'])
                # print('name: ' + cn['name'] + ' ' + str(is_same))
                if is_same < last_same:
                    last_same = is_same
                    k = ii

                ii += 1
            break

    coin = coins_img[k]

    if times == 'first':
        prepend.append(coin)
        coins_img.pop(k)

    elif times == 'second':
        if len(prepend):
            coins_img.append(prepend[0])
        prepend.pop(0)
        pyautogui.hotkey('alt', 'tab')
        time.sleep(1)

    cur_coin = coin['name']
    if len(coins):
        check_coins(times)

    if (k == len(coins_img)) & len(prepend):
        pre = pyautogui.locateCenterOnScreen(prepend[0]['path'], confidence=0.8)
        if pre:
            coins_img.pop(k)
            prepend.pop(0)
            pyautogui.hotkey('alt', 'tab')
            time.sleep(1)
            return False

    print(times + ' cur_coin:' + coin['name'])
    return coin['name']

    # for coin in coins_img:
    #     coin_coord = pyautogui.locateCenterOnScreen(coin['path'], confidence=0.8)
    #     if coin_coord:
    #
    #         return
    #     # name = True
    #
    #     # coin = coins_img[k]
    #
    #     print(coin['name'])
    #
    #
    #     get_img2(coin_coord)
    #
    #     is_same = image_diff_percent('pic.png', coin['path'])
    #     if is_same < last_same:
    #         last_same = is_same
    #         k = ii
    #     ii += 1
    #
    #     if times == 'first':
    #         prepend.append(coin)
    #         coins_img.pop(k)
    #
    #     elif times == 'second':
    #         if len(prepend):
    #             coins_img.append(prepend[0])
    #         prepend.pop(0)
    #         pyautogui.hotkey('alt', 'tab')
    #         time.sleep(1)
    #
    #     cur_coin = coin['name']
    #     if len(coins):
    #         check_coins(times)
    #
    #     print(times + ' cur_coin:' + coin['name'])
    #     return coin['name']
    #
    # if (k == len(coins_img)) & len(prepend):
    #     pre = pyautogui.locateCenterOnScreen(prepend[0]['path'], confidence=0.8)
    #     if pre:
    #         coins_img.pop(k)
    #         prepend.pop(0)
    #         pyautogui.hotkey('alt', 'tab')
    #         time.sleep(1)
    #         return False


def check_coins(times):
    global coins, cur_coin

    n = 0
    while len(coins) > n:
        print(coins[n])
        if cur_coin == coins[n]['name']:
            if times == 'first':
                print('go after_first_click' + coins[n]['name'])
                after_first_click(coins[n]['id'])
            elif times == 'second':
                print('go after_second_click')
                after_second_click(coins[n]['id'])
        n += 1


def after_first_click(index):
    global first_index, second_index, coins
    time.sleep(0.4)
    pyautogui.moveTo(game_matrix[index]['coord'])
    click()
    click()
    time.sleep(0.9)

    # m = 0
    # while m < len(coins):
    #    if coins[m]['id'] == index:
    #        coins.pop(m)
    #   if coins[m]['id'] == cur_index+1:
    #       coins.pop(m)
    #   m += 1
    # first_index -= 1
    # second_index -= 1
    # if (first_index <= len(game_matrix)) & (second_index <= len(game_matrix)):
    #     time.sleep(0.5)
    #     click(game_matrix[first_index]['coord'], first_index, 'first')


def after_second_click(index):
    global cur_index, coins

    pyautogui.moveTo(game_matrix[cur_index + 1]['coord'])
    click()
    time.sleep(0.5)
    pyautogui.moveTo(game_matrix[index]['coord'])
    click()
    time.sleep(1)
    # m = 0
    # while m < len(coins):
    #    if coins[m]['id'] == index:
    #        coins.pop(m)
    #   if coins[m]['id'] == cur_index+1:
    #       coins.pop(m)
    #   m += 1
