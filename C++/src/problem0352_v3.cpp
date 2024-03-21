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

#include <set>
#include <vector>
#include <iterator>
#include <algorithm>
#include <utility>

class SummaryRanges {
	struct Interval {
		int left, right;

		Interval(int v) : left(v), right(v) {}
	};

	struct IntervalInvariant {
		bool operator()(const Interval &lhs, const Interval &rhs) const {
			return rhs.left - lhs.right > 1;
		}
	};

	// The set maintains invariant for each pair of adjacent entries
	std::set<Interval, IntervalInvariant> m;

public:
	void addNum(int v) {
		if (!m.insert(v).second) {
			auto [first, last] = m.equal_range(v);
			int left = first->left, right = (--last)->right;
			auto combined = &const_cast<Interval &>(*m.erase(first, last));
			combined->left = std::min(v, left);
			combined->right = std::max(v, right);
		}
	}

	std::vector<std::vector<int>> getIntervals() {
		std::vector<std::vector<int>> answer;
		std::transform(m.begin(), m.end(), std::back_inserter(answer),
			[](const auto &e) { return std::vector<int>{e.left, e.right}; }
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
