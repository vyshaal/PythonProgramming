t = int(input())

inp = []
while t > 0:
    t -= 1
    inp.insert(len(inp),int(input()))

n = max(inp)
arr = []
arr.insert(0,0)
arr.insert(1,1)
arr.insert(2,2)
arr.insert(3,4)

for i in range(4,n+1):
    arr.insert(i,arr[i-1]+arr[i-2]+arr[i-3])

for num in inp:
    print(str(arr[num]))