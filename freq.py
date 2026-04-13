def freq(nums):
    count = 0
    
    for i in range(len(nums) -1):
        current = nums[i]
        while True:
            if nums[i] == nums[i+1]:
              count += 1

    return count

nums = [1,1,1,2,1,1,4,5]
print(freq(nums))
