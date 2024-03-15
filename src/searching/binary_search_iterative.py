def binary_search(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return arr[mid], mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False


if __name__ == '__main__':
    arr = [2, 3, 1, 4, 7, 5]
    target = 10
    result = binary_search(arr, target)
    print(result)
