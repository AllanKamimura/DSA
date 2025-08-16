from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def _entrypoint(
        self, head: Optional[List[Tuple[int, int]]], x: int
    ) -> Optional[List[int]]:
        next_ = None
        for num in head[::-1]:
            next_ = ListNode(num, next_)

        return self.partition(next_, x)

    def linked_list_to_list(self, head: ListNode) -> List:
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_less = ListNode(0)
        head_great = ListNode(0)

        head_less_add = head_less
        head_great_add = head_great

        while head:
            next = head.next

            if head.val < x:
                head_less_add.next = head
                head_less_add = head_less_add.next

            else:
                head_great_add.next = head
                head_great_add = head_great_add.next

            head = next

        head_great_add.next = None
        head_less_add.next = head_great.next

        return self.linked_list_to_list(head_less.next)
