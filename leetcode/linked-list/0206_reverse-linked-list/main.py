from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def _entrypoint(self, head: Optional[List]):
        next_ = None
        for num in head[::-1]:
            next_ = ListNode(num, next_)

        return self.reverseList(next_)

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_ = curr.next

            curr.next = prev
            prev = curr
            curr = next_

        return self.linked_list_to_list(prev)
