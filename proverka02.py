
# 1. Екі бүтін А және В саны берілген (А ≤ B бар). А-дан В-ға дейінгі барлық сандарды басып шығарыңыз. 

# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно. 

# a=int(input("a = "))
# b=int(input("b = "))

# for i in range (a,b+1):
#     print (i)

# 2. А және В екі бүтін сандар берілген.
#  А<B болса, өсу ретімен немесе басқаша жағдайда кему ретімен А-дан В-ға дейінгі барлық сандарды басып шығарыңыз. 

# a=int(input("a = "))
# b=int(input("b = "))
# if a<b:
#     for i in range (a,b+1):
#         print(i)
# else:
#     for i in range(a, b-1, -1):
#         print(i)

# 3. Екі бүтін А және В саны берілген, A>B.
#  А-дан В-ға дейінгі барлық тақ сандарды кему ретімен басып шығарыңыз. Бұл тапсырмада if операторынсыз орындай аласыз. 
# a = int(input("a = "))
# b = int(input("b = "))
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i, end=' ')

# 4.Үстел ойыны үшін 1-ден N-ге дейінгі сандары бар карталар пайдаланылады.Бір карта жоғалады.
#  Қалған карталардың сандарын білу арқылы оны табыңыз. 
# N саны берілген, содан кейін N − 1 қалған карталардың саны (1-ден N-ге дейінгі әртүрлі сандар).
#  Бағдарлама жоғалған картаның нөмірін көрсетуі керек. 
# def missing_card(N, cards):
#     return sum(range(1, N + 1)) - sum(cards)

# N = int(input("Карталар санын енгізіңіз: "))
# cards = [int(input("Карта нөмірін енгізіңіз: ")) for i in range(N - 1)]
# print("Жетіспейтін карта: ", missing_card(N,cards))


#4/1 Кіші және бас әріптерді қамтитын жол енгізіледі. Бір жағдайда бірдей жолды шығару қажет, 
# ол қай әріптердің үлкенірек екеніне байланысты. Егер тең болса, кіші әріпке түрлендіріңіз.
#  Мысалы, «HeLLo World» жолы енгізілсе, оны «hello world» түрлендіру керек, себебі бастапқы
#   жолда кіші әріптер көбірек. Кодыңызда for циклды пайдаланыңыз. upper() (бас әріпті түрлендіру) 
#   және lower () (кіші әріпті түрлендіру),
#  сонымен қатар жолдың немесе таңбаның регистрін тексеретін isupper() және islower() әдістері. 

# def Turlendiru(soilem):
#     upper_count = 0
#     lower_count = 0
    
#     for char in soilem:
#         if char.isupper():
#             upper_count = upper_count+1
#         elif char.islower():
#             lower_count = 1 +lower_count
            
#     if upper_count > lower_count:
#         return soilem.upper()
#     else:
#         return soilem.lower()

# soilem = str(input("soilem zhaz : "))
# turlengen_s = Turlendiru(soilem)
# print(turlengen_s) 
## 10 primer string soilemderge 
# def Titlee(soilem):
#     return soilem.title()
# soilem = str(input("soilem engiz: "))
# Titlee_s = Titlee(soilem)
# print(Titlee_s)

# def Rstrip(soilem):
#     return soilem.swapcase()
# soilem = str(input("soilem engiz: "))
# Rstrpp_s = Rstrip(soilem)
# print(Rstrpp_s)

# text = "Salem alem Hello world"
# print(len(text))
# print(text.upper())
# print(text.lower())
# print(text.split())
# print(text.count("a"))
# print(text.replace("alem", "Hello"))
# print(text.endswith("testing."))





#4/2 isdigit() жол әдісі жолда тек сандар бар-жоғын тексереді. Енгізуден екі бүтін санды сұрайтын және
#  олардың қосындысын басып шығаратын программа жазыңыз. Қате енгізілген жағдайда, бағдарлама қатемен 
#  аяқталмауы керек,
#  бірақ сандарды сұрауды жалғастыру керек. try-exception ерекше жағдай өңдеушісін пайдаланылмауы керек

