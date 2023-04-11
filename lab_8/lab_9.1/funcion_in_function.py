def compose(f, g):
    def h(x):
        return f(g(x))
    return h

def square(x):
    return x * x

def double(x):
    return x * 2

f = square
g = double
h = compose(f, g)

x = 3
result = h(x)
print(result) # (3 * 2) * (3 * 2) = 36
