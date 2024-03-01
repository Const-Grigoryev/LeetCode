package dev.aspid812.leetcode.problem0202

/* 202. Happy Number
 * -----------------
 *
 * Write an algorithm to determine if a number `n` is happy.
 *
 * A **happy number** is a number defined by the following process:
 *
 *   * Starting with any positive integer, replace the number by the sum of the squares of its digits.
 *   * Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle**
 *     which does not include 1.
 *   * Those numbers for which this process **ends in 1** are happy.
 *
 * Return `true` if `n` is a happy number, and `false` if not.
 *
 * ### Constraints:
 *
 *   * `1 <= n <= 2^31 - 1`
 *
 * Source: https://leetcode.com/problems/happy-number/
 */

class Solution {

	// `n >= 163` implies `nextNumber(n) < n` and `n < 163` implies `nextNumber(n) < 163`
	val cacheLimit = 163
	val happyCache = setOf(
		1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133, 139
	)

	fun nextNumber(num: Int): Int =
		generateSequence(num) { n -> n / 10 }
			.takeWhile { it != 0 }
			.map { n -> n % 10 }
			.sumOf { d -> d * d }

	// Limit cycles of `happyProcess` are [0], [1] and [4, 16, 37, 58, 89, 145, 42, 20]
	fun happyProcess(seed: Int) =
		generateSequence(seed, this::nextNumber)

	fun isHappy(num: Int): Boolean =
		happyProcess(num).first { it < cacheLimit } in happyCache
}

fun main() {
	val s = Solution()

	// Example 1:
	//
	// Input: n = 19
	// Output: true
	// Explanation: 1^2 + 9^2 = 82, 8^2 + 2^2 = 68, 6^2 + 8^2 = 100, 1^2 + 0^2 + 0^2 = 1.
	println("${s.isHappy(19)} == true")

	//Example 2:
    //
	//Input: n = 2
	//Output: false
	println("${s.isHappy(2)} == false")
}