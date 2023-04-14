import math

number = '010000000111111010111001'

def Question1(number):
    # sign  
    s = int(number[0])
    # exponent
    c = int(number[1:12], 2)

    # fraction(mantissa)
    f = 0
    for n, bit in enumerate(number[12:], 1):
        f += int(bit) * 2**(-1*n)

    return (-1) ** s * (2**(c-1023) * (1+f))

print(Question1(number))
print()

def Question2(number):
    num = Question1(number)
    n = 0
    while num >= 1:
        num /= 10
        n += 1
    while num < 0.1:
        num *= 10
        n -= 1
    return int(num * 1000)

print(Question2(number))
print()

def Question3(number):
    num = Question1(number)
    n = 0
    while num >= 1:
        num /= 10
        n += 1
    while num < 0.1:
        num *= 10
        n -= 1
    num += 0.0005
    return int(num * 1000)

print(Question3(number))
print()

def Question4a(number):
    num1 = Question1(number)
    num2 = Question3(number)
    return abs(num1 - num2)

print(Question4a(number))

def Question4b(number):
    num1 = Question1(number)
    num2 = Question3(number)
    return abs(num1 - num2) / abs(num1)

print(Question4b(number))
print()

def Question5(error):
    x = 1
    n = 1
    while(True):
        if (abs((-1)**n * (x**n / n**3))) < error:
            break
        n += 1
    return n-1

print(Question5(10**-4))
print()

def Question6a(a, b, tol):
    def func(x):
        return (x**3) + (4 * (x**2)) - 10
    i = 0
    while abs(b-a) > tol:
        p = (a + b) / 2
        if func(p) == 0:
            break
        elif func(p) * func(a) < 0:
            b = p
        else:
            a = p
        i += 1
    return i

print(Question6a(-4.0, 7.0, 10**-4))

def Question6b(p_prev, tol):
    def func(x):
        return (x**3) + (4 * (x**2)) - 10
    def func_deriv(x):
        return (3 * (x**2)) + (8 * x)
    i = 0
    i = 1

    while(True):
        if func_deriv(p_prev) == 0:
            break
        else:
            p_next = p_prev - (func(p_prev) / func_deriv(p_prev))
            if abs(p_next - p_prev) < tol:
                break
            i += 1
            p_prev = p_next

    return i

print(Question6b(7.0, 10**-4))