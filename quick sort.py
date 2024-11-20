def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)
n=int(input())
l=list(map(int,input().split()))
ll=quicksort(l)
print(ll)