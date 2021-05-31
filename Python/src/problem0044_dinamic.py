# 44. Wildcard Matching
# ---------------------
#
# Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'`
# where:
#
#   * `'?'` Matches any single character.
#   * `'*'` Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the **entire** input string (not partial).
#
# ### Constraints:
#
#   * `0 <= s.length, p.length <= 2000`
#   * `s` contains only lowercase English letters.
#   * `p` contains only lowercase English letters, `'?'` or `'*'`.
#
# Source: https://leetcode.com/problems/wildcard-matching/

def match(text, pattern):
	n = len(text)
	table = list(k == 0 for k in range(n + 1))
	for p in pattern:
		if p == '*':
			for k in range(n):
				table[k + 1] = table[k + 1] or table[k]
		elif p == '?':
			for m in range(n, 0, -1):
				table[m] = table[m - 1]
			table[0] = False
		else:
			for m in range(n, 0, -1):
				table[m] = text[m - 1] == p and table[m - 1]
			table[0] = False
	return table[n]


class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		return match(s, p)

if __name__ == '__main__':
	s = Solution()

	# Example 1:
	#
	# Input: s = "aa", p = "a"
	# Output: false
	# Explanation: "a" does not match the entire string "aa".
	print(f"{s.isMatch(s='aa', p='a')} == false")

	# Example 2:
	#
	# Input: s = "aa", p = "*"
	# Output: true
	# Explanation: '*' matches any sequence.
	print(f"{s.isMatch(s='aa', p='*')} == true")

	# Example 3:
	#
	# Input: s = "cb", p = "?a"
	# Output: false
	# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
	print(f"{s.isMatch(s='cb', p='?a')} == false")

	# Example 4:
	#
	# Input: s = "adceb", p = "*a*b"
	# Output: true
	# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
	print(f"{s.isMatch(s='adceb', p='*a*b')} == true")

	# Example 5:
	#
	# Input: s = "acdcb", p = "a*c?b"
	# Output: false
	print(f"{s.isMatch(s='acdcb', p='a*c?b')} == false")

	# Example 6:
	#
	# Input: s = "ab", p = "?*"
	# Output: true
	print(f"{s.isMatch(s='ab', p='?*')} == true")

	# Example 7:
	#
	# Input: s = "", p = "ab*"
	# Output: true
	print(f"{s.isMatch(s='', p='ab*')} == false")