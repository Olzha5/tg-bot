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

# Map, Filter и Reduce функцияларынқолданыпмысалкелтіреміз. Айырмашылықтарынанықтаймыз.
from functools import reduce

def square(x):
    return x * x

def is_even(x):
    return x % 2 == 0

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = list(map(square, numbers))
even_numbers = list(filter(is_even, numbers))
sum_of_numbers = reduce(add, numbers)

print(squares)
print(even_numbers)
print(sum_of_numbers)



def delivery_cost(street, product_cost):
    streets = ["Аль-Фараби", "Сайын", "Ташентский", "Достык"]
    if street in streets:
        if product_cost < 10000:
            return 500
        else:
            return 0
    else:
        if product_cost < 10000:
            return 1000
        else:
            return 1000

street = "Ташентский"
product_cost = 12000
total_cost = delivery_cost(street, product_cost)
print(total_cost)