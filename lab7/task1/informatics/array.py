#A. A[0], A[2], A[4], ...
N = int(input())
arr = list(map(int, input().split()))

for i in range(0, N, 2):
    print(arr[i], end=" ")


#B. Вывести четные элементы
N = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if i % 2 == 0:
        print(i, end=" ")

#C. Количество положительных элементов
N = int(input())
arr = list(map(int, input().split()))

count = 0
for i in arr:
    if i > 0:
        count += 1

print(count)

#D. Количество элементов, больших предыдущего
N = int(input())
arr = list(map(int, input().split()))

count = 0
for i in arr:
    if i > arr[0]:
        count += 1

print(count) 

#E. Есть ли два элемента с одинаковыми знаками
n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    if arr[i] * arr[i + 1] > 0:
        print("Yes")
        break
else:
    print("No")

#F. Количество элементов больших обоих соседей
n = int(input())
arr = list(map(int, input().split()))

count = 0

for i in range(1, n - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        count += 1

print(count)

#G. Переставить элементы в обратном порядке
n = int(input())
arr = list(map(int, input().split()))

for i in range(n // 2):
    arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]

print(*arr)
