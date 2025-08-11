from typing import List, Optional


class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def _entrypoint(self, head: Optional[List], n: int):
        next_ = None
        for num in head[::-1]:
            next_ = ListNode(num, next_)

        return self.removeNthFromEnd(next_, n)

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Add dummy node before head
        fast = dummy
        slow = dummy

        # Move fast n+1 steps ahead to maintain a gap
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the nth node
        slow.next = slow.next.next

        # return dummy.next
        return self.linked_list_to_list(dummy.next)
