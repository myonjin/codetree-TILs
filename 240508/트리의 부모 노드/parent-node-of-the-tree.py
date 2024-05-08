N = int(input())
edges = [ [] for _ in range(N+1)]
visited = [False] * (N+1)
parents = [0]*(N+1)
for _ in range(N-1):
    # a,b=list(map(int,input().split()))
    a,b=list(map(int,input().split()))
    edges[a].append(b)
    edges[b].append(a)


def tree(x):

    for y in edges[x]:
        if visited[y] == False:
            visited[y] = True
            parents[y] = x
            tree(y)
visited[1]=True
tree(1)
# print(parents)
parents.pop(0)
parents.pop(0)
for i in parents:
    print(i)