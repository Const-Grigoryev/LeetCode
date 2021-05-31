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

# ### Author's remark:
#
# This naive solution demonstrates surprisingly decent results:
#
# > Runtime: 48 ms, faster than 91.54% of Python3 online submissions for Wildcard Matching.
# > Memory Usage: 14.2 MB, less than 96.90% of Python3 online submissions for Wildcard Matching.

def substr(text, pat, offset=0):
	m, n = 0, min(len(pat), len(text) - offset)
	while m < n and (pat[m] == '?' or pat[m] == text[offset + m]):
		m += 1
	return m == len(pat)


def find(text, pat, offset=0):
	for m in range(offset, len(text) - len(pat) + 1):
		if substr(text, pat, m):
			return m
	return -1

def findall(text, pats):
	m = 0
	for pat in pats:
		loc = find(text, pat, m)
		if loc < 0:
			break
		yield loc
		m = loc + len(pat)

class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		pats = p.split('*')
		if len(pats) == 1:
			return len(s) == len(p) and substr(s, p)
		else:
			locs = list(findall(s, pats))
			prefix, suffix = pats[0], pats[-1]
			return len(locs) == len(pats) and substr(s[:len(prefix)], prefix) and substr(s[-len(suffix):], suffix)


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