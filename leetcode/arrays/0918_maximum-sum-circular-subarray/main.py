from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        curr_sum = nums[0]
        max_sum = curr_sum

        curr_sum_negative = nums[0]
        min_sum = curr_sum_negative

        total = curr_sum

        for i in range(1, n):
            num = nums[i]

            total += num

            if curr_sum > 0:
                curr_sum += num
            else:
                curr_sum = num

            if curr_sum_negative > 0:
                curr_sum_negative = num
            else:
                curr_sum_negative += num

            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum_negative < min_sum:
                min_sum = curr_sum_negative

        if total == min_sum:
            return max_sum
        else:
            return max(max_sum, (total - min_sum))
