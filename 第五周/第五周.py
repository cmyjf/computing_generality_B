#E29895:分解因数
n = int(input())
for i in range(2,n+1):
 if n%i == 0:
  print(n//i)
  break

#E29940: 机器猫斗恶龙
n = int(input())
li = input().split()
a = 0
b = 0
for i in li:
 a += int(i)
 b = min(a,b)
print(-b+1)

#M29917: 牛顿迭代法
while 1:
 try:
    a = float(input())
    x = 1
    x1 = 1
    b = 0
    while 1:
        x = x1
        x1 = x - (x**2 - a)/(x*2)
        b += 1
        if abs(x-x1)<=10**(-6):
            break
    print(b,end=' ')
    print(f'{x1:.2f}')
 except EOFError:
    break

#M29949: 贪婪的哥布林
n,m = map(int,input().split())
li = []
for i in range(n):
    a,b = map(int,input().split())
    c = a/b
    li.append([c,b])
    li.sort()
d = 0
e = 0
for i in range(n):
    if d+li[n-1-i][1] < m:
        d += li[n-1-i][1]
        e += li[n-1-i][0]*li[n-1-i][1]
    else:
        e += li[n-1-i][0]*(m-d)
        break
print(f'{e:.2f}')

#M29918: 求亲和数
def hh(n):
    a = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            a += i
            a += n//i
    if n**0.5 % 1 == 0:
        a -= n**0.5
    return a
n = int(input())
for a in range(1,n+1):
    b = hh(a)
    if n >= b > a and a == hh(b):
        print(f'{a} {b}')

#T29947:校门外的树又来了
l, m = map(int, input().split())
se = set()
for _ in range(m):
    a, b = map(int, input().split())
    ab = 1
    for i in se:
        c,d = i[0],i[1]
        if a >= c and d >= b:
            ab = 0
            break
    if ab == 0:
        continue
    while 1:
        aa = 0
        for i in se:
            c,d = i[0],i[1]
            if a<=c<=b or a<=d<=b:
                aa = 1
                a = min(a,c)
                b = max(b,d)
                break
        if aa == 1:
            se.remove((c,d))
            continue
        else:
            se.add((a,b))
            break
t = 0
for i in se:
    a,b = i[0],i[1]
    t += b-a+1
print(l+1-t)
