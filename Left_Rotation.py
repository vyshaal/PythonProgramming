n,d = [int(inp) for inp in str(input()).split()]

nums = [int(num) for num in str(input()).split()]

nums = nums[d:]+nums[0:d]
print(" ".join([str(num) for num in nums]))