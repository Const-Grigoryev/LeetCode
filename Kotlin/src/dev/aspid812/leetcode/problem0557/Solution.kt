package dev.aspid812.leetcode.problem0557

/* 557. Reverse Words in a String III
 * ----------------------------------
 *
 * Given a string `s`, reverse the order of characters in each word within a sentence while still preserving
 * whitespace and initial word order.
 *
 * ### Constraints:
 *
 *   * `1 <= s.length <= 5 * 10^4`
 *   * `s` contains printable **ASCII** characters.
 *   * `s` does not contain any leading or trailing spaces.
 *   * There is **at least one** word in `s`.
 *   * All the words in `s` are separated by a single space.
 */

class Solution {
    fun reverseWords(s: String) =
        s.split(' ').joinToString(" ", transform = String::reversed)
}

fun main() {
    val s = Solution()

    println("${s.reverseWords("Let's take LeetCode contest")} == \"s'teL ekat edoCteeL tsetnoc\"")
    println("${s.reverseWords("God Ding")} == \"doG gniD\"")
}
