def search(v,A,low,high,n):
    mid = low + (high-low)//2
    if A[mid] == v:
        return str(mid)
    if A[mid] > v:
        return search(v,A,low,mid-1,mid-low)
    else:
        return search(v,A,mid+1,high,high-mid)

v = int(input())
n = int(input())

numbers = [int(i) for i in input().split()]

print(search(v,numbers,0,len(numbers)-1,len(numbers)))