/* 4. Median of Two Sorted Arrays
 * ------------------------------
 *
 * Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two
 * sorted arrays.
 *
 * The overall run time complexity should be `O(log (m+n))`.
 *
 * ### Constraints:
 *
 *   * `nums1.length == m`
 *   * `nums2.length == n`
 *   * `0 <= m <= 1000`
 *   * `0 <= n <= 1000`
 *   * `1 <= m + n <= 2000`
 *   * `-10^6 <= nums1[i], nums2[i] <= 10^6`
 *
 * Source: https://leetcode.com/problems/median-of-two-sorted-arrays/
 */

package dev.aspid812.leetcode.problem0004

import java.lang.Integer.max
import java.lang.Integer.min

class Solution {
	fun binarySearch(lower: Int, upper: Int, pred: (Int) -> Boolean): Int {
		var u = lower
		var v = upper
		while (u < v) {
			val m = (u + v) / 2
			if (pred(m)) {
				v = m
			}
			else {
				u = m + 1
			}
		}
		return u
	}

	fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
		val m = nums1.size
		val n = nums2.size
		val r = (m + n) / 2
		val p = binarySearch(max(0, r - n), min(r, m)) { p ->
			nums1[p] >= nums2[r - p - 1]
		}
		val q = r - p

		val x1 = if (p > 0) nums1[p - 1] else Int.MIN_VALUE
		val x2 = if (p < m) nums1[p] else Int.MAX_VALUE
		val y1 = if (q > 0) nums2[q - 1] else Int.MIN_VALUE
		val y2 = if (q < n) nums2[q] else Int.MAX_VALUE

		if ((m + n) % 2 == 0) {
			return (max(x1, y1) + min(x2, y2)) / 2.0
		}
		else {
			return min(x2, y2).toDouble()
		}
	}
}

fun main() {
	val s = Solution()

	//Example 1:
	//
	//Input: nums1 = [1,3], nums2 = [2]
	//Output: 2.00000
	//Explanation: merged array = [1,2,3] and median is 2.
	var nums1 = intArrayOf(1, 3)
	var nums2 = intArrayOf(2)
	println("${s.findMedianSortedArrays(nums1, nums2)} == 2.00000")

	//Example 2:
	//
	//Input: nums1 = [1,2], nums2 = [3,4]
	//Output: 2.50000
	//Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
	nums1 = intArrayOf(1, 2)
	nums2 = intArrayOf(3, 4)
	println("${s.findMedianSortedArrays(nums1, nums2)} == 2.50000")

	//Example 3:
	//
	//Input: nums1 = [0,0], nums2 = [0,0]
	//Output: 0.00000
	nums1 = intArrayOf(0, 0)
	nums2 = intArrayOf(0, 0)
	println("${s.findMedianSortedArrays(nums1, nums2)} == 0.00000")

	//Example 4:
	//
	//Input: nums1 = [], nums2 = [1]
	//Output: 1.00000
	nums1 = intArrayOf()
	nums2 = intArrayOf(1)
	println("${s.findMedianSortedArrays(nums1, nums2)} == 1.00000")

	//Example 5:
	//
	//Input: nums1 = [2], nums2 = []
	//Output: 2.00000
	nums1 = intArrayOf(2)
	nums2 = intArrayOf()
	println("${s.findMedianSortedArrays(nums1, nums2)} == 2.00000")
}