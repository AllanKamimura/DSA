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

        return self.middleNode(next_)

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next:  # If there are two middle nodes, return the second middle node.
            slow = slow.next

        return self.linked_list_to_list(slow)
