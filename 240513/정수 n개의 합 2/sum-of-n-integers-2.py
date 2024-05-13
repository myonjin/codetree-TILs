n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr_sum = arr[:]
max_sum = 0

for i in range(1,n):
    arr_sum[i] = arr_sum[i-1] + arr_sum[i] 

for i in range(n-k+1):
     
    if max_sum <= (arr_sum[i+k-1] - arr_sum[i] + arr[i]):
        max_sum = arr_sum[i+k-1] - arr_sum[i] + arr[i]
print(max_sum)