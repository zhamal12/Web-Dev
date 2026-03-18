#A. Минимум 4 чисел
def min_num(a, b, c, d):
    m = a
    if b < m:
        m = b
    if c < m:
        m = c
    if d < m:
        m = d
    return m

a, b, c, d = map(int, input().split())
print(min_num(a, b, c, d))

#B. Степень
def square(a, b):
    return a ** b

a, b = map(int, input().split())
print(square(a, b))

#C. Исключающее ИЛИ
def xor(x, y):
    return x^y

x, y = map(int, input().split())
print(xor(x, y))