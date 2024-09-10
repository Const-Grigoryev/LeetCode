LeetCode
========

[LeetCode](https://leetcode.com/) is a collection of algorithmic problems which is purposed for a training before a coding interview. Here I suggest my own solutions to some of those problems.

Problems and Solutions
----------------------

| Problem | Difficulty and Acceptance | Solution | :stopwatch:[^runtime] | Notes |
|---------|---------------------------|----------|-----------------------|-------|
| [1622. Fancy Sequence](https://leetcode.com/problems/fancy-sequence/) | :hot_pepper::hot_pepper::hot_pepper: 17.1% | [Python](Python/src/problem1622.py) | 97% :zap: | **Key observation #1:** it is easy to solve a similar problem about `float`s or something like that. Just keep a set of numbers and an overbuilt linear transformation separately and pass any incoming number through the inverse transformation before adding it into the set.<br>**Key observation #2:** in fact, we already have “something like `float`”. We are asked to perform all operations in $\mathbb{Z} / (10^9 + 7)$, which is a field, since modulus is a prime number. A reciprocal in this field may be calculated using [Bézout identity][bezout].<br>**Key observation #3:** incoming multipliers are bounded by a relatively small number, about 100. Therefore we don't need to invert them in runtime, it would be sufficient to precompute a table of its inversions offline and store it as a plain static array. |
| [352. Data Stream as Disjoint Intervals](https://leetcode.com/problems/data-stream-as-disjoint-intervals/) | :hot_pepper::hot_pepper::hot_pepper: 60.0% | [C++ (eager)](C++/src/problem0352_v1.cpp) | 35% | All my C++ solutions are based on `std` ordered containers. This particular one is not too fast, but makes an interesting example of using a *reverse iterator*. |
| —〃— | —〃— | [C++ (eager)](C++/src/problem0352_v2.cpp) | 100% | A significant improvement of the previous solution, that avoids unnecessary modification of a search tree and provides a cleaner, more “symmetrical” view of the problem. |
| —〃— | —〃— | [C++ (eager)](C++/src/problem0352_v3.cpp) | 100% :zap: | The most clean and laconic solution. First, a confusing `std::map` was abandoned in favor of natural `std::set` of intervals. Second, a major share of work was assigned to a smartly chosen comparator (this comparator is considered as an invariant, which is automatically maintained by a `set`). Third, some amount of efficiency was sacrificed for code aesthetics, switching general design principle to a more transparent “try to insert and, if fail, fix whats hinder”. Finally, a `const_cast` trick helped to counterbalance that sacrifice and to keep a near-top performance. |
| —〃— | —〃— | Python *(coming soon)* | | A completely different approach. Instead of eager modification of a sophisticated data structure, I just accumulate incoming points into a list. And only on user's demand I convert them to a sequence of intervals and [merge][merge] it with the same sequence from the last step. |
| [1482. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | :lemon::lemon: 55.6% | [Python](Python/src/problem1482.py) | 81% | I maintain a set of _rows_ (a row is a sequence of flowers those are already blossomed) and update it on-line at each blossom day. Each update takes a constant time, but since the input must be preliminarily sorted, the overall complexity is $O(n \log n)$. In contrast, a [treap][treap] promises to reduce complexity down to linear. |
| [202. Happy Number](https://leetcode.com/problems/happy-number/) | :broccoli: 56.0% | [Python](Python/src/problem0202.py) | 97% :zap: | As I figured out, the function reduces any sufficient large number for at least one digit. Thus the number of steps is proportional to a bit length of the input value. For smaller values I have just precalculated the answer. |
| —〃— | —〃— | [Kotlin](Kotlin/src/dev/aspid812/leetcode/problem0202/Solution.kt) | 7% | The same as above, but in Kotlin. I have made it as an exercise in Sequence API, and nothing more. |

[^runtime]: This column shows a _runtime percentile_. For instance, “65%” should be read as “my solution beats 65% of others” (on the same platform). So, a larger value means a faster code and a better result.

[merge]: https://en.wikipedia.org/wiki/Merge_algorithm
[bezout]: https://en.wikipedia.org/wiki/Bézout's_identity
[treap]: https://en.wikipedia.org/wiki/Treap
