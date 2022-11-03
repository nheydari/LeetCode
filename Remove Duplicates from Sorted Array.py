def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums) - 1):
        j = i + 1
        if j > len(nums) - 1:
            break
        while nums[i] == nums[j]:
            j += 1
            if j > len(nums) - 1:
                break
        if j > i + 1:
            del (nums[i + 1:j])
