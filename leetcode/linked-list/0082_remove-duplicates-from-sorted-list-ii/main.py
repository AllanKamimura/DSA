from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def _entrypoint(self, head: Optional[List[int]]):
        next_ = None
        for num in head[::-1]:
            next_ = ListNode(num, next_)

        return self.deleteDuplicates(next_)

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        fake_head_add = ListNode(-101)
        fake_head = ListNode(-101, next=fake_head_add)
        left = head
        right = left.next
        prev = fake_head

        while right:
            if left.val == right.val:
                prev = left
                left = right.next
                if not left:
                    break
                right = left.next

            else:
                if left.val != prev.val:
                    left.next = None
                    fake_head_add.next = left
                    fake_head_add = fake_head_add.next

                prev = left
                left = right
                right = left.next

        if left:
            if left.val != prev.val:
                left.next = None
                fake_head_add.next = left
                fake_head_add = fake_head_add.next

        return self.linked_list_to_list(fake_head.next.next)
