# 151. Reverse Words in a String
# ------------------------------
#
# Given an input string `s`, reverse the order of the **words**.
#
# A **word** is defined as a sequence of non-space characters. The **words** in `s` will be separated by at least
# one space.
#
# Return *a string of the words in reverse order concatenated by a single space*.
#
# **Note** that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string
# should only have a single space separating the words. Do not include any extra spaces.
#
# ### Constraints:
#
#   * `1 <= s.length <= 10^4`
#   * `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
#     There is at least one word in s.
#
# **Follow up:** Could you solve it **in-place** with `O(1)` extra space?

class Solution:
	def reverseWords(self, string: str) -> str:
		words = string.split()
		return " ".join(words[::-1])


if __name__ == '__main__':
	s = Solution()

	# Example 1:
	#
	# Input: s = "the sky is blue"
	# Output: "blue is sky the"
	print(f"{s.reverseWords('the sky is blue')} == 'blue is sky the'")

	# Example 2:
	#
	# Input: s = "  hello world  "
	# Output: "world hello"
	# Explanation: Your reversed string should not contain leading or trailing spaces.
	print(f"{s.reverseWords('  hello world  ')} == 'world hello'")

	# Example 3:
	#
	# Input: s = "a good   example"
	# Output: "example good a"
	# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
	print(f"{s.reverseWords('a good   example')} == 'example good a'")

	# Example 4:
	#
	# Input: s = "  Bob    Loves  Alice   "
	# Output: "Alice Loves Bob"
	print(f"{s.reverseWords('  Bob    Loves  Alice   ')} == 'Alice Loves Bob'")

	# Example 5:
	#
	# Input: s = "Alice does not even like bob"
	# Output: "bob like even not does Alice"
	print(f"{s.reverseWords('Alice does not even like bob')} == 'bob like even not does Alice'")