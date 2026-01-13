#1.1
a = int(input())
if a%4 == 0 and a%100 != 0:
    print('Y')
elif a%100 == 0 and a%400 != 0:
    print('N')
elif a%400 ==0:
    print('Y')
else:
    print('N')

#1.2
a = int(input())
if a % 2 != 0:
    b = c =0
else:
    b = int(a / 2)
    c = int(a // 4 + (a % 4)/2)
print(c, end=' ')
print(b)

#1.3
list1 = input().split()
a = int(list1[0])*int(list1[1])
print(a//2)

#1.4
import math
l = input().split()
n = int(l[0])
m = int(l[1])
a = int(l[2])
b = math.ceil(m/a) * math.ceil(n/a)
print(b)

#1.5
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

#1.6
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

#338013094
list = input().split()
n = int(list[0])
k = int(list[1])
l = int(list[2])
c = int(list[3])
d = int(list[4])
p = int(list[5])
nl = int(list[6])
np = int(list[7])
a = min((l*k)//nl,c*d,p//np)
b = a//n
print(b)

#M01002
#一个超时的代码
def ab(x):
    list0 = []
    for i in x:
        if i == '-':
            continue
        if i == '0' or i == '1':
            list0.append(i)
        elif i == 'A' or i == 'B' or i == 'C' or i == '2':
            list0.append('2')
        elif i == 'D' or i == 'E' or i == 'F' or i == '3':
            list0.append ('3')
        elif i == 'G' or i == 'H' or i == 'I' or i == '4':
            list0.append('4')
        elif i == 'J' or i == 'K' or i == 'L' or i == '5':
            list0.append ('5')
        elif i == 'M' or i == 'N' or i == 'O' or i == '6':
            list0.append('6')
        elif i == 'P' or i == 'R' or i == 'S' or i == '7':
            list0.append('7')
        elif i == 'T' or i == 'U' or i == 'V' or i == '8':
            list0.append('8')
        elif i == 'W' or i == 'X' or i == 'Y' or i == '9':
            list0.append('9')
    result = ''.join(list0)
    return result

n = int(input())
list1 = []
for i in range(n):
    list1.append(ab(input()))
jihe = set(list1)
list2 = list(jihe)
list2.sort()
for i in list2:
    if list1.count(i) > 1:
        ii = str(i)
        ia = ii[:3] + '-' + ii[3:]
        print(ia,end=' ')
        print(list1.count(i))
if len(list1) == len(list2):
    print('No duplicates.')
#AC代码
def ab(x):
    list0 = []
    for i in x:
        if i == '-':
            continue
        if i == '0' or i == '1':
            list0.append(i)
        elif i == 'A' or i == 'B' or i == 'C' or i == '2':
            list0.append('2')
        elif i == 'D' or i == 'E' or i == 'F' or i == '3':
            list0.append ('3')
        elif i == 'G' or i == 'H' or i == 'I' or i == '4':
            list0.append('4')
        elif i == 'J' or i == 'K' or i == 'L' or i == '5':
            list0.append ('5')
        elif i == 'M' or i == 'N' or i == 'O' or i == '6':
            list0.append('6')
        elif i == 'P' or i == 'R' or i == 'S' or i == '7':
            list0.append('7')
        elif i == 'T' or i == 'U' or i == 'V' or i == '8':
            list0.append('8')
        elif i == 'W' or i == 'X' or i == 'Y' or i == '9':
            list0.append('9')
    result = ''.join(list0)
    return result

n = int(input())
list1 = []
for i in range(n):
    list1.append(ab(input()))
word_count = {}
for word in list1:
    word_count[word] =word_count.get(word,0) + 1
list2 =[]
for i in word_count:
    list2.append(i)
list2.sort()
for i in list2:
    if word_count[i] > 1:
        print(f'{i[:3]}-{i[3:]} {word_count[i]}')
if len(word_count) == len(list1):
    print('No duplicates.')

#M19944
n = int(input())
list0 = []
zidian = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
for i in range(n):
    list0.append(input())
for date in list0:
    c = int(date[0:2])
    y = int(date[2:4])
    m = int(date[4:6])
    d = int(date[6:8])
    if m == 1:
        m = 13
        y -= 1
    elif m == 2:
        m = 14
        y -= 1
    if date[2:6] == '0001' or date[2:6] == '0002':
        y = 99
        c -= 1
    w = (y + y//4 + c//4 - 2*c + (26*(m+1))//10 +d - 1) % 7
    print(zidian[w])

#160A
n = int(input())
list0 = input().split()

s = 0
t = 0
a = 0
for i in range(n):
    list0[i] = int(list0[i])
list0.sort(reverse=True)
for i in range(n):
    s += list0[i]
for i in range(n):
    t += list0[i]
    a += 1
    if t > s/2 :
        break
print(a)

#1475A
t = int(input())
l0 = []
for i in range(t):
    l0.append(int(input()))
for n in l0:
    a = 1
    while 2**a <= n:
        if n == 2**a:
            print('NO')
            break
        if 2**a <= n < 2**(a+1):
            print('YES')
        a += 1

