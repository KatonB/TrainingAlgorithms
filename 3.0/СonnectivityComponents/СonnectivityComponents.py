def dfs(graph, visited, ans, start):
    stack = []
    stack.append(start)
    while stack:
        now = stack.pop()
        if visited[now]:
            continue
        else:
            visited[now] = 1
            ans[start].append(now)
            for elem in graph[now]:
                if not visited[elem]:
                    stack.append(elem)

with open('input.txt', 'r') as File:
    v, e = map(int, File.readline().split())
    #v, e = map(int, input().split())
    graph = [[] for i in range(v+1)]
    visited = [0]*(v+1)
    for line in File:
        vert1, vert2 = map(int, line.split())
        graph[vert1].append(vert2)
        graph[vert2].append(vert1)

count = 0
ans = [[] for i in range(v+1)]
for i in range(1,v+1):
    if visited[i]==0:
        count += 1
        dfs(graph, visited, ans, i)

print(count)
for i in range(len(ans)):
    if len(ans[i])!=0:
        print(len(ans[i]))
        print(' '.join(str(elem) for elem in ans[i]))