def compose(f, g):
    def h(x):
        return f(g(x))
    return h

# Пример использования функции compose
def square(x):
    return x * x

def double(x):
    return x * 2

# Создаем композицию функций square и double
composed_function = compose(square, double)

# Вызываем новую функцию h(x) с аргументом x = 3
result = composed_function(3)
print(result)  # Вывод: 36, так как square(double(3)) = square(6) = 36
