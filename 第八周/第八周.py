#M04147汉诺塔问题(Tower of Hanoi)
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

#M05585: 晶矿的个数
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

#M02786: Pell数列
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

#46. 全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        a = []
        def dfs(li,l):
            if l == 1:
                a.append(li[0])
                ans.append(a[:])
                a.pop()
            else:
                for i in range(l-1):
                    a.append(li[i])
                    dfs(li[:i]+li[i+1:],l-1)
                    a.pop()
                a.append(li[l-1])
                dfs(li[:-1],l-1)
                a.pop()
        dfs(nums,len(nums))
        return ans

#T02754:八皇后
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

#T01958 Strange Towers of Hanoi
li = [1]
for n in range(2,13):
    se = set()
    for i in range(1,n):
        se.add(2*li[i-1]+2**(n-i)-1)
    li.append(min(se))
for i in li:
    print(i)
