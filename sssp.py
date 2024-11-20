import heapq
def djikstra(graph,start):
    n=len(graph)
    visited=[False]*n
    distances=[float('inf') for _ in range(n)]
    distances[start]=0
    prev=[-1]*n
    min_heap=[(0,start)]
    total_dis=0
    while min_heap:
        curr_dist,curr_ver=heapq.heappop(min_heap)
        if visited[curr_ver]:
            continue
        visited[curr_ver]=True
        for ver,dis in graph[curr_ver]:
            if not visited[ver]:
                distance=curr_dist+dis
                if distance<distances[ver]:
                    distances[ver]=distance
                    heapq.heappush(min_heap,(distance,ver))
                    prev[ver]=curr_ver
    return distances

n=int(input())
graph={i:[] for i in range(n)}
m=int(input())
for i in range(m):
    wt,ver1,ver2=map(int,input().split())
    graph[ver1].append((ver2,wt))
    graph[ver2].append((ver1,wt))
start=int(input())
weight=djikstra(graph,start)
print(weight)