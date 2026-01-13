#M18160:最大连通域面积
def dfs(x,y):
    if ma[x][y] == '.':
        return 0
    else:
        ans = 1
        ma[x][y] = '.'
        ans += dfs(max(0,x-1),y)
        ans += dfs(min(n-1,x+1), y)
        ans += dfs(x,max(0,y-1))
        ans += dfs(x,min(m-1,y+1))
        ans += dfs(max(0,x-1),min(m-1,y+1))
        ans += dfs(min(n-1,x+1), max(0,y-1))
        ans += dfs(max(0,x-1),max(0,y-1))
        ans += dfs(min(n-1,x+1),min(m-1,y+1))
    return ans

t = int(input())
li = []
for _ in range(t):
    n,m = map(int,input().split())
    ma = []
    for _ in range(n):
        a = input()
        b = []
        for i in a:
            b.append(i)
        ma.append(b)
    ans = 0
    for x in range(n):
        for y in range(m):
            ans = max(ans,dfs(x,y))
    li.append(ans)
for ans in li:
    print(ans)

#sy134: 全排列III 中等
from itertools import permutations
n = input().split()
li = list(map(int,input().split()))
a = permutations(li)
a = set(a)
a = list(a)
a.sort()
for i in a:
    for j in range(len(i)-1):
        print(i[j],end=' ')
    print(i[-1])

#sy136: 组合II 中等
n,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
a = []
ans = []
def dfs(li,l,p):
    if l < k-p:
        pass
    elif p == k:
        for i in range(l):
            a.append(li[i])
            ans.append(a[:])
            a.pop()
    else:
        for i in range(l-1):
            a.append(li[i])
            dfs(li[i+1:], l-1-i,p+1)
            a.pop()
dfs(li,n,1)
for i in ans:
    for j in range(len(i)-1):
        print(i[j],end=' ')
    print(i[-1])

#sy137: 组合III 中等
n,k = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
a = []
ans = []
def dfs(li,l,p):
    if l < k-p:
        pass
    elif p == k:
        for i in range(l):
            a.append(li[i])
            ans.append(a[:])
            a.pop()
    else:
        for i in range(l-1):
            a.append(li[i])
            dfs(li[i+1:], l-1-i,p+1)
            a.pop()
dfs(li,n,1)
dic = {}
tt = 0
for i in ans:
    t = 1
    if i not in dic.values():
        dic[tt] = i
        tt += 1
ans.sort()
for i in range(len(dic)):
    i = dic[i]
    for j in range(len(i)-1):
        print(i[j],end=' ')
    print(i[-1])

#M04123: 马走日
t = int(input())
ans = 0
def dfs(x,y,c):
    global ans
    if ma[x][y] == 1:
        pass
    elif c == n*m:
        ans += 1
    else:
        ma[x][y] = 1
        if x-1 >= 0 and y-2 >= 0:
            dfs(x-1,y-2,c+1)
        if x-2 >= 0 and y-1 >= 0:
            dfs(x-2,y-1,c+1)
        if x+1 < n and y+2 < m:
            dfs(x+1,y+2,c+1)
        if x+2 < n and y+1 < m:
            dfs(x+2,y+1,c+1)
        if x+1 < n and y-2 >= 0:
            dfs(x+1,y-2,c+1)
        if x+2 < n and y-1 >= 0:
            dfs(x+2,y-1,c+1)
        if x-1 >= 0 and y+2 < m:
            dfs(x-1,y+2,c+1)
        if x-2 >= 0 and y+1 < m:
            dfs(x-2,y+1,c+1)
        ma[x][y] = 0
for _ in range(t):
    n,m,x,y = map(int,input().split())
    ma = [[0]*m for _ in range(n)]
    ans = 0
    dfs(x,y,1)
    print(ans)

#T02287: Tian Ji -- The Horse Racing
from collections import deque
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        li1 = list(map(int,input().split()))
        li2 = list(map(int,input().split()))
        li1.sort()
        li2.sort()
        ans = 0
        de1 = deque(li1)
        de2 = deque(li2)
        while de1:
            if de1[-1] > de2[-1]:
                de1.pop()
                de2.pop()
                ans += 1
            elif de1[-1] < de2[-1]:
                de1.popleft()
                de2.pop()
                ans -= 1
            else:
                if de1[0] < de2[0]:
                    de1.popleft()
                    de2.pop()
                    ans -= 1
                elif de1[0] > de2[0]:
                    de1.popleft()
                    de2.popleft()
                    ans += 1
                else:
                    if de1[0] == de2[-1]:
                        break
                    else:
                        ans -= 1
                        de1.popleft()
                        de2.pop()
        print(ans*200)








