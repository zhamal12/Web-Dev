#1
print("Hello, World!")

#2
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
            

#3
if __name__ == '__main__':
    n = int(input())
    
for i in range(0, n):
    print(i ** 2)

#4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a + b)
print(a - b)
print(a * b)

#5
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a // b)
print(a / b)

#6
def is_leap(year):
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False 
        
    
year = int(input())
print(is_leap(year))

#7
if __name__ == '__main__':
    n = int(input())
    
for i in range(1, n + 1):
    print(i, end="")

#8
if __name__ == '__main__':
    s = input()
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))

#9
if __name__ == '__main__':
    N = int(input())
    
list = []

for _ in range(N):
    command = input().split()
    
    if command[0] == "insert":
        i = int(command[1])
        e = int(command[2])
        list.insert(i, e)
        
    if command[0] == "print":
        print(list)
    
    if command[0] == "remove":
        e = int(command[1])
        list.remove(e)    
            
    if command[0] == "append":
        e = int(command[1])
        list.append(e)
    if command[0] == "sort":
        list.sort() 
    if command[0] == "pop":
        list.pop()
    if command[0] == "reverse":
        list.reverse()

#10
students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

second_lowest = sorted(set(score for _, score in students))[1]
print("\n".join(sorted(name for name, score in students if score == second_lowest)))

