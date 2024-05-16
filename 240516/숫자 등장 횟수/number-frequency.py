n,m = map(int,input().split())
arr = list(map(int,input().split()))
num = list(map(int,input().split()))
d = dict()
for i,e in enumerate(arr):
    if e not in d:
        d[e] = 1
    else:
        d[e] += 1
    
for n in num:
    if n in d:
        print(d[n],end=" ")
    else:
        print(0,end=" ")