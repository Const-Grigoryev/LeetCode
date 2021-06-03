package dev.aspid812.leetcode.problem0010

/* 10. Regular Expression Matching
 * -------------------------------
 *
 * Given an input string (`s`) and a pattern (`p`), implement regular expression matching with support for `'.'`
 * and `'*'` where:
 *
 *   * `'.'` Matches any single character.
 *   * '*' Matches zero or more of the preceding element.
 *
 * The matching should cover the **entire** input string (not partial).
 *
 * ### Constraints:
 *
 *   * `0 <= s.length <= 20`
 *   * `0 <= p.length <= 30`
 *   * `s` contains only lowercase English letters.
 *   * `p` contains only lowercase English letters, `'.'`, and `'*'`.
 *   * It is guaranteed for each appearance of the character `'*'`, there will be a previous valid character to match.
 */

class DynamicSolution(
	val text: String,
	val pattern: String
) {
	private val table = BooleanArray(text.length + 1)

	private fun matchChar(char: Char, pat: Char): Boolean {
		return char == pat || pat == '.'
	}

	private fun updateTableOne(p: Char) {
		for (m in text.indices.reversed()) {
			table[m + 1] = matchChar(text[m], p) && table[m]
		}
		table[0] = false
	}

	private fun updateTableMany(p: Char) {
		for (m in text.indices) {
			table[m + 1] = table[m + 1] || ((matchChar(text[m], p)) && table[m])
		}
	}

	fun solve(): Boolean {
		table[0] = true
		sequence {
			yieldAll(pattern.asIterable())
			yield('1')
		}
			.zipWithNext()
			.filter { it.first != '*' }
			.forEach {
				if (it.second == '*') {
					updateTableMany(it.first)
				}
				else {
					updateTableOne(it.first)
				}
			}
		return table.last()
	}
}

class Solution {
	fun isMatch(s: String, p: String): Boolean {
		return DynamicSolution(s, p).solve()
	}
}

fun main() {
	val s = Solution()

	// Example 1:
	//
	//Input: s = "aa", p = "a"
	//Output: false
	//Explanation: "a" does not match the entire string "aa".
	println("${s.isMatch(s = "aa", p = "a")} == false")

	//Example 2:
	//
	//Input: s = "aa", p = "a*"
	//Output: true
	//Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
	println("${s.isMatch(s = "aa", p = "a*")} == true")

	//Example 3:
	//
	//Input: s = "ab", p = ".*"
	//Output: true
	//Explanation: ".*" means "zero or more (*) of any character (.)".
	println("${s.isMatch(s = "ab", p = ".*")} == true")

	//Example 4:
	//
	//Input: s = "aab", p = "c*a*b"
	//Output: true
	//Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
	println("${s.isMatch(s = "aab", p = "c*a*b")} == true")

	//Example 5:
	//
	//Input: s = "mississippi", p = "mis*is*p*."
	//Output: false
	println("${s.isMatch(s = "mississippi", p = "mis*is*p*.")} == false")
}
