# Задача 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

# ниже три варианта

def my_func(x, y, z):
    list_1 = [x, y, z]
    list_2 = (sorted(list_1))
    s = (list_2[1] + list_2[2])
    return s


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
except ValueError:
    print("Формат ввода не соответствует")
else:
    print(my_func(a, b, c))

def my_func(x, y, z):
    list_1 = [x, y, z]
    if x < y and x < z:
        s = y + z 
    elif y < x and y < z:
        s = x + z
    else:
        s = x + y
    return s


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
except ValueError:
    print("Формат ввода не соответствует")
else:
    print(my_func(a, b, c))

def my_func(x, y, z):
    list_1 = [x, y, z]
    s = x + y + z - min(list_1)
    return s


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
except ValueError:
    print("Формат ввода не соответствует")
else:
    print(my_func(a, b, c))