# 51. N-Queens
# ------------
#
# The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack
# each other.
#
# Given an integer `n`, return *all distinct solutions to the **n-queens puzzle***. You may return the answer in **any
# order**.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate
# a queen and an empty space, respectively.
#
# ### Constraints:
#
#   * `1 <= n <= 9`
#
# Source: https://leetcode.com/problems/n-queens/

from typing import List
from collections import namedtuple

def log2(x):
	n = 0
	if x >> 8:  n, x = n + 8, x >> 8
	if x >> 4:  n, x = n + 4, x >> 4
	if x >> 2:  n, x = n + 2, x >> 2
	if x >> 1:  n, x = n + 1, x >> 1
	return n

def iterbits(mask):
	while mask:
		newmask = mask & (mask - 1)
		yield mask & ~newmask
		mask = newmask

Place = namedtuple("Place", 'row col tail')

def iterPlacement(self):
	p = self
	while p is not None:
		yield p
		p = p.tail

# (SHIFT + 1) must be greater than or equal to the maximal problem size (i.e. 9)
SHIFT = 8

def placeQueens(row, col, diag, codiag, placement):
	if row == 0:
		yield placement
		return

	r = next(iterbits(row))
	for c in iterbits(col & ((diag * r) >> SHIFT) & (codiag // r)):
		a, b = log2(r), log2(c)
		yield from placeQueens(
			row = row ^ (1 << a),
			col = col ^ (1 << b),
			diag = diag ^ (1 << (b + SHIFT - a)),
			codiag = codiag ^ (1 << (b + a)),
			placement = Place(a, b, placement)
		)

class Solution:
	def solveNQueens(self, n: int) -> List[List[str]]:
		row = col = (1 << n) - 1
		diag = (1 << (SHIFT + n)) - (1 << (SHIFT - n + 1))
		codiag = (1 << (2 * n - 1)) - 1

		renderRow = lambda q: '.' * q.col + 'Q' + '.' * (n - q.col - 1)
		return list(
			list(renderRow(queen) for queen in iterPlacement(placement))
			for placement in placeQueens(row, col, diag, codiag, None)
		)


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
	print(f"{s.solveNQueens(4)} == [['.Q..','...Q','Q...','..Q.'],['..Q.','Q...','...Q','.Q..']]")

	# Example 2:
	#
	# Input: n = 1
	# Output: [["Q"]]
	print(f"{s.solveNQueens(1)} == [['Q']]")