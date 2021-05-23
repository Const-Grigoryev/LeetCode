# 1. Two Sum
# ----------
#
# Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up
# to `target`.
#
# You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.
#
# You can return the answer in any order.
#
# ### Constraints:
#
#   * `2 <= nums.length <= 10^4`
#   * `-10^9 <= nums[i] <= 10^9`
#   * `-10^9 <= target <= 10^9`
#   * **Only one valid answer exists.**
#
# **Follow-up:** Can you come up with an algorithm that is less than `O(n^2)` time complexity?
#
# Source: https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		nums = [(x, i) for i, x in enumerate(nums)]
		nums.sort()

		i, j = 0, len(nums) - 1
		while i < j:
			x, x_index = nums[i]
			y, y_index = nums[j]
			if x + y < target:
				i += 1
			elif x + y > target:
				j -= 1
			else:
				return [x_index, y_index]


if __name__ == '__main__':
	s = Solution()

	# Example 1:
	#
	# Input: nums = [2,7,11,15], target = 9
	# Output: [0,1]
	# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
	print(f"{s.twoSum(nums=[2, 7, 11, 15], target=9)} == [0, 1]")

	# Example 2:
	#
	# Input: nums = [3,2,4], target = 6
	# Output: [1,2]
	print(f"{s.twoSum(nums=[3, 2, 4], target=6)} == [1, 2]")

	# Example 3:
	#
	# Input: nums = [3,3], target = 6
	# Output: [0,1]
	print(f"{s.twoSum(nums=[3, 3], target=6)} == [0, 1]")