# while True:
    # try:
        # num1 = input("Nakty san engiziniz: ")
        # num2 = input("Nakty san engiziniz: ")
        # if num1.isdigit() and num2.isdigit():
            
        #     result = int(num1) + int(num2)
        #     print("kosyndysy", result)
        #     break  
        # else:
        #     print("Kate: Nakkty san engiziniz")
    # except:
    #     print("Kate: Nakkty san engiziniz")

# text = "This is a sample string for testing."
# # функция len() - выводит длину строкиprint("Длина строки:", len(text))
# # метод str.upper() - преобразует строку к верхнему регистру
# print("Верхний регистр:", text.upper())
# # метод str.lower() - преобразует строку к нижнему региструprint("Нижний регистр:", text.lower())
# # метод str.capitalize() - преобразует первую букву строки к верхнему регистру
# print("Первая буква заглавная:", text.capitalize())
# # метод str.title() - преобразует каждое слово в строке к начальному заглавному региструprint("Каждое слово с заглавной буквы:", text.title())
# # метод str.startswith() - возвращает True, если строка начинается с указанной подстроки
# print("Начинается ли строка с 'This'?", text.startswith("This"))
# # метод str.endswith() - возвращает True, если строка заканчивается на указанную подстрокуprint("Заканчивается ли строка на 'testing.'?", text.endswith("testing."))
# # метод str.count() - возвращает количество вхождений указанной подстроки в строке
# print("Сколько раз встречается подстрока 'is'?", text.count("is"))
# # метод str.replace() - заменяет указанную подстроку на другую строкуnew_text = text.replace("sample", "new")


# 1  Бағдарламалау секцияларына қатысатын әртүрлі топтағы студенттерді таныстыруды сұрайтын бағдарламаны жазыңыз. 
# Тізімді сыныптардың өсу реті бойынша сұрыптау қажет. Фамилиялар мен сыныптардың тізімін басып шығарыңыз. 


# # Создаем пустой словарь для хранения данных об учениках
# students = {}

# # Запрашиваем количество учеников
# num_students = int(input("Сколько учеников вы хотите добавить? "))

# # Запрашиваем информацию об учениках и добавляем ее в словарь
# for i in range(num_students):
#     name = input("Введите фамилию ученика: ")
#     grade = int(input("Введите класс ученика: "))
#     if grade not in students:
#         students[grade] = []
#     students[grade].append(name)

# # Упорядочиваем список по возрастанию классов
# sorted_grades = sorted(students.keys())

# # Распечатываем список фамилий и классов
# for grade in sorted_grades:
#     print("Класс {}: {}".format(grade, ", ".join(students[grade])))


# 2  Тізім қайтаратын функция жазып шығу. Алдын ала студенттердің пәндері және бағалары бар тізім құрастыр. 
# Және сол тізім бойынша студенттің атын еңгізген кезде, сол студенттің бағаларын шығарып бертін болсын.

# def get_grades(student_name):
#     # создаем словарь, содержащий список оценок для каждого ученика
#     grades = {
#         "Alice": [4, 5, 4, 3, 5],
#         "Bob": [3, 2, 4, 5, 4],
#         "Charlie": [5, 5, 5, 4, 5]
#     }
    
#     # проверяем, есть ли ученик с указанным именем в списке
#     if student_name in grades:
#         return grades[student_name]
#     else:
#         return "Ученик не найден"
    

# import random

# # генерируем список из шести случайных чисел
# numbers = random.sample(range(1, 50), 6)

# # сортируем список и выводим его на экран
# numbers.sort()
# print("Номера на вашем лотерейном билете: ", numbers)



def missing_card(N, cards):
    return sum(range(1, N + 1)) - sum(cards)


for N in range(1, 5):
    print(N)
cards = [int(input("Карта нөмірін енгізіңіз: ")) for i in range(N - 1)]
print("Жетіспейтін карта: ", missing_card(N,cards))










