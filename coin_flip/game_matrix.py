# from PIL import Image
import time

import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

matrixs = [
    {'name': '3x4', 'path': './coin_flip/matrix/matrix_3x4.png'},
    {'name': '4x4', 'path': './coin_flip/matrix/matrix_4x4.png'},
    {'name': '5x4', 'path': './coin_flip/matrix/matrix_5x4.png'},
]


def get_game_matrix():
    matrix = cur_matrix()
    matrix_center = matrix['matrix_center']
    matrix = matrix['matrix']
    print(matrix)
    print(matrix_center)
    matrix_size = get_matr_size(matrix)
    print(matrix_size)
    block_size = get_block_size(matrix, matrix_size)
    print(block_size)

    block_matrix = get_block_matrix(matrix, matrix_center, block_size)
    # print(block_matrix)
    return {'matrix': block_matrix, 'block': block_size}


def cur_matrix():
    matr = ''
    matr_coords = []
    for matrix in matrixs:
        get_matrix = pyautogui.locateCenterOnScreen(matrix['path'], confidence=0.9)
        if get_matrix:
            matr = matrix['name']
            matr_coords = get_matrix
    return {'matrix': matr, 'matrix_center': matr_coords}


def get_matr_size(matr):
    if matr == '3x4':
        return {
            'width': 472,
            'height': 657
        }
    elif matr == '4x4':
        return {
            'width': 637,
            'height': 657
        }
    elif matr == '5x4':
        return {
            'width': 814,
            'height': 657
        }


def get_block_size(matr, matr_size):
    if matr == '3x4':
        return {
            'width': matr_size['width'] / 3,
            'height': matr_size['height'] / 4
        }
    elif matr == '4x4':
        return {
            'width': matr_size['width'] / 4,
            'height': matr_size['height'] / 4
        }
    elif matr == '5x4':
        return {
            'width': matr_size['width'] / 5,
            'height': matr_size['height'] / 4
        }


def get_block_matrix(matrix, matrix_center, block_size):
    start_col = 0
    row = 0
    col = 0
    i = 10
    block_matrix = []
    start_block = []

    # pyautogui.moveTo(matrix_center)
    if matrix == '3x4':
        row = 4
        col = 3
        start_col = 3
        start_block = [
            matrix_center[0] - (block_size['width'] * 2),
            matrix_center[1] - (block_size['height'] + block_size['height'] / 2)
        ]
    elif matrix == '4x4':
        row = 4
        col = 4
        start_col = 4
        start_block = [
            matrix_center[0] - (block_size['width'] * 2 + block_size['width'] / 2),
            matrix_center[1] - (block_size['height'] + block_size['height'] / 2)
        ]
    elif matrix == '5x4':
        row = 4
        col = 5
        start_col = 5
        start_block = [
            matrix_center[0] - (block_size['width'] * 2 + block_size['width']),
            matrix_center[1] - (block_size['height'] + block_size['height'] / 2)
        ]
    # time.sleep(0.6)
    # pyautogui.moveTo(start_block)
    while row > 0:
        start_w = start_block[0]
        while col > 0:
            i += 1
            start_w += block_size['width']
            block_matrix.append({'id': i, 'coord': [start_w, start_block[1]]})
            col -= 1
        start_block[1] = start_block[1] + block_size['height']
        col = start_col
        row -= 1
        i += ((i % 10 - 10) // -1)

    return block_matrix
