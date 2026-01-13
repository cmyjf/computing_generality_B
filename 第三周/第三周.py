#E28674
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

#E28691
list0 = input().split()
a = int(list0[0][:2])
b = int(list0[1][:2])
print(a + b)

#M28664
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

#M28678
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

#158B
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

#


