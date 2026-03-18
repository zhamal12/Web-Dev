#A.Максимум из двух чисел
a = int(input())
b = int(input())

if a > b:
    print(a)
else:
    print(b)

#B.Вискосный год
n = int(input())

if n % 4 == 0:
    print("Yes")
elif n % 100 !=0 or n % 400 != 0:
    print("No")

#C. Тестирующая система
correct = int(input())
student = int(input())

if (correct == 1 and student == 1) or (correct != 1 and student != 1):
    print("Yes")
else:
    print("No")

#D.Знак числа
x = int(input())

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    elif x == 0:
        return 0

res = sign(x)
print(res)

#E.Какое из чисел больше 
a = int(input())
b = int(input())

if a > b:
    print(1)
elif b > a:
    print(2)
else:
    print(0)


