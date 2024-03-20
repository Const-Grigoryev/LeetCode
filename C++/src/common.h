#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>

namespace std {    // Debug output
	template<typename T>
	ostream &operator<<(ostream &ostr, const vector<T> &vec) {
		ostr << "[";
		if (!vec.empty()) {
			auto first = vec.begin(), last = prev(vec.end());
			copy(first, last, ostream_iterator<T>(ostr, ", "));
			ostr << *last;
		}
		return ostr << "]";
	}
}