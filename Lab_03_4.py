# Lab_03_4.py
# Бойків Андрій
# Лабораторна робота № 3.4
# Розгалуження, задане плоскою фігурою.
# Варіант 2

x = int(input("Enter value of x: ")) # Вхідний аргумент
y = int(input("Enter value of y: ")) # Вхідний параметр
R = int(input("Enter value of R: ")) # Вхідний параметр

# Розгалуження в повній формі:

if (x <= 0 and y >= 0 and x**2 + y**2 <= R) \
or (x >= 0 and y <= 0 and x <= R/2 and  y >= -x/2) \
or (x > R/2 and y <= 0 and x <= R and y >= 2*x - 2*R):
    print("yes")
else:
    print("no")