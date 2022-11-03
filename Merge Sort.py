def sortArray(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    def merge_sort(arr):
        if len(arr) > 1:
            # split to left and right arrays
            left_arr = arr[:len(arr) // 2]
            right_arr = arr[len(arr) // 2:]

            # sorting
            merge_sort(left_arr)
            merge_sort(right_arr)
            l = 0  # left index
            r = 0  # right inedx
            k = 0  # sorted array index
            while l < len(left_arr) and r < len(right_arr):
                if left_arr[l] < right_arr[r]:
                    arr[k] = left_arr[l]
                    l += 1
                else:
                    arr[k] = right_arr[r]
                    r += 1
                k += 1
            while l < len(left_arr):
                arr[k] = left_arr[l]
                l += 1
                k += 1
            while r < len(right_arr):
                arr[k] = right_arr[r]
                r += 1
                k += 1

    merge_sort(nums)
    return nums