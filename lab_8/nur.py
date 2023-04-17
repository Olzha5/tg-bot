# #1
# def compose_functions(f, g):
#     def h(x):
#         return f(g(x))
#     return h
#
# def a(x):
#     return x + 1
#
# def m(x):
#     return 2 * x
#
# f = input("first function (e.g., add_one): ")
# g = input("second function (e.g., multiply): ")
#
# f = globals()[f]
# g = globals()[g]
#
# h = compose_functions(f, g)
# print(h(5))
#
# #2
# def calculate_delivery_cost(street_name, price):
#     delivery_cost = 0
#     if street_name in ['Al-Farabi', 'Sain', 'Tashkent', 'Dostyk']:
#         if price < 10000:
#             delivery_cost = 500
#     else:
#         if price < 10000:
#             delivery_cost = 1000
#     return delivery_cost
#
# street_name = input(" street name: ")
# price = float(input("price: "))
#
# total_delivery_cost = calculate_delivery_cost(street_name, price)
#
# if total_delivery_cost == 0:
#     print("Delivery is free.")
# else:
#     print(f"The total delivery cost for {street_name} and goods worth {price}tg is {total_delivery_cost}tg.")
# #3
# def get_list(n):
#     squares = []
#     for i in range(1, n+1):
#         squares.append(i**2)
#     return squares
#
# def get_tuple(a, b, c):
#     return (a, b, c)
#
# def get_dict():
#     fruits = {"apple": "red", "banana": "yellow", "orange": "orange"}
#     return fruits
#
# squares = get_list(5)
# print(squares)
#
# my_tuple = get_tuple(1, 2, 3)
# print(my_tuple)
#
# fruit_dict = get_dict()
# print(fruit_dict)

# #4
# from functools import reduce
#
# my_list = [1, 2, 3, 4, 5]
# result_map = list(map(lambda x: x * 2, my_list))
# print(result_map)
#
# result_filter = list(filter(lambda x: x % 2 == 0, my_list))
# print(result_filter)
#
# result_reduce = reduce(lambda x, y: x * y, my_list)
# print(result_reduce)
# #5
# def functional(resume):
#     required_keywords = ["Python", "machine learning", "data analysis", "problem solving"]
#     return all(keyword in resume.lower() for keyword in required_keywords)
#
#
# def non_functional(resume):
#     print("This candidate has a degree in Computer Science and 3 years of experience in software development.")
#     print(
#         "They are proficient in Python, Java, and C++, and have worked on several projects involving machine learning and data analysis.")