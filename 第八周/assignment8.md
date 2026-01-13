# Assignment #8: 递归

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

### M04147汉诺塔问题(Tower of Hanoi)

dfs, http://cs101.openjudge.cn/pctbook/M04147

思路：



代码

```
li = input().split()
n = int(li[0])
li = li[1:]
def dfs(n,m1,m2):
    if n == 1:
        print(f'{n}:{li[m1]}->{li[m2]}')
    else:
        dfs(n-1,m1,3-m1-m2)
        print(f'{n}:{li[m1]}->{li[m2]}')
        dfs(n-1,3-m1-m2,m2)

dfs(n,0,2)
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M05585: 晶矿的个数

matrices, dfs similar, http://cs101.openjudge.cn/pctbook/M05585

思路：



代码

```
def dfs(a,b,c):
    if ma[min(max(a,0),m-1)][min(max(b,0),m-1)] == c:
        ma[min(max(a,0),m-1)][min(max(b,0),m-1)] = '#'
        dfs(a,b-1,c)
        dfs(a,b+1,c)
        dfs(a-1,b,c)
        dfs(a+1,b,c)

n = int(input())
for _ in range(n):
    red,black = 0,0
    m = int(input())
    ma = []
    for _ in range(m):
        st = input()
        li = []
        for i in range(m):
            li.append(st[i])
        ma.append(li)
    for i in range(m):
        for j in range(m):
            if ma[i][j] == 'r':
                red += 1
                dfs(i,j,'r')
            elif ma[i][j] == 'b':
                black += 1
                dfs(i,j,'b')
    print(f'{red} {black}')
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M02786: Pell数列

dfs, dp, http://cs101.openjudge.cn/pctbook/M02786/

思路：



代码

```
li = [1,2]
a = 2
while True:
    li.append((2*li[a-1]+li[a-2])%32767)
    if li[a-1] == li[0] and li[a] == li[1]:
        break
    a += 1

n = int(input())
for _ in range(n):
    k = int(input())
    k = (k-1)%(a-1)
    print(li[k])
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M46.全排列

backtracking, https://leetcode.cn/problems/permutations/


思路：



代码

class Solution:

    def permute(self, nums: List\[int]) -> List\[List\[int]]:

        ans = \[]

        a = \[]

        def dfs(li,l):

            if l == 1:

                a.append(li\[0])

                ans.append(a\[:])

                a.pop()

            else:

                for i in range(l-1):

                    a.append(li\[i])

                    dfs(li\[:i]+li\[i+1:],l-1)

                    a.pop()

                a.append(li\[l-1])

                dfs(li\[:-1],l-1)

                a.pop()

        dfs(nums,len(nums))

        return ans



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/pctbook/T02754

思路：



代码

```
from itertools import permutations
li = [1,2,3,4,5,6,7,8]
lii = permutations(li)
liii = []
for a in lii:
    b = set()
    c = set()
    t = 1
    for i in range(8):
        if i+a[i] in b:
            t = 0
            break
        else:
            b.add(i+a[i])
        if i-a[i] in c:
            t = 0
            break
        else:
            c.add(i-a[i])
    if t==1:
        liii.append(a)

n = int(input())
for i in range(n):
    m = int(input())
    for i in liii[m-1]:
        print(i,end='')
    print('')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T01958 Strange Towers of Hanoi

http://cs101.openjudge.cn/practice/01958/

思路：



代码

```
li = [1]
for n in range(2,13):
    se = set()
    for i in range(1,n):
        se.add(2*li[i-1]+2**(n-i)-1)
    li.append(min(se))
for i in li:
    print(i)
```




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





