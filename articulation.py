from collections import defaultdict

def main():
    v = int(input("Enter the number of vertices: "))
    mat = defaultdict(list)

    e = int(input("Enter the number of edges: "))
    print("Enter the edges for each pair of vertices:")
    for _ in range(e):
        fi, si = map(int, input().split())
        mat[fi].append(si)
        mat[si].append(fi)

    print("Articulation points of the given graph are:")
    find_articulation_points(mat, v)

def find_articulation_points(mat, v):
    for i in range(1, v + 1):
        cnt = 0
        vis = [0] * (v + 1)

        for j in range(1, v + 1):
            if j != i and vis[j] == 0:
                cnt += 1
                dfs(mat, vis, i, j)

        if cnt > 1:
            print(i, end=" ")
    print()

def dfs(adj, vis, check, point):
    vis[point] = 1
    for x in adj[point]:
        if x != check and vis[x] == 0:
            dfs(adj, vis, check, x)

if __name__ == "__main__":
    main()