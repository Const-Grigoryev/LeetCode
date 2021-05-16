package dev.aspid812.leetcode.problem0345

/* 345. Reverse Vowels of a String
 * -------------------------------
 *
 * Given a string `s`, reverse only all the vowels in the string and return it.
 *
 * The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both cases.
 *
 * ### Constraints:
 *
 *   * `1 <= s.length <= 3 * 10^5`
 *   * `s` consist of **printable ASCII** characters.
 */

class Solution {
    val vowels = "AEIOUaeiou"

    fun CharArray.swap(i: Int, j: Int) {
        val c = this[i]
        this[i] = this[j]
        this[j] = c
    }

    fun reverseVowels(input: String): String {
        val s = input.toCharArray()
        var i = s.indexOfFirst { it in vowels }
        var j = s.indexOfLast { it in vowels }
        while (i < j) {
            s.swap(i, j)
            while (s[++i] !in vowels) {}
            while (s[--j] !in vowels) {}
        }
        return String(s)
    }
}

fun main() {
    val s = Solution()

    println("${s.reverseVowels("hello")} == \'holle\"")
    println("${s.reverseVowels("leetcode")} == \"leotcede\"")
}