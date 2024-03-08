import tkinter as tk
from tkinter import colorchooser
import random

def select_colors():
    # 색상 선택을 위한 함수
    colors = []
    for i in range(6):
        color = colorchooser.askcolor()[1]
        if color:
            colors.append(color)
    return colors

def generate_lotto_numbers(colors):
    # 색상값을 이용하여 로또 번호를 생성하는 함수
    lotto_numbers = []
    for color in colors:
        # RGB 값을 가져와서 합산
        r, g, b = int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16)
        # RGB 값의 합을 이용하여 번호 생성
        number = (r + g + b) % 45 + 1
        lotto_numbers.append(number)
    
    return sorted(lotto_numbers)

# 색상 선택 및 로또 번호 생성
colors = select_colors()
lotto_numbers = generate_lotto_numbers(colors)
print("생성된 로또 번호:", lotto_numbers)