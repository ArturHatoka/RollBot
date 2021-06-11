# from PIL import Image, ImageChops
#
#
# def difference_images():
#     image_1 = Image.open('pic.png')
#     image_2 = Image.open('./coin_flip/coins/riple.png')
#
#     result = ImageChops.difference(image_1, image_2).getbbox()
#
#     if result is None:
#         print(image_1, image_2, 'matches')
#     return
#
#
# difference_images()
from imgcompare import image_diff_percent

coins = [
        {'path': './coin_flip/coins/bit.jpg', 'name': 'btc'},
        {'path': './coin_flip/coins/bnb.jpg', 'name': 'bnb'},
        {'path': './coin_flip/coins/ether.jpg', 'name': 'eth'},
        {'path': './coin_flip/coins/lite.jpg', 'name': 'ltc'},
        {'path': './coin_flip/coins/monero.jpg', 'name': 'mnr'},
        {'path': './coin_flip/coins/riple.jpg', 'name': 'rpl'},
        {'path': './coin_flip/coins/rocket.jpg', 'name': 'rkt'},
        {'path': './coin_flip/coins/roll.jpg', 'name': 'rll'},
        {'path': './coin_flip/coins/teter.jpg', 'name': 'ttr'},
        {'path': './coin_flip/coins/usdt.jpg', 'name': 'usdt'},
]

for coin in coins:
    is_same = image_diff_percent('pic.png', coin['path'])

    print(is_same)