# 42. Trapping Rain Water
# -----------------------
#
# Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much
# water it can trap after raining.
#
# ### Constraints:
#
#   * `n == height.length`
#   * `0 <= n <= 3 * 10^4`
#   * `0 <= height[i] <= 10^5`
#
# Source: https://leetcode.com/problems/trapping-rain-water/

from typing import List
from itertools import accumulate

class Solution:
    def trap(self, height: List[int]) -> int:
        left_bound = list(accumulate(height, max))
        right_bound = list(accumulate(height[::-1], max))
        right_bound.reverse()
        return sum(min(lb, rb) - h for h, lb, rb in zip(height, left_bound, right_bound))


if __name__ == '__main__':
    s = Solution()

    # Example 1:
    #
    # Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # Output: 6
    # [              #        ]
    # [      # ~ ~ ~ # # ~ #  ]
    # [  # ~ # # ~ # # # # # #]
    # [0 1 0 2 1 0 1 3 2 1 2 1]
    # Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this
    # case, 6 units of rain water (blue section) are being trapped.
    print(f"{s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])} == 6")

    # Example 2:
    #
    # Input: height = [4,2,0,3,2,5]
    # Output: 9
    print(f"{s.trap([4, 2, 0, 3, 2, 5])} == 9")