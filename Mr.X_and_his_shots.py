def bst(x,A,low,high):
    mid = int(low + (high-low)/2)
    if x < A[low]:
        return 0
    if A[mid] == x:
        return mid
    else:
        if A[mid] < x < A[mid+1]:
            return mid
        elif x < A[mid+1]:
            return bst(x,A,low,mid)
        else:
            return bst(x,A,mid+1,high)

# A = [1,2,4,6,8,10]
# low = 0
# high = len(A)-1
# x = 9
# print(bst(x,A,low,high))
n,m = map(int,input().split())

player_shot = []
while n > 0:
    n -= 1
    a,b = map(int,input().split())
    player_shot.append((a,b))

player_shot = sorted(player_shot)

player_shot_a = [a for a,b in player_shot]
player_shot_b = [b for a,b in player_shot]

fielder_range = []
count = 0
while m > 0:
    m -= 1
    a,b = map(int,input().split())
    fielder_range.append((a,b))
    lower_bound = bst(a, player_shot_a, 0, len(player_shot_b) - 1) + 1
    other_lower = bst(a, player_shot_b, 0, len(player_shot_b) - 1) + 1
    if a in player_shot_b:
        lower = min(lower_bound,other_lower)
    else:
        lower = lower_bound
    upper_bound = bst(b, player_shot_b, 0, len(player_shot_b) - 1) + 1
    count += upper_bound - lower + 1
print(count)
