t = int(input())

while t>0:
    t -= 1
    n,k = map(int,input().split())
    arrival_times = [num for num in map(int,input().split())]
    early_students = [num for num in arrival_times if num <= 0]
    if len(early_students) >= k:
        print("NO")
    else:
        print("YES")
