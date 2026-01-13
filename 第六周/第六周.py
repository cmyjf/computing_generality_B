#M18211: 军备竞赛
p = int(input())
n = 0
m = 0
li = list(map(int,input().split()))
li.sort()
le = 0
ri = len(li)-1
while le <= ri:
    if p >= li[le]:
        p -= li[le]
        le += 1
        n += 1
    else:
        if n == 0:
            break
        else:
            n -= 1
            p += li[ri]
            ri -= 1
    m = max(m,n)
print(m)

#M21554: 排队做实验
n = int(input())
t = 0
li = list(map(int,input().split()))
for i in range(len(li)):
    li[i] = (li[i],i+1)
li.sort()
for i in li:
    print(i[1],end=' ')
print('')
for i in range(len(li)):
    t += li[i][0]*(n-1-i)
print(f'{t/n:.2f}')

#E23555:节省存储的矩阵乘法
n,m1,m2 = map(int,input().split())
ma1 = {}
ma2 = {}
ma = []
for _ in range(m1):
    x, y, a = map(int, input().split())
    ma1[(x,y)] = a
for _ in range(m2):
    x, y, a = map(int, input().split())
    ma2[(x,y)] = a
for x in range(n):
    for y in range(n):
        s = 0
        for i in range(n):
            if (x,i) in ma1 and (i,y) in ma2:
                s += ma1[(x,i)]*ma2[(i,y)]
        if s != 0:
            ma.append(f'{x} {y} {s}')
for i in ma:
    print(i)


#M12558: 岛屿周⻓
n,m = map(int,input().split())
ma = [['0']*(m+2)]
for i in range(n):
    li = input().split()
    ma.append(['0']+li+['0'])
ma.append(['0']*(m+2))
def hhh(a,b):
    l = 0
    ij = [(-1,0),(1,0),(0,1),(0,-1)]
    for (i,j) in ij:
            if ma[a+i][b+j] == '0':
               l += 1
    return l
ll = 0
for a in range(1,n+1):
    for b in range(1,m+1):
        if ma[a][b] == '1':
            ll += hhh(a,b)
print(ll)

#M01328: Radar Installation
anss = []
while 1:
    li0 = input().split()
    n = int(li0[0])
    d = float(li0[1])
    if n == d == 0:
        break
    ans = 0
    li = []
    for _ in range(n):
        x,y = map(int,input().split())
        if y > d:
            ans = -1
        else:
            a = (d**2-y**2)**0.5
            li.append((x-a,x+a))
    if ans == -1:
        anss.append(-1)
    else:
        li.sort()
        i = 0
        rm = li[i][1]
        ans = 1
        while i<len(li):
            l,r = li[i][0],li[i][1]
            if r < rm:
                rm = r
            if l > rm:
                ans += 1
                rm = r
            i += 1
        anss.append(ans)
    _ = input()
for i in range(len(anss)):
    print(f'Case {i+1}: {anss[i]}')

#545C. Woodcutters
#贪心
n = int(input())
ans = 0
li = []
xm = float('-inf')
for _ in range(n):
    li.append(list(map(int,input().split())))
li.append([float('inf'),0])
for i in range(n):
    if li[i][0]-li[i][1] > xm:
        ans += 1
        xm = li[i][0]
    elif li[i][0]+li[i][1] >= li[i+1][0]:
        xm = li[i][0]
    else:
        ans += 1
        xm = li[i][0]+li[i][1]
print(ans)
#搜索+递归
n = int(input())
ans = 0
li = []
xm = -10**9-1
for _ in range(n):
    li.append(list(map(int,input().split())))
li.append([2*10**9+1,0])
def able_to_right(x):
    if li[x][0]+li[x][1] < li[x+1][0]-li[x+1][1]:
        return True
    elif li[x][0]+li[x][1] < li[x+1][0]:
        if li[x][0] >= li[x+1][0]-li[x+1][1]:
            return True
        else:
            return able_to_right(x+1)
for i in range(n):
    x,h = li[i][0],li[i][1]
    if i == n-1:
        ans += 1
    elif x-h > xm:
        ans += 1
        xm = x
    elif x+h >= li[i+1][0]:
        xm = x
    elif x+h+li[i+1][1]<li[i+1][0]:
        xm = x+h
        ans += 1
    elif x+li[i+1][1]>=li[i+1][0]:
        ans += 1
        xm = x+h
    elif able_to_right(i+1):
        xm = x
        ans += 1
    else:
        xm = x
print(ans)