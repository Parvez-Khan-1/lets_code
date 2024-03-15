def binary_search(arr, target, left, right):
    if left > right:
        return -1

    # Check if target is within the range of array elements
    if target < arr[left] or target > arr[right]:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return arr[mid]

    elif target < arr[mid]:
        return binary_search(arr, target, left, mid)
    else:
        return binary_search(arr, target, mid + 1, right)


arr = [2, 3, 1, 4, 7, 5]
arr.sort()
target = -30
left = 0
right = len(arr)-1
result = binary_search(arr, target, left, right)
print(result)