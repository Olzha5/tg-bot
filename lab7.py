student_info = {
    "Имя": "Абухан",
    "Фамилия": "Олжас",
    "Возраст": 20,
    "Город": "Алматы",
    "Университет": "Сатпаев",
    "Факультет": "ИАиТИ",
    "Специальность": "Computer Science",
    "Средний балл": 3.2,
    "Курсы": ["Функциональное программирование"]
}
def print_keys(dict):
    print("Данный:")
    for key in dict.keys():
        print(key)
print_keys(student_info)

def print_values(dict):
    print("Данный:")
    for value in dict.values():
        print(value)

print_values(student_info)
def print_items(dict):
    print("Полный Резюме:")
    for item in dict.items():
        print(item)

print_items(student_info)


# 2. Берілген есептерді шығару: 
# 1. Бірінші жолда N саны — сөздіктегі элементтер саны. Əр елде жəне онда ағып жатқан өзендердің тізімі (сөздік ретінде) берілген. Содан кейін өзендердің атаулары беріледі (тізім түрінде). Тапсырмаларды орындаңыз: 
# 1) Əрбір өзен үшін оның қай елде ағып жатқанын көрсетіңіз. 
# 2) Енгізілген өзен атауының сөздікте бар-жоғын тексеріңіз (бар немесе жоқ деген ақпаратты шығарыңыз) 
# 3) Сөздікке жаңа ел-өзен жұбын қосыңыз. 
# В первой строке содержится число N — число элементов в словаре. Дан список (словарь) стран и рек, протекающих в каждой стране. Затем даны названия рек (в виде списка). Выполните задания: 1) Для каждой реки укажите, в какой стране она протекает. 
# 2) Проверьте, есть ли введенное название реки в словаре (вывести есть или нет) 
# 3) Добавьте новую пару страна-река в словарь. 


countries = {
    "Казахстан": ["Іле", "Сырдария", "Нура"],
    "Корея": ["Кан", "Йонсанган", "Кымган"],
    "Туркия": ["Евфрат", "Гедис" , "Мурат"]
}
def find_river_country(river, countries):
    for country, rivers in countries.items():
        if river in rivers:
            return country
    return None

rivers = ["Кан", "Іле", "Гедис"]
for river in rivers:
    country = find_river_country(river, countries)
    if country:
        print(f"Река {river} орналасқан {country}.")
    else:
        print(f"Река туралы {river} информация жоқ.")
def find_river(river, countries):
    for country, rivers in countries.items():
        if river in rivers:
            return True
    return False

river_name = input("Река аты: ")
if find_river(river_name, countries):
    print(f"{river_name} ")
else:
    print(f"{river_name} ")

    country_name = input("Ел аты: ")
if country_name in countries:
    countries[country_name].append(river_name)
else:
    countries[country_name] = [river_name]

print(f"Сөздік қосылған: {countries}")


# 2. Əлеуметтік желідегі аккаунтында бір жұлдыздың фотосына пікір қалдырды. Кейбір келушілер бірнеше пікір қалдырды. Пікірлер тізімінен комментаторлардың бірегей санын анықтау талап етіледі. Пікірлер бағдарламаны енгізу кезінде келесі форматта қабылданады: 
# 1 аты: түсініктеме 1 
# 2 аты: түсініктеме 2 ... 
# аты N: түсініктеме N бос жол енгізілгенше. Сондай-ақ əртүрлі комментаторлардың аты-жөні сəйкес келмейді деп болжанады. Бірегей комментаторлардың жалпы санын көрсетіңіз. 
# В аккаунте социальной сети одного звезды прокомментировали фотографию. Некоторые посетители оставляли несколько комментариев. Требуется по списку комментариев определить уникальное число комментаторов. Комментарии поступают на вход программы в формате: имя 1: комментарий 1 имя 2: комментарий 2 ... имя N: комментарий N пока не будет введена пустая строка. Также полагается, что имена у разных комментаторов не совпадают. Вывести на экран общее число уникальных комментаторов. 
commentators = {}

while True:
    input_string = input()
    if input_string == "":
        break
    name, comment = input_string.split(": ")
    if name not in commentators:
        commentators[name] = None

print(len(commentators))


# 2.	Телефон нөмірлерін аты бойынша табуға көмектесетін бағдарлама жазыңыз. Бірінші жолда бір бүтін сан бар - телефон нөмірлерінің саны. Келесі жолдарда бос орынмен бөлінген телефондар мен олардың иелерінің аты бар. Келесі жолда сұрау бар - бұл телефонын тапқыңыз келетін атау. Телефон нөмірін сұрағандай көрсетіңіз. Телефон кітапшасында осындай есімі бар адамның телефон нөмірлері болмаса, сəйкес жолда «Телефон кітапшасында жоқ» деп басып шығарыңыз.
#  Напишите программу, которая поможет находить номера телефонов по имени. В первой строке задано одно целое число - количество номеров телефонов. В следующих строках заданы телефоны и имена их владельцев через пробел. В следующей строке записан запрос — это имя, чей телефон нужно найти. Вывести номер телефона согласно запросу. Если в телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «Нет в телефонной книге». 

# 4. HR маманына «Демалыс кестесі» сөздігін жасаңыз. Белгілі демалыс кестесіне сəйкес, берілген айда кімнің демалысы бар екенін анықтауды үйреніңіз. Бірінші жолда бүтін сан бар - жұмысшылар саны. Келесі N жолда олардың демалыс күні туралы ақпарат бар. Əрбір жол бір-бірінен бос орынмен бөлінген үш бөліктен тұрады - қызметкердің аты-жөні, оның демалыс күні мен айы. Келесі жолда сұрау бар - бұл айдың атауы. Шығару, бос орынмен бөлінген, көрсетілген айда демалыста болған барлық қызметкерлердің тегі. Егер берілген айда ешкім демалысқа шықпаса, жауап жолын бос қалдырыңыз. 
# Составьте словарь «График отпусков» для специалиста отдела кадров. По известному графику отпусков научитесь определять, у кого отпуск в заданном месяце. В первой строчке записано целое число – количество сотрудников. В следующих N строчках записана информация о дате их отпуска. Каждая строчка состоит из трёх частей, разделённых пробелом – фамилии сотрудника, дня и месяца его отпуска. В следующей строке записан запрос — это название месяца. Выведите через пробел фамилии всех сотрудников, у которых отпуск в указанном месяце. Если в заданном месяце никто не идет в отпуск, оставьте строку ответа пустой.
n = int(input())  # количество сотрудников

vacations = {}  # словарь для хранения графика отпусков

# заполняем словарь месяцами отпусков для каждого сотрудника
for i in range(n):
    line = input().split()
    name = line[0]
    month = line[2]
    if name in vacations:
        vacations[name].append(month)
    else:
        vacations[name] = [month]

# запрашиваем список сотрудников, у которых отпуск в заданном месяце
month = input().strip()
result = []
for name, months in vacations.items():
    if month in months:
        result.append(name)

# выводим результаты
if result:
    print(" ".join(result))
else:
    print()