/* 352. Data Stream as Disjoint Intervals
 * --------------------------------------
 *
 * Given a data stream input of non-negative integers `a[1], a[2], ..., a[n]`, summarize the numbers seen so far
 * as a list of disjoint intervals.
 *
 * Implement the `SummaryRanges` class:
 *
 *   * `SummaryRanges()` initializes the object with an empty stream.
 *   * `void addNum(int value)` adds the integer value to the stream.
 *   * `int[][] getIntervals()` returns a summary of the integers in the stream currently as a list of disjoint
 *     intervals `[start[i], end[i]]`. The answer should be sorted by `start[i]`.
 *
 * ### Constraints:
 *
 *   * `0 <= value <= 10^4`
 *   * At most `3 * 10^4` calls will be made to `addNum` and `getIntervals`.
 *   * At most `10^2` calls will be made to `getIntervals`.
 *
 * **Follow up:** What if there are lots of merges and the number of disjoint intervals is small compared to the size
 * of the data stream?
 *
 * Source: https://leetcode.com/problems/data-stream-as-disjoint-intervals/
 */

#include "common.h"

#include <map>
#include <vector>
#include <iterator>
#include <algorithm>

class SummaryRanges {
	// Maps left bound of each interval to its right bound
	std::map<int, int> m;

public:
	void addNum(int v) {
		auto it = m.upper_bound(v);
		auto rit = std::map<int, int>::reverse_iterator(it);
		if (rit != m.rend() && v <= rit->second)
			return;

		int left = rit != m.rend() && v == rit->second + 1 ? rit->first : v;
		int right = it != m.end() && v == it->first - 1 ? it->second : v;
		if (rit != m.rend() && rit->first == left) {
			rit->second = right;
		}
		else {
			m.insert(it, {left, right});
		}
		if (it != m.end() && it->second == right) {
	        m.erase(it);
		}
	}

	std::vector<std::vector<int>> getIntervals() const {
		std::vector<std::vector<int>> answer;
		std::transform(m.begin(), m.end(), std::back_inserter(answer),
	        [](const auto &i) { return std::vector<int>{i.first, i.second}; }
		);
		return answer;
	}
};



int main() {
	SummaryRanges summaryRanges;
    summaryRanges.addNum(1);      // arr = [1]
    std::cout << summaryRanges.getIntervals() << " == [[1, 1]]" << std::endl;
    summaryRanges.addNum(3);      // arr = [1, 3]
    std::cout << summaryRanges.getIntervals() << " == [[1, 1], [3, 3]]" << std::endl;
    summaryRanges.addNum(7);      // arr = [1, 3, 7]
    std::cout << summaryRanges.getIntervals() << " == [[1, 1], [3, 3], [7, 7]]" << std::endl;
    summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
    std::cout << summaryRanges.getIntervals() << " == [[1, 3], [7, 7]]" << std::endl;
    summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
    std::cout << summaryRanges.getIntervals() << " == [[1, 3], [6, 7]]" << std::endl;
}