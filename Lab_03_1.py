# Lab_03_1.py
# Бойків Андрій
# Лабораторна робота № 3.1
# Розгалуження, задане формулою: функція однієї змінної.
# Варіант 2

from math import *

x = float(input("Enter value of x:\n")) # Вхідний параметр

A = 1/x + 4 # Проміжний результат - функціонально стала частина виразу
B = None # Проміжний результат - функціонально стала частина виразу

# Перший спосіб розгалуження (скорочена форма):

if x < 1:
    B = 0.65*x + 8
if 1 <= x and x < 5:
    B = atan((x + 6.1) / 2) + e**x
if x >= 5:
    B = sqrt(1 + sqrt(x))

y = A - B
print("1) y = ", y)

# Другий спосіб розгалуження (повна форма):

if x < 1:
    B = 0.65*x + 8
else:
    if x >= 5:
        B = sqrt(1 + sqrt(x))
    else:
        B = atan((x + 6.1) / 2) + e**x

y = A - B
print("2) y = ", y)