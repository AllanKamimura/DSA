from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) < 2:
            return [-1] * len(nums1)

        sentinel = 10001  # constrain: 0 <= nums1[i], nums2[i] <= 10^4
        lookup_table = {nums2[-1]: sentinel}

        last_num = nums2[-1]

        for num in nums2[-2::-1]:
            while last_num < num:
                last_num = lookup_table[last_num]

            lookup_table[num] = last_num
            last_num = num

        output = [
            lookup_table[num] if lookup_table[num] != sentinel else -1 for num in nums1
        ]

        return output
