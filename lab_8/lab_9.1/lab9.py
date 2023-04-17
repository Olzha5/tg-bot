# Функциалды және функцианалды емес функция құру

# Функционалды функция, енгізілген деректерді қабылдау және нәтиже ретінде бір мәнді қайтаратын функция.
# Функционалды емес функция, нәтиже ретінде ештеңе қайтармай,
# бір әрекет (жалпы жағдайда экранға шығару) орындайтын функция.

def functional_function(resume, work_experience):
    # функционалды функция коды
    if work_experience >= 5:
        return f"{resume}, жұмыс тәжірибесі {work_experience} жылдан астам."
    else:
        return f"{resume}, жұмыс тәжірибесі {work_experience} жыл."

def non_functional_function(resume, work_experience):
    # функционалды емес функция коды
    if work_experience >= 5:
        print(f"{resume}, жұмыс тәжірибесі {work_experience} жылдан астам.")
    else:
        print(f"{resume}, жұмыс тәжірибесі {work_experience} жыл.")
# функционалды функцияның пайдаланылуы
resume = "Abukhan Olzhas"
work_experience = 2
result = functional_function(resume, work_experience)
print(result)  

# функционалды емес функцияның пайдаланылуы
resume = "Abukhan Olzhas"
work_experience = 2
non_functional_function(resume, work_experience)  


# тізім кортеж сөздік кайтаратын функция
def tsk():
    return [1, 2, 3], ('a', 'b', 'c'), {'key1': 'value1', 'key2': 'value2'}
print(tsk())





