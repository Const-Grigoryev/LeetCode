package dev.aspid812.leetcode.problem0344

import java.util.*

/* 344. Reverse String
 * -------------------
 *
 * Write a function that reverses a string. The input string is given as an array of characters `s`.
 *
 *
 * ### Constraints:
 *
 *   * `1 <= s.length <= 10^5`
 *   * `s[i]` is a [printable ascii character](https://en.wikipedia.org/wiki/ASCII#Printable_characters).
 *
 * **Follow up:** Do not allocate extra space for another array. You must do this by modifying the input array
 * [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.
*/

class Solution {
    fun reverseString(s: CharArray): Unit {
        var i = s.indices.first
        var j = s.indices.last
        while (i < j) {
            val c = s[i]
            s[i++] = s[j]
            s[j--] = c
        }
    }
}

fun main() {
    val s = Solution()

    val s1 = charArrayOf('h', 'e', 'l', 'l', 'o')
    s.reverseString(s1)
    println("${s1.contentToString()} == ['o', 'l', 'l', 'e', 'h']")

    val s2 = charArrayOf('H', 'a', 'n', 'n', 'a', 'h')
    s.reverseString(s2)
    println("${s2.contentToString()} == ['h', 'a', 'n', 'n', 'a', 'H']")
}