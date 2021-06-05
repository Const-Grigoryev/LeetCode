/* 354. Russian Doll Envelopes
 * ---------------------------
 *
 * You are given a 2D array of integers `envelope`s where `envelopes[i] = [w_i, h_i]` represents the width and
 * the height of an envelope.
 *
 * One envelope can fit into another if and only if both the width and height of one envelope are greater than
 * the other envelope's width and height.
 *
 * Return *the maximum number of envelopes you can Russian doll (i.e., put one inside the other)*.
 *
 * **Note:** You cannot rotate an envelope.
 *
 * ### Constraints:
 *
 *   * `1 <= envelopes.length <= 5000`
 *   * `envelopes[i].length == 2`
 *   * `1 <= w_i, h_i <= 10^4`
 *
 * Source: https://leetcode.com/problems/russian-doll-envelopes/
 */

package dev.aspid812.leetcode.problem0354

typealias Envelope = IntArray

fun lexicographical(x: Int, y: Int) = when {
	x != 0 -> x
	else   -> y
}

infix fun Envelope.lessThan(other: Envelope) = this[0] < other[0] && this[1] < other[1]

class Solution {
	fun maxEnvelopes(envelopes: Array<IntArray>): Int {
		envelopes.sortWith(Comparator<Envelope> { a, b -> lexicographical(a[0] - b[0], a[1] - b[1]) })
		val table = IntArray(envelopes.size)
		for (j in table.indices) {
			table[j] = (0 until j)
				.filter { i -> envelopes[i] lessThan envelopes[j] }
				.map { i -> table[i] + 1 }
				.maxOrNull() ?: 1
		}
		return table.maxOrNull() ?: 0
	}
}

fun main() {
	val s = Solution()

	// Example 1:
	//
	// Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
	// Output: 3
	// Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
	val envelopes1 = arrayOf(intArrayOf(5, 4), intArrayOf(6, 5), intArrayOf(6, 7), intArrayOf(2, 3))
	println("${s.maxEnvelopes(envelopes1)} == 3")

	// Example 2:
	//
	// Input: envelopes = [[1,1],[1,1],[1,1]]
	// Output: 1
	val envelopes2 = arrayOf(intArrayOf(1, 1), intArrayOf(1, 1), intArrayOf(1, 1))
	println("${s.maxEnvelopes(envelopes2)} == 1")
}