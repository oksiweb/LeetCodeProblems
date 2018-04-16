def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    length = len(nums)
    start = 0
    end = length - 1
    arr = sorted(nums)

    while start <= end and length:
        mid = (end + start) // 2

        if arr[mid] == target:
            return nums.index(arr[mid])
        elif arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
    return -1

print(search([4,5,6,7,0,1,2], 0))