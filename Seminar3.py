# Задача 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень

# list_year = ["Зима", "Весна", "Лето", "Осень"]
# a = int(input("Введите номер месяца: "))
# if a == 12 or a == 1 or a == 2:
#     print(f"Результат через список: {list_year[0]}")
# elif a == 3 or a == 4 or a == 5:
#     print(f"Результат через список: {list_year[1]}")
# elif a == 6 or a == 7 or a == 8:
#     print(f"Результат через список: {list_year[2]}")
# elif a == 9 or a == 10 or a == 11:
#     print(f"Результат через список: {list_year[3]}")
# else:
#     print("Нет такого месяца в году")

# season_dict = {12:"Зима", 1:"Зима", 2:"Зима", 3:"Весна", 4:"Весна", 5:"Весна", 6:"Лето", 7:"Лето", 8:"Лето", 9:"Осень", 9:"Осень", 10:"Осень", 11:"Осень"}
# print(f"Результат через словарь: {season_dict.get(a)}")

# Задача 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).
# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!
# Process finished with exit code 0
# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0
# Process finished with exit code 0

# def calc_division(x, y):
#     a = x / y
#     return a
# try:
#     x = int(input("Введите число делимое: "))
#     y = int(input("Введите число делитель: "))
#     x / y
# except ValueError:
#     print("Формат ввода не соответствует")
# except ZeroDivisionError:
#     print("На нуль делить нельзя!!!")
# else:
#     print(calc_division(x, y))


# Задача 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456

# def passport_data(**kwargs):
#     return kwargs

# print(passport_data(name = input("Ваше имя: "), surname = input("Введите Вашу фамилию: " ), \
#             data_birth = input("Ваш год рождения; "),\
#             place = input("Город в котором Вы живете: "), emale = input("Ваша электронная почта: "), \
#             tel = input("Телефон: ")))

# def passport_data(name, surname, data_birth, place, email, tel):
#     print(f"{surname} {name}, {data_birth} года рождения, проживает в городе {place}, электронная почта: {email}, 
# телефон: {tel}")

# passport_data(name = input("Ваше имя: "), surname = input("Введите Вашу фамилию: " ), data_birth = input("Ваш год рождения: "),\
# place = input("Город в котором Вы живете: "), email = input("Ваша электронная почта: "), tel = input("Телефон: "))


# 
# Задача 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()

# def my_func(x, y, z):
#     list_1 = [x, y, z]
#     list_2 = (sorted(list_1))
#     s = (list_2[1] + list_2[2])
#     return s
    
    
# try:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     c = int(input("Введите третье число: "))
# except ValueError:
#     print("Формат ввода не соответствует")
# else:
#     print(my_func(a, b, c))

# def my_func(x, y, z):
#     list_1 = [x, y, z]
#     if x < y and x < z:
#         s = y + z 
#     elif y < x and y < z:
#         s = x + z
#     else:
#         s = x + y
#     return s
    
    
# try:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     c = int(input("Введите третье число: "))
# except ValueError:
#     print("Формат ввода не соответствует")
# else:
#     print(my_func(a, b, c))

# def my_func(x, y, z):
#     list_1 = [x, y, z]
#     s = x + y + z - min(list_1)
#     return s
    
    
# try:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
#     c = int(input("Введите третье число: "))
# except ValueError:
#     print("Формат ввода не соответствует")
# else:
#     print(my_func(a, b, c))

# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1


# n = int(input("Введите  положительное, целое число: "))
# list_1 = [i for i in range(1, n + 1)]
# print(list_1)

# d = int(input("Введите искомое число: "))
# count = 0
# for i in list_1:
#     if (list_1[i - 1]) == d:
#         count += 1
# print(f"выбранное число встресается {count} раз")

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите  положительное, целое число: "))
list_1 = [i for i in range(1, n + 1)]
print(list_1)

d = (int(input("Введите искомое число: ")))
list_2 = []
for i in range(n):
    
    list_2.append(abs(1 - d / list_1[i]))
#print(list_2)
#print(min(list_2))
x = list_2.index(min(list_2))
print(f"Наиболее близкое число {list_1[x]}")




# m = min(abs(d - list_2[i]))
# print(f"наиболее близкое число {m} ")
