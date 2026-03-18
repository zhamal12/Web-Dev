#A. Список квадратов
N = int(input())

i = 1
while i * i <= N:
    print(i * i)
    i += 1

#B. Минимальный делитель
N = int(input())
i = 2
while i <= N:
    if N % i == 0:
        print(i)
        break
    i += 1

#C. Список степеней двойки
N = int(input())

i = 1

while i <= N:
    print(i, end=" ")
    i *= 2

#D. Точная степень двойки
N = int(input())
while N > 1:
    if N % 2 != 0:
        print("No")
        break
    N //= 2
else:
    print("Yes")

#E. Двоичный логарифм
N = int(input())

k = 0
power = 1

while power < N:
    power *= 2
    k += 1

print(k)


