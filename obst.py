def obst(p,q,n):
    w=[[0]*(n+1) for _ in range(n+1)]
    c=[[0]*(n+1) for _ in range(n+1)]
    r=[[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        w[i][i]=q[i]
        c[i][i]=0
        r[i][i]=0
    for length in range(1,n+1):
        for i in range(n-length+1):
            j=i+length
            w[i][j]=w[i][j-1]+p[j]+q[j]
            c[i][j]=float('inf')
            for k in range(i+1,j+1):
                cost=c[i][k-1]+c[k][j]+w[i][j]
                if cost<c[i][j]:
                    c[i][j]=cost
                    r[i][j]=k
        print(f"w[{i}][{j}]={w[i][j]:.2f} , c[{i}][{j}]={c[i][j]:.2f} ,r[{i}][{j}]={r[i][j]}")
    print("min cose:",c[0][n])
n=int(input())
p=[0]*(n+1)
q=[0]*(n+1)
for i in range(1,n+1):
    p[i]=float(input())
for j in range(n+1):
    q[j]=float(input())
obst(p,q,n)
                