def intersection_of_two_arrays(nums1,nums2):
    return list(set(nums1) & set(nums2))
nums1 = [1,3,5,4]
nums2 = [2,4,8,8]
print(intersection_of_two_arrays(nums1,nums2))
