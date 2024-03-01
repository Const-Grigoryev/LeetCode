# 300. Longest Increasing Subsequence
# -----------------------------------
#
# Given an integer array `nums`, return the length of the longest strictly increasing subsequence.
#
# A **subsequence** is a sequence that can be derived from an array by deleting some or no elements without changing
# the order of the remaining elements. For example, `[3,6,2,7]` is a subsequence of the array `[0,3,1,6,2,2,7]`.
#
# ### Constraints:
#
#   * `1 <= nums.length <= 2500`
#   * `-10^4 <= nums[i] <= 10^4`
#
# Source: https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

def binsearch(arr, x):
    u, v = 0, len(arr)
    while u < v:
        m = (u + v) // 2
        if arr[m] >= x:
            v = m
        else:
            u = m + 1
    return u

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        table = []
        for x in nums:
            k = binsearch(table, x)
            if k == len(table):
                table.append(x)
            else:
                table[k] = x
        return len(table)


if __name__ == '__main__':
    s = Solution()

    # Example 1:
    #
    # Input: nums = [10,9,2,5,3,7,101,18]
    # Output: 4
    # Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
    print(f"{s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])} == 4")

    # Example 2:
    #
    # Input: nums = [0,1,0,3,2,3]
    # Output: 4
    print(f"{s.lengthOfLIS([0, 1, 0, 3, 2, 3])} == 4")

    # Example 3:
    #
    # Input: nums = [7,7,7,7,7,7,7]
    # Output: 1
    print(f"{s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7])} == 1")