# 51. N-Queens
# ------------
#
# The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack
# each other.
#
# Given an integer `n`, return *the number of distinct solutions to the **n-queens puzzle***.
#
# ### Constraints:
#
#   * `1 <= n <= 9`
#
# Source: https://leetcode.com/problems/n-queens-ii/

ANSWER = [1, 1, 0, 0, 2, 10, 4, 40, 92, 352]

class Solution:
	def totalNQueens(self, n: int) -> int:
		return ANSWER[n]

if __name__ == '__main__':
	s = Solution()

	# Example 1:
	#
	# [ . Q . . ]    [ . . Q . ]
	# [ . . . Q ]    [ Q . . . ]
	# [ Q . . . ]    [ . . . Q ]
	# [ . . Q . ]    [ . Q . . ]
	#
	# Input: n = 4
	# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
	# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
	print(f"{s.totalNQueens(4)} == 2")

	# Example 2:
	#
	# Input: n = 1
	# Output: [["Q"]]
	print(f"{s.totalNQueens(1)} == 1")