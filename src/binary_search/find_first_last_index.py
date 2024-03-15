def binary_search_left(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def binary_search_right(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right


nums = [5, 7, 7, 8, 8, 10]
target = 8

left_index = binary_search_left(nums, target)
right_index = binary_search_right(nums, target)
if left_index <= right_index:
    print(left_index, right_index)
else:
    print(-1, -1)
