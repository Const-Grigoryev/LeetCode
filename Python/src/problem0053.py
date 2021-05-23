# 53. Maximum Subarray
# --------------------
#
# Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest
# sum and return *its sum*.
#
# ### Constraints:
#
#   * `1 <= nums.length <= 3 * 10^4`
#   * `-10^5 <= nums[i] <= 10^5`
#
# **Follow up:** If you have figured out the `O(n)` solution, try coding another solution using the **divide and
# conquer** approach, which is more subtle.

from typing import List
from itertools import accumulate

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		return max(accumulate(nums, lambda a, x: max(0, a) + x))


if __name__ == '__main__':
	s = Solution()

	# Example 1:
	#
	# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
	# Output: 6
	# Explanation: [4,-1,2,1] has the largest sum = 6.
	print(f"{s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])} == 6")

	# Example 2:
	#
	# Input: nums = [1]
	# Output: 1
	print(f"{s.maxSubArray([1])} == 1")

	# Example 3:
	#
	# Input: nums = [5,4,-1,7,8]
	# Output: 23
	print(f"{s.maxSubArray([5, 4, -1, 7, 8])} == 23")