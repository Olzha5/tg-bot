# 1.Біркортежді 0-ден 5-кедейінгіонкездейсоқбүтінсанментолтырыңыз.
# Сондай-ақекіншікортежді-5-тен 0-гедейінгісандарментолтырыңыз.
# Кортеждердісандарментолтыруүшінбірфункцияныжазыңыз. Үшіншікортеждіжасауүшін + операторынпайдаланып
# екікортеждібіріктіріңіз. Ондағынөлдердіңсанынанықтауүшінкортеждіңcount() əдісінпайдаланыңыз.
# Үшіншікортеждіжəнеондағынөлдерсанынбасыпшығарыңыз.


# import random

# def generate_tuples():
#     tuple1 = tuple(random.randint(0, 5) for i in range(10))
#     tuple2 = tuple(random.randint(-5, 0) for i in range(10))
#     return tuple1, tuple2

# tuple1, tuple2 = generate_tuples()
# tuple3 = tuple1 + tuple2
# print(tuple1)
# print(tuple2)
# print(tuple3)
# count_zeros = tuple3.count(0)
# print("Количество нулей в третьем кортеже:", count_zeros)

#2 Екі элементі бар кірістірілген кортежді жасаңыз: 
# бүтінсан жəне тағы екі элементі бар кірістірілген кортеж: 
# нақты сан жəне тағы екі элементі бар кірістірілген кортеж:
# күрделі сан жəне тағы екі элемент элементі бар кірістірілген кортеж: жолжəнежол.
# боскортеж. Соңғыжолдыэкранғабасыпшығарыңыз.

# my_tuple = (42, (3.14, (1+2j, ('Hello World', ()))))


# print(my_tuple[1][1][0])



# my_tuple = (7, "apple", 2)
# print(my_tuple)
# my_tuple = (3.14, "orange", 5)
# print(my_tuple)
# my_tuple = (1/3, "banana", 4)
# print(my_tuple)
# my_tuple = ("path", " ")
# print(my_tuple)
# print(my_tuple[1])

# my_tuple = (7, "apple", 2)
# print(my_tuple)
# my_tuple = (3.14, "orange", 5)
# print(my_tuple)
# my_tuple = (1/3, "banana", 4)
# print(my_tuple)
# my_tuple = ("path", " ")
# print(my_tuple)
# print(my_tuple[1])
# reshka = (((1, "apple", 2),), ((3.14, "orange", 5), ()), ((1/3, "banana", 4), ()), (("path", " "),))
# print(reshka)



# 3.Жалпышығындар. Аптаныңəркүнінешығындарыңыздыесептейтінбағдарламажасаңыз. 
# Келесісанаттарбойыншашығыстар (жолшығындары, түскіасжəнет.б.) 
# Сомалартізімдесақталуыкерек.
# Апталықжалпышығындарыңыздыесептеужəненəтиженікөрсетуүшінциклдыпайдаланыңыз.

# # Апталық күндердің тізімін енгізіңіз
# days_of_week = ['Дүйсенбі', 'Сейсенбі', 'Сәрсенбі', 'Бейсенбі', 'Жұма', 'Сенбі', 'Жексенбі']

# # Күндер бойынша шығындарды сақтау үшін диктіонерді құрамыз
# expenses = {}
# for day in days_of_week:
#     expenses[day] = []

# # Аптаның жалпы шығындарын есептеу үшін цикл жасаймыз
# for day in days_of_week:
#     # Жол шығындарын есептеу үшін көбіне төлеуді сұраған болсақ:
#     expenses[day].append(float(input(f"{day} күніне көбіне жол шығындарыңызға қанша төлегіңіз кетті? ")))
#     # Түскі ас жəне т.б. шығындарын есептеу үшін қажетті сан жазуымыз керек болса:
#     expenses[day].append(float(input(f"{day} күніне түскі ас жəне т.б. үшін қанша төлегіңіз кетті? ")))

