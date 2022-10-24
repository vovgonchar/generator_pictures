from email import iterators
from re import X
from tkinter import Image
from PIL import Image, ImageDraw, ImageFont
import random
import string
import sys

##### Просим пользователя ввести значения #####
global_x = int(input("Введи ширину(кратные и больше 64): "))
if (global_x < 64) or (global_x % 64 != 0):
    print("Вы ввели некоректные значения. Программа остановлена.")
    sys.exit()
global_y = int(input("Введи длинну(кратные и больше 64): "))
if (global_y < 64) or (global_y % 64 != 0):
    print("Вы ввели некоректные значения. Программа остановлена.")
    sys.exit()
name = str(input("Введите слово для поиска: ")).upper()
iterations = int(input("Введите количество итераций: "))
if (iterations < 0):
    print("Вы ввели некоректные значения. Программа остановлена.")
    sys.exit()

# Список всех букв 
k = string.ascii_uppercase

# Создание исходного фона для букв
img = Image.new("RGB", (64,64) ,(34, 34, 34))

# Обозначиваем шрифт и размер
font = ImageFont.truetype('Fifaks10Dev1.ttf',size=50)

# Создаем объект текста
draw_text = ImageDraw.Draw(img)

# Цикл для генерация изображений всего алфавита
for item in k:
    img = Image.new("RGB", (64,64) ,(34, 34, 34)) # Создание фона для буквы
    draw_text = ImageDraw.Draw(img) # Создание объекта шрифта
    draw_text.text((22,8), f"{item}", font = font ,fill=(255,255,255)) # Наложение шрифта на фон
    img.save(f'letters/image_{item}.png') # Сохранение изображения

# Цикл для генерации букв для моего изображения
for item in name:
    img = Image.new("RGB", (64,64) ,(34, 34, 34)) # Создание фона для буквы
    draw_text = ImageDraw.Draw(img) # Создание объекта шрифта
    draw_text.text((22,8), f"{item}", font = font ,fill=(102,255,60)) # Наложение шрифта на фон
    img.save(f'letter_slovo/image_{item}.png') # Сохранение изображения

#####Генерация общей картины#####

#### Функция для генерации значений ####

def pasters(x, y):
    random_choise = random.choice(k)
    img = Image.open(f'letters/image_{random_choise}.png')
    background.paste(img, (cord_x,cord_y))
    count = 0
    
    if(x + 256 < global_x) and (random_choise == name[0]):    
        img = Image.open(f'letter_slovo/image_{random_choise}.png')
        background.paste(img, (cord_x,cord_y))
        for i in name:
            img = Image.open(f'letter_slovo/image_{i}.png')
            background.paste(img, (x , y))
            x += 64
            count += 1
        return(count * 64)
    else:
        return(64)

#######################################

#Генерация нашего изображения
for item in range(1, iterations+1):

    # Создание основного  фона
    background = Image.new("RGB", (global_x, global_y), (242,243,244))

    # Нулевая координата x
    cord_x = 0 

    # Нулевая координата y
    cord_y = 0

    while(cord_y <= global_y):
        while(cord_x < global_x):        
            cord_x += pasters(cord_x, cord_y)
            #print(f'y: {cord_y} | x: {cord_x}') # Отображение координат в консоль
        cord_x = 0
        cord_y += 64
    background.save(f"background{item}.png")