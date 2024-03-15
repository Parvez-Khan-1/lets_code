"""
Example 1:
Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
Output: [5, 6]

Example 2:
Input: nums = [1, 1]
Output: [2]
"""
from typing import List


# Brute force approach -
# O(n)
# Time limit exceeded
def find_missing_num_brute_force(nums: List[int]):
    missing_nums = []
    for i in range(1, len(nums)+1):
        if i not in nums:
            missing_nums.append(i)
    return missing_nums


# Average case time complexity O(1)
# Worst case time complexity O(n**n)
def find_missing_num_approach_1(nums: List[int]):
    sorted_nums = set(nums)
    print(len(sorted_nums))
    print(len(nums))
    if len(nums) == len(sorted_nums):
        return []
    else:
        return [i for i in range(1, len(nums)+1) if i not in sorted_nums]


# Average case time complexity O(1)
# Worst case time complexity O(n**n)
def find_missing_num_approach_2(nums: List[int]):
    sorted_nums = set(nums)
    print(len(sorted_nums))
    print(len(nums))
    if len(nums) == len(sorted_nums):
        return []
    else:
        return [i for i in range(1, len(nums)+1) if i not in sorted_nums]


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(find_missing_num_approach_1(nums))
