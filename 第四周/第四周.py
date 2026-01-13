#34B Sale
li0 = input().split()
n = int(li0[0])
m = int(li0[1])
li = list(map(int,input().split()))
s = 0
for _ in range(m):
    a = min(li)
    if a < 0:
        s += min(li)
        li.remove(a)
    else:
        break
print(-s)

#160A Twins
n = int(input())
list0 = input().split()

s = 0
t = 0
a = 0
for i in range(n):
    list0[i] = int(list0[i])
list0.sort(reverse=True)
for i in range(n):
    s += list0[i]
for i in range(n):
    t += list0[i]
    a += 1
    if t > s/2 :
        break
print(a)

#1879B. Chips on the Board
t = int(input())
li = []
for _ in range(t):
    n = int(input())
    li1 = list(map(int,input().split()))
    li2 = list(map(int,input().split()))
    a = min(li1)
    b = min(li2)
    s1 = n*a
    s2 = n*b
    for i in range(n):
        s1 += li2[i]
        s2 += li1[i]
    li.append(min(s1,s2))
for i in li:
    print(i)

#M01017: 装箱问题
import math
while 1:
    li=list(map(int,input().split()))
    if li==[0,0,0,0,0,0]:
        break
    a,b,c,d,e,f=li[0],li[1],li[2],li[3],li[4],li[5]
    s=f+e+d+c//4
    a-=11*e+max(5*d-b,0)*4
    b=max(0,b-5*d)
    a=max(a,0)
    if c%4==0:
        pass
    elif c%4==1:
        s += 1
        if b >= 5:
            b -= 5
            a -= 7
        else:
            b = 0
            a -= 7 + (5-b)*4
    elif c%4 == 2:
        s += 1
        if b>= 3:
            b -= 3
            a -= 6
        else:
            b = 0
            a -= 6 +(3-b)*4
    else:
        s += 1
        if b >= 1:
            b -= 1
            a -= 5
        else:
            a -= 9
    if b%9 != 0:
        s += math.ceil(b / 9) + math.ceil(max(0, (a - 36 + b % 9 * 4)) / 36)
    else:
        s += b//9 + math.ceil(max(0,a)/36)
    print(s)

#M01008: Maya Calendar
di = {'pop':0,'no':1,'zip':2,'zotz':3,'tzec':4,'xul':5,'yoxkin':6,'mol':7,'chen':8,'yax':9,'zac':10,'ceh':11,'mac':12,'kankin':13,'muan':14,'pax':15,'koyab':16,'cumhu':17,'uayet':18}
li = ['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
n = int(input())
print(n)
for _ in range(n):
    l = input().split()
    a = int(l[0][:-1])
    b = di[l[1]]
    c = int(l[2])
    date = a + b*20 + c*365 + 1
    z = (date-1)//260
    x = (date)%13
    if x == 0:
        x = 13
    y = li[date%20-1]
    print(f'{x} {y} {z}')

#T-primes
se0 = {2,3,5,7,11,13,17,19,23,29,31}
se = set(range(37,10**3))
for j in se0:
    li0 = []
    for i in se:
        if i%j == 0:
            li0.append(i)
    for i in li0:
        se.remove(i)
se1 = se0 | se
se = set(range(10**3,10**6))
for j in se1:
    li0 = []
    for i in se:
        if i%j == 0:
            li0.append(i)
    for i in li0:
        se.remove(i)
se = se | se1
n = int(input())
li = map(int,input().split())
for i in li:
    if i**0.5 in se:
        print('YES')
    else:
        print('NO')
