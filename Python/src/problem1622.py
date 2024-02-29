# 1622. Fancy Sequence
# --------------------
#
# Write an API that generates fancy sequences using the `append`, `addAll`, and `multAll` operations.
#
# Implement the `Fancy` class:
#
#   * `Fancy()` Initializes the object with an empty sequence.
#   * `void append(val)` Appends an integer `val` to the end of the sequence.
#   * `void addAll(inc)` Increments all existing values in the sequence by an integer `inc`.
#   * `void multAll(m)` Multiplies all existing values in the sequence by an integer `m`.
#   * `int getIndex(idx)` Gets the current value at index `idx` (0-indexed) of the sequence **modulo** `10^9 + 7`.
#     If the index is greater or equal than the length of the sequence, return `-1`.
#
# ### Constraints:
#
#   * `1 <= val, inc, m <= 100`
#   * `0 <= idx <= 10^5`
#   * At most `10^5` calls total will be made to `append`, `addAll`, `multAll`, and `getIndex`.
#
# Source: https://leetcode.com/problems/fancy-sequence/

modulus = 1_000_000_007
limit = 100

# def bezout(a, b):
#     if b == 1:
#         return 0, 1
#     k, c = divmod(a, b)
#     x, y = bezout(b, c)
#     return y - b, x - k * y + a
#
# inv_table = [None] + list(bezout(modulus, a)[1] for a in range(1, limit + 1))

inv_table = [None,
            1, 500000004, 333333336, 250000002, 400000003, 166666668, 142857144, 125000001, 111111112, 700000005,
    818181824,  83333334, 153846155,  71428572, 466666670, 562500004, 352941179,  55555556, 157894738, 850000006,
     47619048, 409090912, 739130440,  41666667, 280000002, 576923081, 370370373,  35714286, 758620695, 233333335,
    129032259, 281250002, 939393946, 676470593, 628571433,  27777778, 621621626,  78947369, 717948723, 425000003,
    658536590,  23809524, 395348840, 204545456, 822222228, 369565220, 404255322, 520833337, 448979595, 140000001,
    784313731, 788461544,  56603774, 685185190, 763636369,  17857143, 385964915, 879310351,  50847458, 616666671,
    688524595, 564516133,  15873016, 140625001,  30769231, 469696973, 686567169, 838235300, 579710149, 814285720,
     98591550,  13888889, 410958907, 310810813,  93333334, 539473688, 831168837, 858974365, 202531647, 712500005,
    123456791, 329268295,  84337350,  11904762, 670588240, 197674420, 252873565, 102272728, 415730340, 411111114,
    164835166, 184782610,  43010753, 202127661, 231578949, 760416672, 268041239, 724489801, 646464651, 570000004,
]

class Fancy:
    def __init__(self):
        self._vals = list()
        self._addt = 0
        self._mult = 1
        self._imult = 1

    def append(self, y):
        q, a = self._imult, self._addt
        x = (q * (y - a)) % modulus
        self._vals.append(x)

    def getIndex(self, i):
        if i >= len(self._vals):
            return -1
        p, a = self._mult, self._addt
        x = self._vals[i]
        return (p * x + a) % modulus

    def addAll(self, a):
        self._addt += a

    def multAll(self, m):
        self._addt = (self._addt * m) % modulus
        self._mult = (self._mult * m) % modulus
        self._imult = (self._imult * inv_table[m]) % modulus


if __name__ == '__main__':
    # Example 1
    fancy = Fancy()
    fancy.append(2)     # [2]
    fancy.addAll(3)     # [2 + 3] -> [5]
    fancy.append(7)     # [5, 7]
    fancy.multAll(2)    # [5 * 2, 7 * 2] -> [10, 14]
    print(fancy.getIndex(0), "== 10")
    fancy.addAll(3)     # [10 + 3, 14 + 3] -> [13, 17]
    fancy.append(10)    # [13, 17, 10]
    fancy.multAll(2)    # [13 * 2, 17 * 2, 10 * 2] -> [26, 34, 20]
    print(fancy.getIndex(0), "== 26")
    print(fancy.getIndex(1), "== 34")
    print(fancy.getIndex(2), "== 20")
