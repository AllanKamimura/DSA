from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup_table = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                smaller_num = stack.pop()
                lookup_table[smaller_num] = num

            stack.append(num)

        while stack:
            big_num = stack.pop()
            lookup_table[big_num] = -1

        output = [lookup_table[num] for num in nums1]

        return output
