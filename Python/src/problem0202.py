# 202. Happy Number
# -----------------
#
# Write an algorithm to determine if a number `n` is happy.
#
# A **happy number** is a number defined by the following process:
#
#   * Starting with any positive integer, replace the number by the sum of the squares of its digits.
#   * Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle**
#     which does not include 1.
#   * Those numbers for which this process **ends in 1** are happy.
#
# Return `true` if `n` is a happy number, and `false` if not.
#
# ### Constraints:
#
#   * `1 <= n <= 2^31 - 1`
#
# Source: https://leetcode.com/problems/happy-number/

limit = 163
happy = {1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139}

def nextNumber(n):
	return sum((ord(c) - 48) ** 2 for c in str(n))

class Solution:
	def isHappy(self, n: int) -> bool:
		while n >= limit:
			n = nextNumber(n)
		return n in happy


if __name__ == '__main__':
	s = Solution()

	# Example 1:
	#
	# Input: n = 19
	# Output: true
	# Explanation: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.
	print(s.isHappy(19), "== true")

	# Example 2:
	#
	# Input: n = 2
	# Output: false
	print(s.isHappy(2), "== false")
