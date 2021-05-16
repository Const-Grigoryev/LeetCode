package dev.aspid812.leetcode.problem1854

import java.time.Year

/* 1854. Maximum Population Year
 * -----------------------------
 *
 * You are given a 2D integer array `logs` where each `logs[i] = [birth_i, death_i]` indicates the birth and death
 * years of the `i`-th person.
 *
 * The **population** of some year `x` is the number of people alive during that year. The `i`-th person is counted
 * in year `x`'s population if `x` is in the **inclusive** range `[birth_i, death_i - 1]`. Note that the person
 * is **not** counted in the year that they die.
 *
 * Return *the **earliest** year with the **maximum population***.
 *
 * ### Constraints:
 *
 *   * `1 <= logs.length <= 100`
 *   * `1950 <= birth_i < death_i <= 2050`
 */

import kotlin.math.min

typealias Lifespan = IntArray

data class PopulationRecord(
    public val year: Int,
    public val population: Int
)

class Solution {
    fun maximumPopulation(logs: Array<Lifespan>): Int {
        val birthYears = logs.map { log -> log[0] }.toIntArray()
        birthYears.sort()

        val deathYears = logs.map { log -> log[1] }.toIntArray()
        deathYears.sort()

        return sequence {
            var population = 0
            var (i, j) = Pair(0, 0)
            while (i < birthYears.size || j < deathYears.size) {
                var year = min(
                    birthYears.getOrNull(i) ?: 2050,
                    deathYears.getOrNull(j) ?: 2050
                )
                while (i < birthYears.size && birthYears[i] == year) {
                    population += 1
                    i++
                }
                while (j < deathYears.size && deathYears[j] == year) {
                    population -= 1
                    j++
                }
                yield(PopulationRecord(year, population))
            }
        }.maxByOrNull(PopulationRecord::population)?.year ?: 1950
    }
}

fun makeLogs(vararg lifespans: IntRange): Array<Lifespan> {
    return lifespans.map { range -> intArrayOf(range.start, range.endInclusive + 1) }.toTypedArray()
}

fun main() {
    val s = Solution()

    // The maximum population is 1, and 1993 is the earliest year with this population.
    val logs1 = makeLogs(1993 until 1999, 2000 until 2010)
    println("${s.maximumPopulation(logs1)} == 1993")

    // The maximum population is 2, and it had happened in years 1960 and 1970.
    // The earlier year between them is 1960.
    val logs2 = makeLogs(1950 until 1961, 1960 until 1971, 1970 until 1981)
    println("${s.maximumPopulation(logs2)} == 1960")

    val logs3 = makeLogs(1982 until 1998, 2013 until 2042, 2010 until 2035, 2022 until 2050, 2047 until 2048)
    println("${s.maximumPopulation(logs3)} == 2022")
}
