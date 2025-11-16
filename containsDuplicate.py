def containsDuplicate(nums):
    return len(nums) != len(set(nums))

# test
print(containsDuplicate([1, 2, 3, 1]))
