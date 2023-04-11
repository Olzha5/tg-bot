# 2. Берілген есептерді шығару: 
# 1. Бірінші жолда N саны — сөздіктегі элементтер саны. Əр елде жəне онда ағып жатқан өзендердің тізімі (сөздік ретінде) берілген. Содан кейін өзендердің атаулары беріледі (тізім түрінде). Тапсырмаларды орындаңыз: 
# 1) Əрбір өзен үшін оның қай елде ағып жатқанын көрсетіңіз. 
# 2) Енгізілген өзен атауының сөздікте бар-жоғын тексеріңіз (бар немесе жоқ деген ақпаратты шығарыңыз) 
# 3) Сөздікке жаңа ел-өзен жұбын қосыңыз. 

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
def eldegi_ozen(country, countries):
    if country in countries:
        print(f"{country}")
        +
   
country_name = input("Ел енгіз: ")
eldegi_ozen(country_name, countries)

