# M12560:生存游戏
n,m = map(int,input().split())
li = [['0']*(m+2)]
for _ in range(n):
    li.append(['0']+input().split()+['0'])
li.append(['0']*(m+2))
ans = [[0]*m for _ in range(n)]
def count_(x,y):
    num1 = -1
    for a in (x-1,x,x+1):
        for b in (y-1,y,y+1):
            if li[a][b] == '1':
                num1 += 1
    if li[x][y] == '1':
        if num1 == 2 or num1 == 3:
            ans[x-1][y-1] = 1
    elif li[x][y] == '0':
        num1 += 1
        if num1 == 3:
            ans[x-1][y-1] = 1
for x in range(1,n+1):
    for y in range(1,m+1):
        count_(x,y)
for a in range(n):
    for b in range(m):
        print(ans[a][b],end=' ')
    print('')

# M04133:垃圾炸弹
d = int(input())
n = int(input())
li = [[0]*1025 for _ in range(1025)]
for _ in range(n):
    x,y,i = map(int,input().split())
    for a in range(max(0,x-d),min(1025,x+d+1)):
        for b in range(max(0, y-d), min(1025, y + d+1)):
            li[a][b] += i
ans = 0
count = 1
for i in range(1025):
    for j in range(1025):
        if li[i][j] == ans:
            count += 1
        if li[i][j] > ans:
            ans = li[i][j]
            count = 1
print(count,ans)

#M02746:约瑟夫问题
while True:
    n,m = map(int,input().split())
    if n == 0:
        break
    li = [1]*n
    a = 0
    b = 0
    c = 1
    while c<n:
        if li[a] == 1:
            b += 1
            if b%m == 0:
                li[a] = 0
                c += 1
        a += 1
        if a > n-1:
            a -= n

#M26976:摆动序列
n = int(input())
li = list(map(int, input().split()))
a = li[0]
b = 0
c = 1
for i in range(n):
    if a < li[i] and b <= 0:
        a = li[i]
        b = 1
        c += 1
    elif a > li[i] and b >= 0:
        a = li[i]
        b = -1
        c += 1
    elif a < li[i] and b > 0:
        a = li[i]
    elif a > li[i] and b < 0:
        a = li[i]
print(c)

#T26971:分发糖果
n = int(input())
li = list(map(int,input().split()))
aaa = []
def cut():
    global li
    if len(li) > 1:
        t = 0
        for i in range(len(li)-1):
            if li[i] == li[i+1]:
                t = 1
                break
        if t == 1:
            aaa.append(li[:i + 1])
            li = li[i + 1:]
            cut()
cut()
aaa.append(li)


ans = 0

for i in range(len(aaa)):
    li = aaa[i]
    n = len(li)
    if n == 1:
        ans += 1
        continue
    li1 = [0]*n
    li2 = [1]*n
    if li[0] < li[1]:
        li1[0] = 1
    else:
        li1[0] = -1
    if li[n-1] < li[n-2]:
        li1[n-1] = 1
    else:
        li1[n-1] = -1
    for i in range(1,n-1):
        if li[i] < li[i-1] and li[i] < li[i+1]:
            li1[i] = 1
        elif li[i] > li[i-1] and li[i] > li[i+1]:
            li1[i] = -1
    a = 1
    for i in range(n):
        if li1[i] == 1:
            a = 1
        elif a > 0:
            a += 1
            li2[i] = a
            if li1[i] == -1:
                a = 0
    a = 1
    for i in range(n-1,-1,-1):
        if li1[i] == 1:
            a = 1
        elif a > 0:
            a += 1
            if li1[i] == 0:
                li2[i] = a
            else:
                li2[i] = max(li2[i],a)
                a = -1

    for i in range(n):
        ans += li2[i]

print(ans)

#A. Fill in the Matrix
nn = int(input())
for _ in range(nn):
    n,m = map(int,input().split())
    if m == 1:
        for _ in range(n+1):
            print(0)
    else:
        if n >= m-1:
            print(m)
            for i in range(m-1):
                li = []
                for j in range(i + 1):
                    li.append(m - i + j - 1)
                for k in range(m - 1 - i):
                    li.append(k)
                print(*li)
            for i in range(n-m+1):
                print(*li)
        else:
            print(n+1)
            for i in range(n):
                li = []
                for j in range(i + 1):
                    li.append(m - i + j - 1)
                for k in range(m - 1 - i):
                    li.append(k)
                print(*li)
