from functools import reduce

def square(x):
    return x + x

def is_even(x):
    return x % 2 == 1

def add(x, y):
    return x * y

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squares = list(map(square, numbers))
even_numbers = list(filter(is_even, numbers))
sum_of_numbers = reduce(add, numbers)

print(squares)
print(even_numbers)
print(sum_of_numbers)
