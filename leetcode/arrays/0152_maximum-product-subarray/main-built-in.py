from typing import List


class Solution:
    """
    nums: integer array
        We don't need to think about the case of numbers 0<x<1 or -1<x<0.
    answer will fit in a 32-bit integer.
        We can just accumulate the product

    The tricky part are the min numbers,
        with odd mins, we go all way to min bottom
        but with even mins, we go back upwards

    Some examples to think:

    nums = [-1, -1, -99, 1]
        if we just look curr_prod > 0 and num < 0:
        we are going to miss the [-1, -99] sub-array.

    nums = [-2,0,-1]
        if we just skip the 0, we are not going to get the right answer

    So one idea is to keep 2 accumulators,
    one for the min value and another for the max value
    """

    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        min_product = nums[0]

        global_max = max_product

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            global_max = max(global_max, max_product)

        return global_max
