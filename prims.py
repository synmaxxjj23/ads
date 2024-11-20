import heapq
def prims(graph):
    n=len(graph)
    fin_res=[]
    min_heap=[(0,0)]
    visited=[False]*n
    weight=0
    prev=[-1]*n
    while min_heap:
        wt,vertex=heapq.heappop(min_heap)
        if visited[vertex]:
            continue
        visited[vertex]=True
        weight+=wt
        if wt!=0:
            fin_res.append((wt,vertex,prev[vertex]))
        for ver,we in graph[vertex]:
            if not visited[ver]:
                heapq.heappush(min_heap,(we,ver))
                prev[ver]=vertex
    return weight,fin_res
n=int(input())
graph={i:[] for i in range(n)}
m=int(input())
for i in range(m):
    wt,ver1,ver2=map(int,input().split())
    graph[ver1].append((ver2,wt))
    graph[ver2].append((ver1,wt))
weight,min_heap=prims(graph)
print(weight,min_heap)