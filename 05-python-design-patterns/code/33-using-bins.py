"""
Number partitioning algorithms - uses a structure for bins.

Author: Erel Segal-Halevi
Since: 2022-03
"""

from bins import *


def roundrobin(bins: Bins, items: list[float]):
    """
    Partition the given items using the round-robin algorithm.

    >>> roundrobin(BinsKeepingSums(2), items=[1,2,3,3,5,9,9]).result()
    [18, 14]
    >>> roundrobin(BinsKeepingContents(2), items=[1,2,3,3,5,9,9]).result()
    [[9, 5, 3, 1], [9, 3, 2]]
    """
    ibin = 0
    for item in sorted(items, reverse=True):
        bins.add_item_to_bin(item, ibin)
        ibin = (ibin+1) % bins.num
    return bins


def greedy(bins: Bins, items: list[float]):
    """
    Partition the given items using the greedy number partitioning algorithm.
    Return the partition.

    >>> greedy(bins=BinsKeepingSums(2), items=[1,2,3,3,5,9,9]).result()
    [16, 16]
    >>> greedy(bins=BinsKeepingContents(2), items=[1,2,3,3,5,9,9]).result()
    [[9, 5, 2], [9, 3, 3, 1]]
    """
    for item in sorted(items, reverse=True):
        index_of_least_full_bin = min(range(bins.num), key=bins.sums.__getitem__)
        bins.add_item_to_bin(item, index_of_least_full_bin)
    return bins



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
