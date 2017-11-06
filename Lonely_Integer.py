n = map(int,input())

nums = map(int,input().split())

ans = 0

for num in nums:
    ans = ans ^ num

print(ans)