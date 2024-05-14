# arr = [0, 6, 3, 2, 4, 9, 1]
# k = 10
# n = 6

# # 가능한 구간 중 최대 크기를 구합니다.
# ans = 0

# # 구간을 잡아봅니다.
# sum_val = 0
# j = 0
# for i in range(1, n + 1):
#     # 구간 내 합이 10을 넘지 않을때까지 계속 진행합니다.
#     while j + 1 <= n and sum_val + arr[j + 1] <= k:
#         sum_val += arr[j + 1]
#         j += 1
    
#     # 현재 구간 [i, j]는 
#     # i를 시작점으로 하는
#     # 가장 긴 구간이므로
#     # 구간 크기 중 최댓값을 갱신합니다.
#     ans = max(ans, j - i + 1)

#     # 다음 구간으로 넘어가기 전에
#     # arr[i]에 해당하는 값은 구간에서 제외시킵니다.
#     sum_val -= arr[i]

# # 조건을 만족하는 가장 큰 구간의 크기는
# # [3, 2, 4]로 3이 됩니다.
# print(ans)

n,s = map(int,input().split()) # n 원소 개수 , s 합 이상
arr = list(map(int,input().split()))
ans = 100000000
sum_val = 0
j = 0
for i in range(0, n):
    # 구간 내 합이 s보다 작으면 진행 
    while j < n and sum_val < s:
        sum_val += arr[j]
        j += 1
    # 최대 이동했는데 s가 못됐을때 
    if sum_val < s:
        break
    j-=1
    ans = min(ans, j - i + 1)
    # print("i는",i,"     j는",j,"답은",j - i + 1)
    sum_val -= arr[i]
if ans == 100000000:
    ans = -1
print(ans)