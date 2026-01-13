#E29982:一种等价类划分问题
def hh(x):
    y = x//1000
    s = y
    x = x-y*1000

    y = x//100
    s += y
    x = x-y*100

    y = x//10
    s += y
    x = x-y*10

    s += x
    return s

m,n,k = map(int,input().split(','))
dic = {}
mm = 0
for i in range(m+1,n):
    s = hh(i)
    if s%k == 0:
        if s/k in dic:
            dic[s/k].append(i)
        else:
            dic[s/k] = [i]
            mm = max(mm,s//k)
for j in range(1,mm+1):
    if j in dic:
        for i in range(len(dic[j])-1):
            print(dic[j][i],end=',')
        print(dic[j][len(dic[j])-1])

#E30086:dance
n,d = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
p = 1
for i in range(n):
    if abs(li[2*i]-li[2*i+1])>d:
        p = 0
        break
if p == 1:
    print('Yes')
else:
    print('No')

#M25570: 洋葱
n = int(input())
ma = []
for i in range(n):
    ma.append(list(map(int,input().split())))
m = 0
for i in range((n+1)//2):
    s = 0
    if i == (n-1)/2:
        s = ma[i][i]
    else:
        for j in range(i,n-i):
            s += ma[i][j]
            s += ma[n-i-1][j]
        for j in range(i+1,n-i-1):
            s += ma[j][i]
            s += ma[j][n-i-1]
    m = max(s,m)

print(m)

#M28906:数的划分
#法一
def dfs(n,k):
    if k == 1:
        return 1
    else:
        s = 0
        for i in range(n//k+1):
            s += dfs(n-k*i,k-1)
        return s
n,k = map(int,input().split())
print(dfs(n-k,k))

#法二
def dfs(n,k):
    if k == 1:
        return 1
    else:
        s = 0
        for i in range(1,n//k+1):
            s += dfs(n-i-(k-1)*(i-1),k-1)
        return s
n,k = map(int,input().split())
print(dfs(n,k))

#M29896:购物
x,n = map(int,input().split())
li = list(map(int,input().split()))
li.sort(reverse=True)
if li[-1] != 1:
    print(-1)
else:
    a = 0
    s = 0
    for i in range(1,x+1):
        if i>s:
            for j in li:
                if j <= i:
                    s += j
                    a += 1
                    break
    print(a)

#25353:排队


