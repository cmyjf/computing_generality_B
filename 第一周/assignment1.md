# Assignment #1: 自主学习

Updated 1427 GMT+8 Sep 9, 2025

2025 fall, Complied by ==翟宇晟 数院==



**作业的各项评分细则及对应的得分**

| 标准                                 | 等级                                                         | 得分 |
| ------------------------------------ | ------------------------------------------------------------ | ---- |
| 按时提交                             | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分  | 1 分 |
| 源码、耗时（可选）、解题思路（可选） | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于2个：0分 | 1 分 |
| AC代码截图                           | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于：0分 | 1 分 |
| 清晰头像、PDF文件、MD/DOC附件        | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
| 学习总结和个人收获                   | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分 | 1 分 |
| 总得分： 5                           | 总分满分：5分                                                |      |

>
>
>
>**说明：**
>
>1. **解题与记录：**
>
>   对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. **课程平台：**课程网站位于Canvas平台（https://pku.instructure.com ）。该平台将在<mark>第2周</mark>选课结束后正式启用。在平台启用前，请先完成作业并将作业妥善保存。待Canvas平台激活后，再上传你的作业。
>
>3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
>4. **延迟提交：****如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E02733: 判断闰年

http://cs101.openjudge.cn/pctbook/E02733/



思路：
很快做完


代码

a = int(input())
if a%4 == 0 and a%100 != 0:
    print('Y')
elif a%100 == 0 and a%400 != 0:
    print('N')
elif a%400 ==0:
    print('Y')
else:
    print('N')



代码运行截图 ==（至少包含有"Accepted"）==
image.png





### E02750: 鸡兔同笼

http://cs101.openjudge.cn/pctbook/E02750/



思路：
很快做完


代码
a = int(input())
if a % 2 != 0:
    b = c =0
else:
    b = int(a / 2)
    c = int(a // 4 + (a % 4)/2)
print(c, end=' ')
print(b)



代码运行截图 ==（至少包含有"Accepted"）==
image.png




### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A



思路：
很快做完
学会了如何在一行中输入多个数据



代码
list1 = input().split()
a = int(list1[0])*int(list1[1])
print(a//2)



代码运行截图 ==（至少包含有"Accepted"）==

image.png



### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：
很快做完
学会了math.ceil()



代码
import math
l = input().split()
n = int(l[0])
m = int(l[1])
a = int(l[2])
b = math.ceil(m/a) * math.ceil(n/a)
print(b)



代码运行截图 ==（至少包含有"Accepted"）==

image.png



### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：
很快做完


代码
list = []
for i in range(2):
    list.append(input())
a = list[0].lower()
b = list[1].lower()
if a > b:
    print(1)
elif a < b:
    print(-1)
else:
    print(0)



代码运行截图 ==（至少包含有"Accepted"）==

image.png



### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：
很快做完
学会了怎么多行输入，且同时在一行中输入多个数据


代码

n = int(input())
list = []
for i in range(n):
    list.append(input().split())
a = 0
for i in range(n):
    if int(list[i][0])+int(list[i][1])+int(list[i][2])>= 2:
        a += 1
print(a)

#E03143
list = []
for i in range(2,2000):
    for j in range(2,i):
        if i%j==0:
            break
        if j == i-1:
            list.append(i)

x = int(input())
if x < 6 or x%2 == 1:
    print('Error!')
else:
    for i in list :
        if x-i in list and i <= x/2:
            print(f'{x}={i}+{x-i}')



代码运行截图 ==（至少包含有"Accepted"）==
image.png




## 2. 学习总结和收获
code forces上所有ac合集
image.png


其他做题：
9.11
O.2   E03143
很快完成
学会了print(f’{ }…’)的用法

C.1   151A
很快完成

O.3   M01002
包括学习过程，约3h完成，期间经历多次runtime error，WA和超时
收获很大，掌握了操作列表的多种方式和利用字典降低计数的时间复杂度，最重要的是认识了复杂度的重要性
感谢马炫钦同学和陈子良同学的指导及闫老师提供的题目测试数据



9.12
O.4   M19944
较快完成（因读错题浪费了一些时间）

C.2   160A
很快完成
了解了用sort()排序字符串形式的数字时，按字典序



9.13
C.3   1475A
很快完成



