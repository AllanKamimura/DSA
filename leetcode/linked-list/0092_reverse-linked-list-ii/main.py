from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def _entrypoint(self, head: Optional[List], left: int, right: int):
        next_ = None
        for num in head[::-1]:
            next_ = ListNode(num, next_)

        return self.reverseBetween(next_, left, right)

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def reverse_linked_list(self, head, max_iter):
        curr = head
        prev = None
        j = 0
        while curr and (j < max_iter):
            next_ = curr.next

            curr.next = prev
            prev = curr
            curr = next_

            j += 1

        return prev, curr

    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        curr = head
        prev_head = ListNode(0, next=curr)
        prev = prev_head
        i = 1
        max_iter = right - left + 1
        while curr:
            if i == left:
                right_node, right_next = self.reverse_linked_list(curr, max_iter)
                prev.next = right_node
                curr.next = right_next
            else:
                prev = curr

            curr = curr.next
            i += 1

        return self.linked_list_to_list(prev_head.next)
