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
        self, head: Optional[List[Tuple[int, int]]], k: int
    ) -> Optional[List[int]]:
        next_ = None
        for num in head[::-1]:
            next_ = ListNode(num, next_)

        return self.rotateRight(next_, k)

    def linked_list_to_list(self, head: ListNode) -> List:
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0

        while curr:
            curr = curr.next
            n += 1

        if n == 0:
            return head

        k %= n

        if k == 0:
            return head

        right = head

        for _ in range(k):
            right = right.next

        left = head

        while right.next:
            right = right.next
            left = left.next

        new_head = left.next
        right.next = head
        left.next = None

        return self.linked_list_to_list(new_head)
