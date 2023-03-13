v, e = map(int, input().split())
graph = [[] for i in range(v+1)]
visited = [0]*(v+1)
ans = []
def dfs(graph, visited, now):
    visited[now] = 1
    #print(visited, graph[now])
    ans.append(now)
    for elem in graph[now]:
        if not visited[elem]:
            dfs(graph, visited, elem)

for i in range(1, e+1):
    vert1, vert2 = map(int, input().split())
    graph[vert1].append(vert2)
    graph[vert2].append(vert1)

dfs(graph, visited, 1)
#print(graph)
ans = sorted(ans)
print(len(ans))
print(' '.join(str(elem) for elem in ans))