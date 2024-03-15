def binary_search(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return arr[mid], mid
        elif target < arr[mid]:
            right = mid
        else:
            left = mid


arr = [2, 3, 1, 4, 7, 5]
target = 2
result = binary_search(arr, target)
print(result)
