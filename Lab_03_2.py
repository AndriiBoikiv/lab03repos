# Lab_03_2.py
# Бойків Андрій
# Лабораторна робота № 3.2
# Розгалуження, задане формулою: функція з параметрами.
# Варіант 2

x = float(input("Enter value of x: ")) # Вхідний аргумент
a = float(input("Enter value of a: ")) # Вхідний параметр
b = float(input("Enter value of b: ")) # Вхідний параметр
c = float(input("Enter value of c: ")) # Вхідний параметр
F = None # Результат обчислення виразу

# Спосіб 1: розгалуження в скороченій формі

if x + 5 < 0 and c == 0:
    F = 1/(a*x) - b
if x + 5 > 0 and c != 0:
    F = (x - a)/x
if not (x + 5 < 0 and c == 0) and not (x + 5 > 0 and c != 0):
    F = 10*x/(c - 4)

print("1) F = ", F)

# Спосіб 2: розгалуження в повній формі

if x + 5 < 0 and c == 0:
    F = 1/(a*x) - b
elif x + 5 > 0 and c != 0:
    F = (x - a)/x
else:
    F = 10*x/(c - 4)

print("2) F = ", F)