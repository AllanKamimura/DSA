from typing import List, Optional, Tuple


class ListNode:
    """ "
    head -> 1 -> 2 -> 3 -> 4 -> 5

    right = head

    0: right = 1
    1: right = 2
    2: right = 3

    left = head

    i: prev = 3, right = 4, left = 1
    i: prev = 4, right = 5, left = 2
    i: prev = 5, right = None, left = 3

    old_head = 1
    head.next = 4
    left.next = 3 -> None
    prev.next = 5 -> 1

    """

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"


class Solution:
    def _entrypoint(
        self,
        list1: List[Tuple[int, int]],
        list2: List[Tuple[int, int]],
    ) -> Optional[List[int]]:
        next1 = None
        for num in list1[::-1]:
            next1 = ListNode(num, next1)

        next2 = None
        for num in list2[::-1]:
            next2 = ListNode(num, next2)

        return self.mergeTwoLists(next1, next2)

    def linked_list_to_list(self, head: ListNode) -> List:
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        start = ListNode(0)
        curr_head = start

        while list1 and list2:
            if list1.val < list2.val:
                curr_head.next = list1
                list1 = list1.next
            else:
                curr_head.next = list2
                list2 = list2.next

            curr_head = curr_head.next

        if list1:
            curr_head.next = list1
        if list2:
            curr_head.next = list2

        return self.linked_list_to_list(start.next)
