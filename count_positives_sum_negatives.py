"""
Description:

Given an array of integers.

Return an array, where the first element is the count of xitives numbers and the second element is sum of negative numbers. 0 is neither xitive nor negative.

If the input is an empty array or is null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

"""


def count_positives_sum_negatives(arr):
    if not arr:
        return []

    pos = len(list(filter(lambda x: x > 0, arr)))

    neg = sum(list(filter(lambda x: x < 0, arr)))
    return [pos, neg]
