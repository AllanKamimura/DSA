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

        return self.deleteDuplicates(next_)

    def linked_list_to_list(self, head: ListNode) -> List:
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        fake_head = ListNode(-101, next=head)
        prev = fake_head
        left = head

        while left:
            if left.next and left.val == left.next.val:
                same = left.val

                while left and left.val == same:
                    left = left.next

                prev.next = left

            else:
                prev.next = left
                prev = left
                left = left.next

        return self.linked_list_to_list(fake_head.next)
