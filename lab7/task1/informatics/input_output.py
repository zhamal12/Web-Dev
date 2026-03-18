#A.Гипотенуза
import math
a = float(input())
b = float(input())

c = math.sqrt(a**2 + b**2)
print(c)

#B.Следующее и предыдущее
n = int(input())

print("The next number for the number ", n, " is ", n + 1, ".", sep="")
print("The previous number for the number ", n, " is ", n - 1, ".", sep="")

#C.Дележ яблок - 1
N = int(input())
K = int(input())

res = K // N
print(res)

#D. Дележ яблок - 2
N = int(input())
K = int(input())

res = K % N
print(res)

#E. МКАД
v = int(input())
t = int(input())

position = (v * t) % 109
print(position)

