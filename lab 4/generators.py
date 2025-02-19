#task 1
def square(n):
    for i in range(1 , n+1):
        yield i*i
numer=int(input("напиши натуральное число:"))
for i in square(numer):
    print(i)


#task 2
def even(n):
    for i in range(0,n+1,2):
        yield i

numer=int(input("напиши числло:"))
for i in even(numer):
    print(i)


#task3
def div(n):
    for i in range(0, n+1):
        if i%3==0 and i%4==0:
         yield i
numer=int(input("напиши число делящееся на 3 и 4:"))
for i in div(numer):
    print(i)


#task4
def squ(a,b):
    for i in range(a, b+1):
        yield i*i
numer=int(input("цифра а:"))
numer_2=int(input("цифра b:"))
for i in squ(numer , numer_2):
    print(i)


#task5
def down(n):
    for i in range(n,-1,-1):
        yield i

numer=int(input("напиши число:"))
for i in down(numer):
    print(i)