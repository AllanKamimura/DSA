from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def _entrypoint(self, head: Optional[List[Tuple[int, int]]]) -> Optional[List[int]]:
        next_ = None
        for num, random in head[::-1]:
            next_ = ListNode(num, next_, random)

        return self.copyRandomList(next_)

    def linked_list_to_list(self, head: ListNode) -> List:
        result = []
        curr = head
        while curr is not None:
            result.append((curr.val, curr.random))
            curr = curr.next
        return result

    def copyRandomList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr:
            next = curr.next
            curr.next = ListNode(val=curr.val)
            curr.next.next = next

            curr = next

        curr = head

        while curr:
            next = curr.next

            if curr.random:
                # the node next to the curr.random is in the new list
                next.random = curr.random.next
            else:
                next.random = None

            curr = next.next

        fake_head_add = ListNode(0)
        fake_head = ListNode(0, next=fake_head_add)

        curr = head

        while curr:
            next = curr.next

            fake_head_add.next = next
            fake_head_add = fake_head_add.next

            curr = next.next

        return self.linked_list_to_list(fake_head.next.next)