# # Аптаның жалпы шығындарын есептеу нəтижесін көрсету
# for day in days_of_week:
#     print(f"{day} күніне жалпы {sum(expenses[day])} тг  кетті.")
 


#  4. Оқушылардың аты-жөнін бос орынмен бір жолға енгізіңіз. Олардың негізінде
# кортеж қалыптасады. Экранда осы кортеждегі «ва» фрагменті бар барлық
# атауларды көрсетіңіз. Атаулар бос орындармен бөлінген бір жолда көрсетіледі.

students = []

for i in range(3):
    name = input("Оқушының аты жөнін енгізіңіз: ")
    first_name, last_name = name.split()
    students.append((first_name, last_name))
for student in students:
    if student[0].endswith('ov') or student[1].endswith('ov'):
        full_name = student[0] + " " + student[1]
        full_name = full_name.replace(" ", "_")
    # if student[0] or "ва" in student[1]:

    #     full_name = student[0] + " " + student[1]student[0].endswith('ov')
    #     full_name = full_name.replace(" ", "_")
        print(full_name)


# 5. Кез келген енгізілген қазақша мəтінді кириллицадан латыншаға түрлендіретін
# программа жазыңыз.

# Импорт библиотеки и использование функции для транслитерации

# from unidecode import unidecode
# text = input("Введите казахский текст на кириллице: ")
# print(unidecode(text))







# #len(): кортежмен және жиындармен қанша элемент бар екенін анықтау үшін қолданылады.
# my_tuple = (1, 2, 3, 4, 5)
# print(len(my_tuple))  # 5

# my_set = {1, 2, 3, 4, 5}
# print(len(my_set))  # 5
# #in: элементтерді кортеж жəне жиындарда бар екенін тексеру үшін қолданылады.
# my_tuple = (1, 2, 3, 4, 5)
# if 3 in my_tuple:
#     print("3 бар")

# my_set = {1, 2, 3, 4, 5}
# if 6 not in my_set:
#     print("6 жоқ")

# #max() және min(): кортеж жəне жиындардың ең кіші және ең үлкен элементтерін табу үшін қолданылады.
# my_tuple = (1, 2, 3, 4, 5)
# print(max(my_tuple))  # 5
# print(min(my_tuple))  # 1

# my_set = {1, 2, 3, 4, 5}
# print(max(my_set))  # 5
# print(min(my_set))  # 1
# #add(): жиындарға элемент қосу үшін қолданылады.
# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)  # {1, 2, 3, 4, 5, 6}
# #count(): кортежде көрсетілген элементтердің санын табу үшін қолданылады.
# my_tuple = (1, 2, 3, 4, 5, 2, 3)
# print(my_tuple.count(2))  # 2
# print(my_tuple.count(6))  # 0





# matryoshka = (42, (7.474, (2+3j, ('sdgfhdf', ()))))
# print(matryoshka)

# outer_tuple = matryoshka[0]
# middle_tuple = matryoshka[1]
# inner_tuple_1 = middle_tuple[1]
# inner_tuple_2 = inner_tuple_1[1]
# inner_tuple_3 = inner_tuple_2[1]

# print("Outer tuple:", outer_tuple)
# print("Middle tuple:", middle_tuple)
# print("Inner tuple 1:", inner_tuple_1)
# print("Inner tuple 2:", inner_tuple_2)
# print("Inner tuple 3:", inner_tuple_3)


# while True:
#     num = int(input())
#     if num == 1:
#         print("Outer tuple:", outer_tuple)
#     elif num == 2:
#         print("Middle tuple:", middle_tuple)
#     elif num == 3:
#         print("Inner tuple 1:", inner_tuple_1)
#     elif num == 4:
#         print("Inner tuple 2:", inner_tuple_2)
#     elif num == 5:
#         print("Inner tuple 3:", inner_tuple_3)
#     else:
#         print("Error")




