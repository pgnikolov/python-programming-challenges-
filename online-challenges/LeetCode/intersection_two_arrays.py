def intersection(nums1, nums2):
    result = []
    nums2_count = {}
    for num in nums2:
        if num in nums2_count:
            nums2_count[num] += 1
        else:
            nums2_count[num] = 1
    for num in nums1:
        if num in nums2_count and nums2_count[num] > 0:
            result.append(num)
            nums2_count[num] -= 1

    return result
