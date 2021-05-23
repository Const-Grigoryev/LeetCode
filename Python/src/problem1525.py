# 1525. Number of Good Ways to Split a String
# -------------------------------------------
#
# You are given a string `s`, a split is called *good* if you can split `s` into 2 non-empty strings `p` and `q`
# where its concatenation is equal to `s` and the number of distinct letters in `p` and `q` are the same.
#
# Return the number of *good* splits you can make in `s`.
#
# ### Constraints:
#
#   * `s` contains only lowercase English letters.
#   * `1 <= s.length <= 10^5`
#
# Source: https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

def cum_card(items):
	s = set()
	yield 0
	for x in items:
		s.add(x)
		yield len(s)

class Solution:
	def numSplits(self, string: str) -> int:
		prefix = list(cum_card(string))
		suffix = list(cum_card(string[::-1]))
		return sum(p == q for p, q in zip(prefix, suffix[::-1]))


if __name__ == '__main__':
	s = Solution()

	# Example 1:
	#
	# Input: s = "aacaba"
	# Output: 2
	# Explanation: There are 5 ways to split "aacaba" and 2 of them are good.
	# ("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
	# ("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
	# ("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
	# ("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
	# ("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
	print(f"{s.numSplits('aacaba')} == 2")

	# Example 2:
	#
	# Input: s = "abcd"
	# Output: 1
	# Explanation: Split the string as follows ("ab", "cd").
	print(f"{s.numSplits('abcd')} == 1")

	# Example 3:
	#
	# Input: s = "aaaaa"
	# Output: 4
	# Explanation: All possible splits are good.
	print(f"{s.numSplits('aaaaa')} == 4")

	# Example 4:
	#
	# Input: s = "acbadbaada"
	# Output: 2
	print(f"{s.numSplits('acbadbaada')} == 2")