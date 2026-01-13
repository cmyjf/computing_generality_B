# Assignment #D: Mock Exam下元节

Updated 1729 GMT+8 Dec 4, 2025

2025 fall, Complied by <mark>翟宇晟 数院</mark>



>**说明：**
>
>1. Dec⽉考： AC4（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
>2. 解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>3. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. 延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E29945:神秘数字的宇宙旅行 

implementation, http://cs101.openjudge.cn/practice/29945

思路：



代码
```
n = int(input())
while n != 1:
    if n % 2 == 0:
        print(f'{n}/2={n//2}')
        n = n//2
    else:
        print(f'{n}*3+1={n*3+1}')
        n = n*3+1
print('End')
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E29946:删数问题

monotonic stack, greedy, http://cs101.openjudge.cn/practice/29946

思路：



代码

```
li = list(str(input()))
m = len(li)
k = int(input())
ans = [li[0]]
t = 1
while k > 0 and t < m:
    if ans and li[t] < ans[-1]:
        ans.pop()
        k -= 1
    else:
        ans.append(li[t])
        t += 1
if k == 0:
    for i in li[t:]:
        ans.append(i)
else:
    while k>0:
        ans.pop()
        k-=1
while ans and ans[0] == '0':
    ans.remove('0')
if ans:
    for i in ans:
        print(i,end='')
else:
    print(0)
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E30091:缺德的图书馆管理员

greedy, http://cs101.openjudge.cn/practice/30091

思路：



代码

```
l = int(input())
n = int(input())
li = list(map(int,input().split()))
a,b = 0,0
for i in li:
    a = max(a,i,l+1-i)
    b = max(b,min(i,l+1-i))
print(f'{b} {a}')
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M27371:Playfair密码

simulation，string，matrix, http://cs101.openjudge.cn/practice/27371


思路：



代码

```
st = str(input())
li1 = ['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
li2 = [0]*25
li3 = list(st)
ll = []
for i in range(len(li3)):
    if li3[i] =='j':
        li3[i] = 'i'
for i in li3:
    t = 0
    while li1[t] != i:
        t += 1
    if li2[t] == 0:
        ll.append(i)
        li2[t] = 1
for t in range(25):
    if li2[t] == 0:
        ll.append(li1[t])
ma = []
for i in range(5):
    lll = []
    for j in range(i*5,(i+1)*5):
        lll.append(ll[j])
    ma.append(lll)
n = int(input())
for _ in range(n):
    st = list(str(input()))
    li = []
    da = []
    for i in range(len(st)):
        if st[i] == 'j':
            st[i] = 'i'
        if not da:
            da.append(st[i])
        else:
            if st[i] != da[0]:
                da.append(st[i])
                li.append(da)
                da = []
            else:
                if st[i] != 'x':
                    da.append('x')
                    li.append(da)
                    da = [st[i]]
                else:
                    da.append('q')
                    li.append(da)
                    da = [st[i]]
    if da:
        if da[0] == 'x':
            da.append('q')
        else:
            da.append('x')
        li.append(da)
    for tw in li:
        a = ll.index(tw[0])
        b = ll.index(tw[1])
        a1,a2 = a//5,a%5
        b1, b2 = b // 5, b % 5
        if a1 == b1:
            tw[0] = ma[a1][(a2+1)%5]
            tw[1] = ma[b1][(b2 + 1) % 5]
        elif a2==b2:
            tw[0] = ma[(a1+1)%5][a2]
            tw[1] = ma[(b1 + 1) % 5][b2]
        else:
            tw[0] = ma[a1][b2]
            tw[1] = ma[b1][a2]
    for tw in li:
        for i in tw:
            print(i,end='')
    print('')
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T30201:旅行售货商问题

dp,dfs, http://cs101.openjudge.cn/practice/30201

思路：



代码

```
import sys
from array import array
data = list(map(int, sys.stdin.buffer.read().split()))
if not data:
    sys.exit(0)
it = iter(data)
n = next(it)
cost = [[next(it) for _ in range(n)] for _ in range(n)]
INF = 10**9
ALL = (1 << n) - 1
dp = [array('I', [INF]) * n for _ in range(1 << n)]
dp[1][0] = 0 
for mask in range(1 << n):
    if not (mask & 1):
        continue
    row = dp[mask]
    for i in range(n):
        cur = row[i]
        if cur >= INF:
            continue
        for j in range(n):
            if (mask >> j) & 1:
                continue
            nm = mask | (1 << j)
            val = cur + cost[i][j]
            if val < dp[nm][j]:
                dp[nm][j] = val
ans = INF
full = ALL
last_row = dp[full]
for i in range(n):
    v = last_row[i]
    if v < INF:
        cand = v + cost[i][0]
        if cand < ans:
            ans = cand
print(ans)
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T30204:小P的LLM推理加速

greedy, http://cs101.openjudge.cn/practice/30204

思路：



代码

```
n,m = map(int,input().split())
li = []
li1 = []
for _ in range(n):
    a,b = map(int,input().split())
    li.append(a+b)
    li1.append(a)
ans = []
m1 = min(li)
li1.sort()
t = m//m1
for i in range(t+1):
    mm = m - i*m1
    an = i*2
    for j in li1:
        if j <= mm:
            mm = mm - j
            an += 1
        else:
            break
    ans.append(an)
print(max(ans))
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。





