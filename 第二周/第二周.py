#263A
l = []
for i in range(5):
    l.append(input().split())
for i in range(5):
    if '1' in l[i]:
        print(abs(i-2)+abs(l[i].index('1')-2))

#E02808
list0 = input().split()
l = int(list0[0]) + 1
m = int(list0[1])
list1 = []
for i in range(l):
    list1.append(1)
for i in range(m):
    list0 = input().split()
    a = int(list0[0])
    b = int(list0[1])
    for i in range(a,b+1):
        list1[i] = 0
print(list1.count(1))

#1328A
t = int(input())
list0 = []
for i in range(t):
    list0.append(input().split())
for ab in list0:
    a = int(ab[0])
    b = int(ab[1])
    c = a/b
    if c == int(c):
        print(0)
    else:
        print((a//b+1)*b - a)

#427A
n = input()
list0 = input().split()
a = 0
b = 0
for i in list0:
    a += int(i)
    if a < 0:
        a = 0
        b += 1
print(b)

#水仙花数II
list0 = input().split()
a = int(list0[0])
b = int(list0[1])
c = 0
for i in range(a,b+1):
    x = i//100
    y = (i-x*100)//10
    z = i-x*100-y*10
    if i == x**3 + y**3 + z**3:
        if c == 0:
            print(i,end='')
            c = 1
        else:
            print(f' {i}',end='')
if c == 0:
    print('NO')

#M01922
import math
while True:
    n = int(input())
    if n == 0:
        break
    list0 = []
    set0 = set()
    for i in range(n):
        list0.append((input().split()))
        v = int(list0[i][0])
        t = int(list0[i][1])
        if t >= 0:
            tz = math.ceil(t + (16200/v))
            set0.add(tz)
    print(min(set0))

#C.M21532
n = int(input())
a = 1
for i in range(6,n+1):
    if n % i == 0:
        print(n//i)
        a = 0
        break
if a == 1:
    print (1)

#M02981
a = int(input())
b = int(input())
c = a + b
print(c)
