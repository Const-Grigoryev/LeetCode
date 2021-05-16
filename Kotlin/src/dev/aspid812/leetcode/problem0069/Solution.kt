package dev.aspid812.leetcode.problem0069

/* 69. Sqrt(x)
 * -----------
 *
 * Given a non-negative integer `x`, compute and return *the square root of `x`*.
 *
 * Since the return type is an integer, the decimal digits are **truncated**, and only **the integer part**
 * of the result is returned.
 *
 * ### Constraints:
 *
 *   * `0 <= x <= 2^31 - 1`
 *
 * Source: https://leetcode.com/problems/sqrtx/
 */

class Solution {
    companion object {
        private val MAGIC = 23_170
        private val QUADRUPLE_MAGIC = 4 * MAGIC - 1
    }

    fun mySqrt(a: Int): Int {
        // Newton's method with linear approximation of the initial value
        var x = MAGIC + Math.floorDiv(a - MAGIC, QUADRUPLE_MAGIC)
        var y = x * x - a
        while (y > 0) {
            x -= 1 + (y - 1) / (2 * x)
            y  = x * x - a
        }
        return x
    }
}

fun main() {
    val s = Solution()

    println("${s.mySqrt(4)} == 2")

    // The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
    println("${s.mySqrt(8)} == 2")
}