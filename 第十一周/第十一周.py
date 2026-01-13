#LuoguP1255 数楼梯
n = int(input())
li = [1,2]
for i in range(2,n):
    li.append(li[i-2]+li[i-1])
print(li[-1])

#27528: 跳台阶
n = int(input())
li = [1]
for i in range(1,n):
    s = 1
    for j in range(i):
        s += li[j]
    li.append(s)
print(li[-1])

#M23421:《算法图解》小偷背包问题
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

#M5.最长回文子串
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

#474D. Flowers
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

#M198.打家劫舍
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        li = [nums[0],max(nums[0],nums[1])]
        for i in range(2,len(nums)):
            li.append(max(li[i-1],li[i-2]+nums[i]))
        return max(li)