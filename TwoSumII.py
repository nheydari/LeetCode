def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = 0
    r = len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if (target - sum) < 0:
            r -= 1
        elif (target - sum) > 0:
            l += 1
        else:
            return [l + 1, r + 1]