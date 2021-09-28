# Lab_03_3.py
# Бойків Андрій
# Лабораторна робота № 3.3
# Розгалуження, задане графіком функції.
# Варіант 2

from math import *

R = int(input("Enter value of R: ")) # Вхідний параметр
x = int(input("Enter value of x: ")) # Вхідний аргумент
y = None # Результат обчислення

# Розгалуження в повній формі:

if x <= -8:
    y = -R
elif -8 < x and x <= -R:
    y = (x + 8)*R/(-R + 8) - R
elif -R < x and x <= R:
    y = -sqrt(R**2 + x**2)
elif R < x and x <= 5:
    y = (x - R)*2/(5 - R)
elif 5 < x:
    y = 3

print("y = ", y)