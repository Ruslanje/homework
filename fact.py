def test(*args):
    print("Числа", args)


test(1, 2, 3, 4,)

# Факториал:

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n*factorial_recursive(n-1)
print(factorial_recursive(n = 5))