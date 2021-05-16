package dev.aspid812.leetcode.problem0539

/* 539. Minimum Time Difference
 * ----------------------------
 * Given a list of 24-hour clock time points in **"HH:MM"** format, return the *minimum **minutes** difference
 * between any two time-points in the list*.
 *
 * ### Constraints:
 *
 *   * `2 <= timePoints <= 2 * 10^4`
 *   * `timePoints[i]` is in the format **"HH:MM"**.
 */

class Solution {
    fun findMinDifference(timePoints: List<String>): Int {
        return timePoints.asSequence()
            .map { timePoint ->
                val hours = timePoint.substringBefore(':').toInt()
                val minutes = timePoint.substringAfter(':').toInt()
                hours * 60 + minutes
            }
            .sorted()
            .let { seq ->
                val instant = seq.iterator().next()
                seq + (instant + 1440)
            }
            .zipWithNext { start, end -> end - start }
            .minOrNull() ?: 1440
    }
}

fun main() {
    val s = Solution()

    val timePoints1 = listOf("23:59", "00:00")
    println("${s.findMinDifference(timePoints1)} == 1")

    val timePoints2 = listOf("00:00", "23:59", "00:00")
    println("${s.findMinDifference(timePoints2)} == 1")
}