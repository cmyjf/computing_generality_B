# Assignment #7: 矩阵、队列、贪心

Updated 1315 GMT+8 Oct 21, 2025

2025 fall, Complied by <mark>同学的姓名、院系</mark>



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### M12560: 生存游戏

matrices, http://cs101.openjudge.cn/pctbook/M12560/

思路：



代码
```
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
```





代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/pctbook/M04133/

思路：



代码

```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M02746: 约瑟夫问题

implementation, queue, http://cs101.openjudge.cn/pctbook/M02746/

思路：



代码

```
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M26976:摆动序列

greedy, http://cs101.openjudge.cn/pctbook/M26976/


思路：



代码

```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T26971:分发糖果

greedy, http://cs101.openjudge.cn/pctbook/T26971/

思路：



代码

```
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 1868A. Fill in the Matrix

constructive algorithms, implementation, 1300, https://codeforces.com/problemset/problem/1868/A

思路：



代码
```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





