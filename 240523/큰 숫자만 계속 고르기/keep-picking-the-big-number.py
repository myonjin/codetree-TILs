import heapq
n,m = map(int,input().split())
arr = list(map(int,input().split()))
hq = []
for a in arr:
    heapq.heappush(hq,-a)
for _ in range(m):
    h = heapq.heappop(hq)
    h += 1
    heapq.heappush(hq,h)
print(-min(hq))