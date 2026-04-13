def find_missing(nums):
    diff = nums[1] - nums[0]
    missing = []

    for i in range(len(nums) - 1):
        current = nums[i]
        while nums[i+1] - current > diff:
            current += diff
            missing.append(current)
        
    return missing
        

nums = [1,2,3,5,6,8]
print(find_missing(nums))