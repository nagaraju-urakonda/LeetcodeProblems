def moveZeroes(nums):
  l = 0
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[l],nums[i] = nums[i],nums[l]
      l += 1
  return nums
nums = [0,1,2,0,4,5]
print(moveZeros(nums))
