# Assignment #5: 20251009 cs101 Mock Exam寒露第二天

Updated 1651 GMT+8 Oct 9, 2025

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

### E29895: 分解因数

implementation, http://cs101.openjudge.cn/practice/29895/



思路：一开始怕超时，用欧拉筛找素数，再除，写到一半发现简单地一个一个除也不会超时（笑）



代码

n = int(input())
for i in range(2,n+1):
 if n%i == 0:
  print(n//i)
  break



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E29940: 机器猫斗恶龙

greedy, http://cs101.openjudge.cn/practice/29940/



思路：implementation即可，不明白和greedy有何关系



代码
n = int(input())
li = input().split()
a = 0
b = 0
for i in li:
 a += int(i)
 b = min(a,b)
print(-b+1)



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M29917: 牛顿迭代法

implementation, http://cs101.openjudge.cn/practice/29917/



思路：想到函数是什么就几乎做完了



代码
while 1:
 try:
    a = float(input())
    x = 1
    x1 = 1
    b = 0
    while 1:
        x = x1
        x1 = x - (x**2 - a)/(x*2)
        b += 1
        if abs(x-x1)<=10**(-6):
            break
    print(b,end=' ')
    print(f'{x1:.2f}')
 except EOFError:
    break



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M29949: 贪婪的哥布林

greedy, http://cs101.openjudge.cn/practice/29949/


思路：略



代码
n,m = map(int,input().split())
li = []
for i in range(n):
    a,b = map(int,input().split())
    c = a/b
    li.append([c,b])
    li.sort()
d = 0
e = 0
for i in range(n):
    if d+li[n-1-i][1] < m:
        d += li[n-1-i][1]
        e += li[n-1-i][0]*li[n-1-i][1]
    else:
        e += li[n-1-i][0]*(m-d)
        break
print(f'{e:.2f}')



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M29918: 求亲和数

implementation, http://cs101.openjudge.cn/practice/29918/



思路：感觉这题最难，开始复杂度n^2，过不去，想了较长时间才改成n^1.5（虽然最后稍微改一下hh函数就好了，但当时总是想优化主程序......）



代码
def hh(n):
    a = 1
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            a += i
            a += n//i
    if n**0.5 % 1 == 0:
        a -= n**0.5
    return a
n = int(input())
for a in range(1,n+1):
    b = hh(a)
    if n >= b > a and a == hh(b):
        print(f'{a} {b}')



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### T29947:校门外的树又来了（选做）

http://cs101.openjudge.cn/practice/29947/



思路：真的有T吗，感觉比好多M都简单，题目中M<=100,关于M的时间复杂度想多大都行（我的最坏M^3，20ms左右过的），想问一下老师如果m较大怎么办？



代码

l, m = map(int, input().split())
se = set()
for _ in range(m):
    a, b = map(int, input().split())
    ab = 1
    for i in se:
        c,d = i[0],i[1]
        if a >= c and d >= b:
            ab = 0
            break
    if ab == 0:
        continue
    while 1:
        aa = 0
        for i in se:
            c,d = i[0],i[1]
            if a<=c<=b or a<=d<=b:
                aa = 1
                a = min(a,c)
                b = max(b,d)
                break
        if aa == 1:
            se.remove((c,d))
            continue
        else:
            se.add((a,b))
            break
t = 0
for i in se:
    a,b = i[0],i[1]
    t += b-a+1
print(l+1-t)



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>课下练习的，总用时超了几分钟，但有1.5小时是在平板上（无编译器）写的，RE,CE了很多次......





