#A.Четные числы
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")

#B.Остаток
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(a, b + 1):
    if i % d == c:
        print(i, end=" ")

#C.Квадраты
a = int(input())
b = int(input())

for i in range(a, b + 1):
    if int(i ** 0.5) ** 2 == i:
        print(i, end=" ")

#x Цифра в числе
x = input()
d = input()

count = 0

for digit in x:
    if digit == d:
        count += 1

print(count)

#x Сумма цифр
x = input()

total = 0
for digit in x:
    total += int(digit)
print(total)

#x Переверни число
x = input()

started = False

for i in range(len(x) -1, -1, -1):
    if x[i] != '0':
        started = True
    if started:
        print(x[i], end="")

#G. Минимальный делитель
x = int(input())

for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break

#H. Делители числа
x = int(input())

for i in range(1, x + 1):
    if x % i == 0:
        print(i, end=" ")

#I. Количество делителей
x = int(input())

count = 0
for i in range(1, x + 1):
    if x % i == 0:
        count += 1
print(count)

#J. Сумма ста
total = 0

for _ in range(100):
    x = int(input())
    total += x
print(total)

#K. Сумма чисел
N = int(input())

total = 0

for _ in range(N):
    x = int(input())
    total += x

print(total)

#x Перевод числа
b = input()

result = 0

for digit in b:
    result = result * 2 + int(digit)

print(result)

#M. Нули
N = int(input())

count = 0
for _ in range(N):
    x = int(input())
    if x == 0:
        count += 1
print(count)
