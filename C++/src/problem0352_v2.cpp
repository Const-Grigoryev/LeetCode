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
#include <utility>

class SummaryRanges {
	struct Interval {
		int left, right;
	};

	// Maps some point within interval to the interval itself
	std::map<int, Interval> m;

public:
	void addNum(int v) {
		auto nil = m.end();
		auto j = m.upper_bound(v);
		auto i = j != m.begin() ? std::prev(j) : nil;

		auto p = i != nil && v - i->second.right <= 1 ? &i->second : NULL;
		auto q = j != nil && j->second.left - v <= 1 ? &j->second : NULL;
		if (p && q) {
			m.insert(j, {v, {p->left, q->right}});
			m.erase(i);
			m.erase(j);
		}
		else if (p) {
			p->right = std::max(p->right, v);
		}
		else if (q) {
			q->left = std::min(q->left, v);
		}
		else {
			m.insert(j, {v, {v, v}});
		}
	}

	std::vector<std::vector<int>> getIntervals() {
		std::vector<std::vector<int>> answer;
		std::transform(m.begin(), m.end(), std::back_inserter(answer),
			[](const auto &e) { return std::vector<int>{e.second.left, e.second.right}; }
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
