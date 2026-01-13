# Assignment #9: Mock Exam立冬前一天

Updated 1658 GMT+8 Nov 6, 2025

2025 fall, Complied by 翟宇晟同学的姓名、院系数院



>**说明：**
>
>1. Nov⽉考：考完做的。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
>2. 解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>3. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. 延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E29982:一种等价类划分问题

hashing, http://cs101.openjudge.cn/practice/29982

思路：



代码

```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E30086:dance

greedy, http://cs101.openjudge.cn/practice/30086

思路：



代码

```
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
```


代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M25570: 洋葱

matrices, http://cs101.openjudge.cn/practice/25570

思路：



代码

```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M28906:数的划分

dfs, dp, http://cs101.openjudge.cn/practice/28906


思路：



代码

```
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M29896:购物

greedy, http://cs101.openjudge.cn/practice/29896

思路：



代码

```
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
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T25353:排队

greedy, http://cs101.openjudge.cn/practice/25353

思路：花了半天，写出来一个时间复杂度为n^2的代码，超时了...…
最近感冒了，还要准备其他课的考试，这题只能以后有时间再做了......



代码
超时的代码
```
def dp(x):
    t = x
    s = x+1
    while x > 0:
        if abs(li[x-1]-li[t]) <= d:
            if li[x-1] > li[t]:
                s = x
            x -= 1
        else:
            break
    tt = li[t]
    for i in range(t-1,s-2,-1):
        li[i+1] = li[i]
    li[s-1] = tt
n,d = map(int,input().split())
li = []
for i in range(n):
    li.append(int(input()))
for i in range(1,n):
    dp(i)
for i in li:
    print(i)
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。





