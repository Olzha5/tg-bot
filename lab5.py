# . Тізімде қолданылатын кемінде 5 функциядарды қолданып,
# программа жазып шығу. Тізім ретінде əр студент өзінің
# резюмесін ұсынсын. Жəне сол тізіммен жұмыс жасасын.

# # Создание списка
# my_list = [1, 2, 3, 4, 5]

# # Функция len() - возвращает длину списка
# print(len(my_list))  # Вывод: 5

# # Функция append() - добавляет элемент в конец списка
# my_list.append(6)
# print(my_list)  # Вывод: [1, 2, 3, 4, 5, 6]

# # Функция insert() - добавляет элемент на определенную позицию списка
# my_list.insert(4, 7)
# print(my_list)  # Вывод: [1, 2, 7, 3, 4, 5, 6]

# # Функция pop() - удаляет и возвращает последний элемент списка
# last_element = my_list.pop()
# print(last_element)  # Вывод: 6
# print(my_list)  # Вывод: [1, 2, 7, 3, 4, 5]

# # Функция sort() - сортирует список по возрастанию
# my_list.sort()
# print(my_list)  # Вывод: [1, 2, 3, 4, 5, 7]






# 1. Əртүрлі топтардағы студенттерді əртүрлі пəндер бойынша секцияға
# қатысатын бағдарлама жазыңыз. Тізімді əртүрлі санаттарға байланысты
# сұрыптау қажет. Нəтижені экранда көрсетіңіз.
# Напишите программу, в которой предлагается вводить учащихся
# различных групп, посещающих секции по разным предметам. Требуется
# упорядочить список по различным категориям. Вывести результат на
# экран. 

# from itertools import groupby

# students = []

# # #заполнение
# while True:
#     student = {}
#     student['name'] = input('Введите имя учащегося (или "стоп" для завершения ввода): ')
#     if student['name'] == 'стоп':
#         break
#     student['group'] = input('Введите номер группы: ')
#     student['subject'] = input('Введите предмет, который посещает учащийся: ')
#     students.append(student)

# # сортировка 
# students.sort(students.sort(key=lambda x: x['name']))

# # вывод 
# for group, students_in_group in groupby(students, key=lambda x: x['group']):
#     print(f'Группа {group}:')
#     for student in students_in_group:
#         studentter=student.sort(reverse=True)
#         print(f'\t{student["name"]}, посещает {student["subject"]}')
#         print(f'\t{student["name"]}, посещает {student["subject"]}')



# 2. Тізім қайтаратын функция жазып шығу. Алдын ала студенттердің
# пəндері жəне бағалары бар тізім құрастыр. Жəне сол тізім бойынша
# студенттің атын еңгізген кезде, сол студенттің бағаларын шығарып
# бертін болсын.


# создаем словарь с предметами и оценками
# grades = {
#     'Олжас': {'математика': 4, 'физика': 5, 'химия': 3},
#     'Ералы': {'математика': 5, 'физика': 4, 'химия': 5},
#     'Диас': {'математика': 3, 'физика': 4, 'химия': 4},
# }

# # запрашиваем имя учащегося и выводим его оценки
# while True:
#     name = input('Введите имя учащегося (или "стоп" для завершения ввода): ')
#     if name == 'стоп':
#         break
#     if name in grades:
#         print(f'Оценки учащегося {name}:')
#         for subject, grade in grades[name].items():
#             print(f'{subject}: {grade}')
#     else:
#         print(f'Учащегося с именем {name} не найдено.')


# 3. Пайдаланушыға бүтін мəндерді сұрайтын жəне оларды тізім ретінде
# сақтайтын бағдарламаны жазыңыз. Мəндерді енгізудің аяқталуының
# көрсеткіші ретінде нөлді пайдалану керек. Содан кейін бағдарлама
# пайдаланушы енгізген барлық сандарды (нөлден басқа) өсу ретімен көрсетуі
# керек - əр жолға бір мəн. Сұрыптау үшін sort əдісін немесе sorted функцияны
# пайдаланыңыз.


# создаем пустой список
# numbers = []

# заполняем список числами, пока пользователь не введет 0
# while True:
#     num = int(input('Введите целое число (0 для завершения ввода): '))
#     if num == 0:
#         break
#     numbers.append(num)

# # сортируем список по возрастанию
# numbers.sort()

# # выводим список на экран
# for num in numbers:
#     print(num)


# 4. Алдыңғы жағдайдағыдай пайдаланушыдан бүтін сандарды сұрайтын
# жəне оларды тізім ретінде сақтайтын бағдарламаны жазыңыз. Нөл мəндерді
# енгізудің аяқталуының көрсеткіші ретінде де қызмет етуі керек. Бұл жолы
# енгізілген мəндерді кему ретімен көрсету қажет.

# запрос чисел у пользователя
# numbers = []
# while True:
#     num = int(input("Введите число (0 для завершения ввода): "))
#     if num == 0:
#         break
#     numbers.append(num)

# # сортировка и вывод на экран
# numbers.sort(reverse=True)
# print("Введенные числа в порядке убывания: ")
# for num in numbers:
#     print(num)


# 5. Бас жүлдені ұтып алу үшін лотерея билетіндегі алты нөмір келесі
# ұтыс ойынында 1-ден 49-ға дейінгі аралықта кездейсоқ алынған алты нөмірге
# сəйкес келуі керек. Билетіңізге алты санды кездейсоқ таңдайтын бағдарлама
# жазыңыз. Бұл сандар арасында көшірмелердің жоқтығына көз жеткізіңіз. 
# Экранда билет нөмірлерін өсу ретімен көрсетіңіз.


# import random

# # Генерируем 
# numbers = random.sample(range(1, 50), 6)

# # Сортируем числа по возрастанию
# numbers.sort()

# # Выводим числа на экран
# print("Номера билета:", numbers)



# 6. Оған параметр ретінде берілген тізім сұрыпталғанын (өсу немесе кему
# ретімен) көрсететін функцияны жазыңыз. Тізім сұрыпталған болса, функция
# True мəнін, ал кері жағдайда False мəнін қайтаруы керек. Негізгі
# бағдарламада пайдаланушыдан тізімге арналған сандар тізбегін сұраңыз, 
# содан кейін тізім бастапқыда сұрыпталғаны туралы хабарды көрсетіңіз.


# def is_sorted(lst):
#     """
#     Проверяет, отсортирован ли переданный список (по возрастанию или убыванию)
#     """
#     if all(lst[i] <= lst[i+1] for i in range(len(lst)-1)):
#         # Если каждый следующий элемент больше или равен предыдущему, то список отсортирован по возрастанию
#         return True
#     elif all(lst[i] >= lst[i+1] for i in range(len(lst)-1)):
#         # Если каждый следующий элемент меньше или равен предыдущему, то список отсортирован по убыванию
#         return True
#     else:
#         # В противном случае список не отсортирован
#         return False

# # Запрашиваем у пользователя последовательность чисел для списка
# lst = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

# # Проверяем, отсортирован ли список
# if is_sorted(lst):
#     print("Список отсортирован.")
# else:
#     print("Список не отсортирован.")
