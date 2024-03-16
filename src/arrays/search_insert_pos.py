
# Using Binary Search O(log n)
def search_position(nums, target) -> int:
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    arr = [1]
    target = 0
    result = search_position(arr, target)
    print(result)
