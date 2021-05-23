# 69. Sqrt(x)
# -----------
#
# Given a non-negative integer `x`, compute and return *the square root of `x`*.
#
# Since the return type is an integer, the decimal digits are **truncated**, and only **the integer part**
# of the result is returned.
#
# ### Constraints:
#
#   * `0 <= x <= 2^31 - 1`
#
# Source: https://leetcode.com/problems/sqrtx/

class Solution:
	def mySqrt(self, a: int) -> int:
		lo, hi = 0, 1
		while hi * hi <= a:
			lo, hi = hi, hi * 2
		while lo < hi:
			x = hi - (hi - lo) // 2
			if x * x <= a:
				lo = x
			else:
				hi = x - 1
		return hi


if __name__ == '__main__':
	s = Solution()

	# Example 1:
	#
	# Input: x = 4
	# Output: 2
	print(f"{s.mySqrt(4) == 2}")

	# Example 2:
	#
	# Input: x = 8
	# Output: 2
	# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
	print(f"{s.mySqrt(8) == 2}")