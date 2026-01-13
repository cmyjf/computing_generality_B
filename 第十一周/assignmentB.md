# Assignment #B: dp

Updated 1448 GMT+8 Nov 18, 2025

2025 fall, Complied by <mark>翟宇晟 数院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：



代码：

```
n = int(input())
li = [1,2]
for i in range(2,n):
    li.append(li[i-2]+li[i-1])
print(li[-1])
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：



代码：

```
n = int(input())
li = [1]
for i in range(1,n):
    s = 1
    for j in range(i):
        s += li[j]
    li.append(s)
print(li[-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M23421:《算法图解》小偷背包问题

dp, http://cs101.openjudge.cn/pctbook/M23421/

思路：



代码：
```
n,b = map(int,input().split())
pr = list(map(int,input().split()))
we = list(map(int,input().split()))
s,m = 0,0
def dp(x,y):
    global s,m
    a = 1
    for i in range(x,n):
        if y+we[i] <= b:
            s += pr[i]
            dp(i+1,y+we[i])
            s -= pr[i]
    if a == 1:
        m = max(m,s)
dp(0,0)
print(m)
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：



代码：

```
n = len(s)
m = 0
le,ri = '',''
for i in range(n):
    j = 0
    for j in range(min(i+1,n-i)):
        if s[i-j] == s[i+j]:
            pass
        else:
            j -= 1
            break
    if 2*j+1 > m:
        m = 2*j+1
        le,ri = i-j,i+j
for i in range(n-1):
    j = 0
    for j in range(min(i+1,n-1-i)):
        if s[i-j] == s[i+j+1]:
            pass
        else:
            j -= 1
            break
    if 2*j+2 > m:
        m = 2*j+1
        le,ri = i-j,i+j+1
return(s[le:ri+1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>







### 474D. Flowers

dp, 1700 https://codeforces.com/problemset/problem/474/D

思路：



代码：

```
t,k = map(int,input().split())
li = [1]*(k-1)+[2]
for i in range(k,10**5+1):
    li.append((li[i-1]+li[i-k])%(10**9+7))
li2 = [0]
ss = 0
for i in range(len(li)):
    ss += li[i]
    ss = ss%(10**9+7)
    li2.append(ss)
for _ in range(t):
    a,b = map(int,input().split())
    print((li2[b]-li2[a-1])%(10**9+7))
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M198.打家劫舍

dp, https://leetcode.cn/problems/house-robber/

思路：



代码：

class Solution:

    def rob(self, nums: List\[int]) -> int:

        if len(nums) == 1:

            return nums\[0]

        li = \[nums\[0],max(nums\[0],nums\[1])]

        for i in range(2,len(nums)):

            li.append(max(li\[i-1],li\[i-2]+nums\[i]))

        return max(li)




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





