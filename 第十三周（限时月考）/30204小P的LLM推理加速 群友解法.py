import sys
n,m=map(int,sys.stdin.readline().split())
x=[]
count=0
min_pair=10**10
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    x.append(a)
    if a+b<min_pair:
        min_pair=a+b
x.sort()
i=0
p=0
while i<len(x):
    if x[i]>min_pair/2 or m<x[i]:
        break
    m-=x[i]
    p=x[i]
    count+=1
    i+=1
t=m//min_pair
count+=t*2
m-=t*min_pair
x=x[i:]
i=0
while i<len(x):
    if x[i]>m:
        break
    count+=1
    m-=x[i]
    p=x[i]
    i+=1
if p+m>=min_pair:
    count+=1
print(count)