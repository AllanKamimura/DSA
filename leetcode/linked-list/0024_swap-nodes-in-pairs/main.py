from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def _entrypoint(self, head: Optional[List[int]]) -> Optional[List[int]]:
        next_ = None
        for num in head[::-1]:
            next_ = ListNode(num, next_)

        return self.swapPairs(next_)

    def linked_list_to_list(self, head: ListNode) -> List:
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_head = ListNode(0, head)

        prev = fake_head
        curr = prev.next

        while curr:
            if curr and curr.next:
                next = curr.next

                curr.next = next.next
                next.next = curr
                prev.next = next

                prev = curr
                curr = curr.next

            elif curr and not curr.next:
                curr = curr.next

        return self.linked_list_to_list(fake_head.next)
