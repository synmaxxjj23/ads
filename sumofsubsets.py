l=list(map(int,input().split()))
lll=[]
w=18
def backtrack(ll,count):
    if w==sum(ll):
            lll.append(ll[:])
            return
    if count==len(l):
            return
    backtrack(ll+[l[count]],count+1)
    backtrack(ll,count+1)
backtrack([],0)
print(lll)

    