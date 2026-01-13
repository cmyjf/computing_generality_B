#sy321迷宫最短路径
#dfs
n,m = map(int,input().split())
ma = [['1']*(m+2)]
for _ in range(n):
    ma.append(['1']+input().split()+['1'])
ma.append(['1']*(m+2))
li = []
ans = [1]*10000
def dfs(x,y,d):
    global ans
    if x == n and y == m:
        li.append(f'{x} {y}')
        if len(li) < len(ans):
            ans = li[:]
    if ma[x][y] == '0':
        li.append(f'{x} {y}')
        if d != 1:
            dfs(x-1,y,-1)
        if d != -1:
            dfs(x+1,y,1)
        if d != 2:
            dfs(x,y-1,-2)
        if d != -2:
            dfs(x,y+1,2)
        li.pop()
dfs(1,1,1)
for i in ans:
    print(i)
#bfs
from collections import deque
n,m = map(int,input().split())
ma = [['1']*(m+2)]
for _ in range(n):
    ma.append(['1']+input().split()+['1'])
ma.append(['1']*(m+2))
pre = [[(-1,-1)]*(m+2) for _ in range(n+2)]
def bfs():
    q = deque([(1,1)])
    while q:
        a,b = q.popleft()
        if a == n and b == m:
            break
        if pre[a-1][b] == (-1,-1) and ma[a-1][b] == '0':
            q.append((a-1,b))
            pre[a-1][b] =(a,b)
        if pre[a+1][b] == (-1,-1) and ma[a+1][b] == '0':
            q.append((a+1,b))
            pre[a+1][b] =(a,b)
        if pre[a][b-1] == (-1,-1) and ma[a][b-1] == '0':
            q.append((a,b-1))
            pre[a][b-1] =(a,b)
        if pre[a][b+1] == (-1,-1) and ma[a][b+1] == '0':
            q.append((a,b+1))
            pre[a][b+1] =(a,b)
bfs()
path = [(n,m)]
while 1:
    x,y = path[-1]
    path.append(pre[x][y])
    if pre[x][y] == (1,1):
        break
path.reverse()
for i in path:
    print(f'{i[0]} {i[1]}')

#sy324多终点迷宫问题
from collections import deque
n,m = map(int,input().split())
ma = []
for _ in range(n):
    ma.append(input().split())
ans = [[-1]*m for _ in range(n)]
ans[0][0] = 0
way = {(0,1),(0,-1),(1,0),(-1,0)}
def bfs():
    q = deque([(0,0)])
    while q:
        a,b = q.popleft()
        for (x,y) in way:
            aa = a+x
            bb = b+y
            if 0 <= aa < n and 0 <= bb < m and ma[aa][bb] == '0' and ans[aa][bb] == -1:
                ans[aa][bb] = ans[a][b] + 1
                q.append((aa,bb))
bfs()
for i in ans:
    print(*i)

#M02945: 拦截导弹
k = int(input())
li = list(map(int,input().split()))
dp = [1]*k
for i in range(k):
    a = 1
    for j in range(i):
        if a <= dp[j] and li[i] <= li[j]:
            a = dp[j]+1
    dp[i] = a
print(max(dp))

#189A. Cut Ribbon
n,a,b,c = map(int,input().split())
li = [0]+[-1]*(n)
for i in range(1,n+1):
        ta,tb,tc = -1,-1,-1
        if i-a >= 0 and li[i-a] != -1:
            ta = li[i-a]+1
        if i-b >= 0 and li[i-b] != -1:
            tb = li[i-b]+1
        if i-c >= 0 and li[i-c] != -1:
            tc = li[i-c]+1
        li[i] = max(ta,tb,tc)
print(li[n])

#01384:Piggy-Bank
T = int(input())
for _ in range(T):
    E,F = map(int,input().split())
    l = F-E
    n = int(input())
    da = []
    for _ in range(n):
        da.append(list(map(int,input().split())))
    li = [0]+[-1]*l
    for i in range(1,l+1):
        ans = []
        for j in da:
            if i-j[1] >= 0 and li[i-j[1]] != -1:
                ans.append(j[0]+li[i-j[1]])
        if ans:
            li[i] = min(ans)
    if li[l] == -1:
        print("This is impossible.")
    else:
        print(f"The minimum amount of money in the piggy-bank is {li[l]}.")

#M02766: 最大子矩阵
n = int(input())
li = []
while 1:
    try:
        a = input().split()
        for i in a:
            li.append(int(i))
    except:
        break
ma = []
ans = -127
for i in range(n):
    ma.append(li[i*n:(1+i)*n])
def ka(li):
    ans = -127
    s = 0
    for i in li:
        s = max(s+i,i)
        ans = max(s,ans)
    return ans
ans = -127
for i in range(n):
    li = []
    for j in range(n):
        li.append(ma[i][j])
        ans = max(ans,ka(li))
    for j in range(1,n-i):
        for k in range(n):
            li[k] += ma[i+j][k]
        ans = max(ans,ka(li))
print(ans)