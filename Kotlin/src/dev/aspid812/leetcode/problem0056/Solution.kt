package dev.aspid812.leetcode.problem0056

/* 56. Merge Intervals
 * -------------------
 *
 * Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return
 * *an array of the non-overlapping intervals that cover all the intervals in the input*.
 *
 * ### Constraints:
 *
 *   * `1 <= intervals.length <= 10^4`
 *   * `intervals[i].length == 2`
 *   * `0 <= start_i <= end_i <= 10^4`
 */

typealias Interval = IntArray

class Solution {
    fun merge(intervals: Array<Interval>): Array<Interval> {
        intervals.sortBy { interval -> interval[0] }

        var span = intArrayOf(-1, -1)
        var (i, j) = Pair(0, 0)
        while (j < intervals.size) {
            if (span[1] < intervals[j][0]) {
                intervals[i] = intervals[j]
                span = intervals[i]
                i += 1
            }
            else if (span[1] < intervals[j][1]) {
                span[1] = intervals[j][1]
            }
            j += 1
        }

        return intervals.copyOfRange(0, i)
    }
}

fun makeIntervals(vararg intervals: IntRange): Array<Interval> {
    return intervals.map { range -> intArrayOf(range.start, range.endInclusive)}.toTypedArray()
}

fun main() {
    val s = Solution()

    // Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    val intervals1 = makeIntervals(1..3, 2..6, 8..10, 15..18)
    println("${s.merge(intervals1).contentDeepToString()} == [[1,6],[8,10],[15,18]]")

    // Intervals [1,4] and [4,5] are considered overlapping.
    val intervals2 = makeIntervals(1..4, 4..5)
    println("${s.merge(intervals2).contentDeepToString()} == [[1,5]]")
}