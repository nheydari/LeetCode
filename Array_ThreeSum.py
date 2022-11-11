def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    locs = []
    for i, j in enumerate(nums):
        if i > 0 and nums[i - 1] == j:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = nums[l] + nums[r]
            if (j + sum) > 0:
                r -= 1
            elif (j + sum) < 0:
                l += 1
            else:
                locs.append([j, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return locs