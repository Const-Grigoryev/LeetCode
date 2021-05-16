package dev.aspid812.leetcode.problem0541

/* 541. Reverse String II
 * ----------------------
 *
 * Given a string `s` and an integer `k`, reverse the first `k` characters for every `2k` characters counting
 * from the start of the string.
 *
 * If there are fewer than `k` characters left, reverse all of them. If there are less than `2k` but greater than
 * or equal to `k` characters, then reverse the first `k` characters and left the other as original.
 *
 * ### Constraints:
 *
 *   * `1 <= s.length <= 10^4`
 *   * `s` consists of only lowercase English letters.
 *   * `1 <= k <= 10^4`
 */

import kotlin.math.min

class Solution {
    fun CharArray.swap(i: Int, j: Int) {
        val c = this[i]
        this[i] = this[j]
        this[j] = c
    }

    fun CharArray.reverse(start: Int, end: Int) {
        var i = start
        var j = end - 1
        while (i < j) {
            swap(i++, j--)
        }
    }

    fun reverseStr(str: String, k: Int): String {
        val s = str.toCharArray()
        for (i in s.indices.step(2 * k)) {
            s.reverse(i, min(i + k, s.size))
        }
        return String(s)
    }
}

fun main() {
    val s = Solution()

    println("${s.reverseStr(str="abcdefg", k=2)} == \"bacdfeg\"")
    println("${s.reverseStr(str="abcd", k=2)} == \"bacd\"")
}