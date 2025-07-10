from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1
        curr_index = m + n - 1

        while first >= 0 and second >= 0:
            first_value = nums1[first]
            second_value = nums2[second]

            if first_value >= second_value:
                nums1[curr_index] = first_value
                first -= 1

            else:
                nums1[curr_index] = second_value
                second -= 1

            curr_index -= 1

        while second >= 0:
            second_value = nums2[second]
            nums1[curr_index] = second_value
            second -= 1

            curr_index -= 1

        return nums1
