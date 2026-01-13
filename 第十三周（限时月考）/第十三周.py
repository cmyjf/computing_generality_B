#T1
n = int(input())
while n != 1:
    if n % 2 == 0:
        print(f'{n}/2={n//2}')
        n = n//2
    else:
        print(f'{n}*3+1={n*3+1}')
        n = n*3+1
print('End')

#T2
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

#T3
l = int(input())
n = int(input())
li = list(map(int,input().split()))
a,b = 0,0
for i in li:
    a = max(a,i,l+1-i)
    b = max(b,min(i,l+1-i))
print(f'{b} {a}')

#T4
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

#T6
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

#T5
