# Assignment #A: 递归、田忌赛马

Updated 2355 GMT+8 Nov 4, 2025

2025 fall, Complied by <mark>翟宇晟 数院</mark>



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### M018160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/pctbook/M18160

思路：



代码

```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### sy134: 全排列III 中等

https://sunnywhy.com/sfbj/4/3/134

思路：



代码

```
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### sy136: 组合II 中等

https://sunnywhy.com/sfbj/4/3/136

给定一个长度为的序列，其中有n个互不相同的正整数，再给定一个正整数k，求从序列中任选k个的所有可能结果。

思路：



代码

```
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### sy137: 组合III 中等

https://sunnywhy.com/sfbj/4/3/137


思路：



代码

```
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M04123: 马走日

dfs, http://cs101.openjudge.cn/pctbook/M04123

思路：



代码

```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/pctbook/T02287

思路：



代码

```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





