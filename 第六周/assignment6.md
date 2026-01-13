# Assignment #6: 矩阵、贪心

Updated 1432 GMT+8 Oct 14, 2025

2025 fall, Complied by <mark>翟宇晟 数院</mark>



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

### M18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/pctbook/M18211



思路：



代码

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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M21554: 排队做实验

greedy, http://cs101.openjudge.cn/pctbook/M21554/



思路：



代码
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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/pctbook/E23555



思路：



代码
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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/pctbook/M12558


思路：



代码
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


代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/



思路：



代码
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


代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C



思路：用时50mins写了一个能AC，但很丑（贪心+搜索+递归，最坏复杂度n^2）的代码，后来意识到可以非常贪，重写了一个复杂度n的代码，但两个代码前者400ms，后者300ms，看来数据没有特别坏的情况



代码
法一：
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

法二：
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




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





