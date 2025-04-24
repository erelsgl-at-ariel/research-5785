"""
Define the various available output formats for a partition algorithm.

For file 50-FlyWeight.
"""

from abc import ABC
from binners import *

BinsArray = any

class OutputType(ABC):
    @classmethod
    def create_binner(cls, valueof: callable) -> Binner:
        """
        Construct and return a Bins structure. Used at the initialization phase of an algorithm.
        """
        raise NotImplementedError("Choose a specific output type")

    @classmethod
    def extract_output_from_binsarray(cls, bins: BinsArray) -> list:
        """
        Return the required output from the given bins-array.
        """
        raise NotImplementedError("Choose a specific output type")


class Sums(OutputType):
    """ Output the list of sums of all bins (but not the bins' contents).  """
    @classmethod
    def create_binner(cls, valueof: callable) -> list:
        return BinnerKeepingSums(valueof)

    @classmethod
    def extract_output_from_sums(cls, sums: list[float]) -> list:
        return list(sums)

    @classmethod
    def extract_output_from_binsarray(cls, bins: BinsArray) -> list:
        try:
            bins[0][0]           # If it succeeds, it means that bins is a tuple (sums,lists).
            sums = bins[0]
        except:
            sums = bins          # If it fails, it means that bins is a singleton: sums.
        return cls.extract_output_from_sums(sums)


class LargestSum(Sums):
    """ Output the largest bin sum. """
    @classmethod
    def extract_output_from_sums(cls, sums: list[float]) -> list:
        return max(sums)

class SmallestSum(Sums):
    """ Output the smallest bin sum. """
    @classmethod
    def extract_output_from_sums(cls, sums: list[float]) -> list:
        return min(sums)

class SortedSums(Sums):
    """ Output the sums sorted from small to large. """
    @classmethod
    def extract_output_from_sums(cls, sums: list[float]) -> list:
        return sorted(sums)

class Difference(Sums):
    """ Output the difference between largest and smallest sum. """
    @classmethod
    def extract_output_from_sums(cls, sums: list[float]) -> list:
        return max(sums)-min(sums)




#
# Outputs based on the entire partition.
#

class Partition(OutputType):
    """ Output the set of all bins. """

    @classmethod
    def create_binner(cls, valueof: callable) -> list:
        return BinnerKeepingContents(valueof)

    @classmethod
    def extract_output_from_sums_and_lists(cls, sums: list[float], lists: list[list[any]]) -> list:
        return lists

    @classmethod
    def extract_output_from_binsarray(cls, bins: BinsArray) -> list:
        return cls.extract_output_from_sums_and_lists(bins[0], bins[1])


class PartitionAndSumsTuple(Partition):
    """ 
    Output a pair (tuple) with two vectors: (sums, lists). 
    sums is a vector of bin sums; lists is a vector of lists of items in each bin. 
    """
    @classmethod
    def extract_output_from_sums_and_lists(cls, sums: list[float], lists: list[list[any]]) -> list:
        return (sums,lists)


class PartitionAndSums(Partition):
    """ 
    Output a struct of all bins with their sums. 
    The struct has two fields: sums and lists. 
    sums is a vector of bin sums; lists is a vector of lists of items in each bin. 
    """
    class Struct:
        def __init__(self, sums, lists):
            self.sums = sums
            self.lists = lists
        def __repr__(self)->str:
            bins_str = [f"Bin #{i}: {self.lists[i]}, sum={self.sums[i]}" for i in range(len(self.sums))]
            return "\n".join(bins_str)
    @classmethod
    def extract_output_from_sums_and_lists(cls, sums: list[float], lists: list[list[any]]) -> list:
        return PartitionAndSums.Struct(sums,lists)

