# Assignment #3: 语法练习

Updated 1440 GMT+8 Sep 23, 2025

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

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/pctbook/E28674/



思路：较快做完，因上课前做的，不知道ord()和chr()函数导致手打了两个很长的字典……



代码
k = int(input())%26
dict0 = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
dict1 = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
word = input()
decode = []
for abc in word:
    if abc in dict0:
        t = (dict0[abc] - k)%26
        if t == 0:
            t = 26
        decode.append(dict1[t])
    else:
        ab = abc.lower()
        t = (dict0[ab] - k) % 26
        if t == 0:
            t = 26
        decode.append(dict1[t].upper())
print(''.join(decode))




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/pctbook/E28691/



思路：



代码
list0 = input().split()
a = int(list0[0][:2])
b = int(list0[1][:2])
print(a + b)



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M28664: 验证身份证号 

http://cs101.openjudge.cn/pctbook/M28664/



思路：



代码
n = int(input())
list0 = []
dict0 = {1:7,2:9,3:10,4:5,5:8,6:4,7:2,8:1,9:6,10:3,11:7,12:9,13:10,14:5,15:8,16:4,17:2}
dict1 = {'1':0,'0':1,'X':2,'9':3,'8':4,'7':5,'6':6,'5':7,'4':8,'3':9,'2':10}
for i in range(n):
    list0.append(input())
for ab in list0:
    s = 0
    for i in range(17):
        c = int(ab[i])
        s += c*dict0[i+1]
    d = ab[17]
    if s%11 == dict1[d]:
        print('YES')
    else:
        print('NO')


代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M28678: 角谷猜想

http://cs101.openjudge.cn/pctbook/M28678/


思路：



代码
n = int(input())
while n != 1:
    if n % 2 == 0:
        print(f'{n}/2={n//2}')
        n = n//2
    else:
        print(f'{n}*3+1={n*3+1}')
        n = n*3+1
print('End')

#M28700
n = input()
l = []
if n > 'A':
    for i in n:
        l.append(i)
    l.append(1)
    s = 0
    while l != [1]:
        if (l[0],l[1]) == ('C','D'):
            s += 400
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('C', 'M'):
            s += 900
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('X', 'L'):
            s += 40
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('X', 'C'):
            s += 90
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('I', 'V'):
            s += 4
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('I', 'X'):
            s += 9
            del l[0]
            del l[0]
        elif l[0] == 'I':
            s += 1
            del l[0]
        elif l[0] == 'V':
            s += 5
            del l[0]
        elif l[0] == 'X':
            s += 10
            del l[0]
        elif l[0] == 'L':
            s += 50
            del l[0]
        elif l[0] == 'C':
            s += 100
            del l[0]
        elif l[0] == 'D':
            s += 500
            del l[0]
        elif l[0] == 'M':
            s += 1000
            del l[0]
    print(s)
else:
    n = int(n)
    l = []
    while n:
        if n >= 1000:
            l.append('M')
            n -= 1000
        elif n >= 900:
            l.append('CM')
            n -= 900
        elif n >= 500:
            l.append('D')
            n -= 500
        elif n >= 400:
            l.append('CD')
            n -= 400
        elif n >= 100:
            l.append('C')
            n -= 100
        elif n >= 90:
            l.append('XC')
            n -= 90
        elif n >= 50:
            l.append('L')
            n -= 50
        elif n >= 40:
            l.append('XL')
            n -= 40
        elif n >= 10:
            l.append('X')
            n -= 10
        elif n >= 9:
            l.append('IX')
            n -= 9
        elif n >= 5:
            l.append('V')
            n -= 5
        elif n >= 4:
            l.append('IV')
            n -= 4
        else:
            l.append('I')
            n -= 1
    print(''.join(l))




代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/pctbook/M28700/



思路：较快做完，if,elif要写吐了，写到一半发现可以用字典，但想想都写了一半了，所以用if,elif写完了……
看了题解，里面转化为减法的想法比我想的更精妙




代码

n = input()
l = []
if n > 'A':
    for i in n:
        l.append(i)
    l.append(1)
    s = 0
    while l != [1]:
        if (l[0],l[1]) == ('C','D'):
            s += 400
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('C', 'M'):
            s += 900
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('X', 'L'):
            s += 40
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('X', 'C'):
            s += 90
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('I', 'V'):
            s += 4
            del l[0]
            del l[0]
        elif (l[0], l[1]) == ('I', 'X'):
            s += 9
            del l[0]
            del l[0]
        elif l[0] == 'I':
            s += 1
            del l[0]
        elif l[0] == 'V':
            s += 5
            del l[0]
        elif l[0] == 'X':
            s += 10
            del l[0]
        elif l[0] == 'L':
            s += 50
            del l[0]
        elif l[0] == 'C':
            s += 100
            del l[0]
        elif l[0] == 'D':
            s += 500
            del l[0]
        elif l[0] == 'M':
            s += 1000
            del l[0]
    print(s)
else:
    n = int(n)
    l = []
    while n:
        if n >= 1000:
            l.append('M')
            n -= 1000
        elif n >= 900:
            l.append('CM')
            n -= 900
        elif n >= 500:
            l.append('D')
            n -= 500
        elif n >= 400:
            l.append('CD')
            n -= 400
        elif n >= 100:
            l.append('C')
            n -= 100
        elif n >= 90:
            l.append('XC')
            n -= 90
        elif n >= 50:
            l.append('L')
            n -= 50
        elif n >= 40:
            l.append('XL')
            n -= 40
        elif n >= 10:
            l.append('X')
            n -= 10
        elif n >= 9:
            l.append('IX')
            n -= 9
        elif n >= 5:
            l.append('V')
            n -= 5
        elif n >= 4:
            l.append('IV')
            n -= 4
        else:
            l.append('I')
            n -= 1
    print(''.join(l))


代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### 158B. Taxi

*special problem, greedy, implementation, 1100,  https://codeforces.com/problemset/problem/158/B



思路：



代码
import math
n = int(input())
l = input().split()
a,b,c,d = 0,0,0,0
for i in l:
    if i == '1':
        a += 1
    elif i == '2':
        b += 1
    elif i == '3':
        c += 1
    elif i == '4':
        d += 1
print(d+c+b//2+b%2+max(0,math.ceil((a-c-2*(b%2))/4)))



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2025fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>





