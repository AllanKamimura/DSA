from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"


class Solution:
    def _entrypoint(
        self,
        l1: Optional[List[Tuple[int, int]]],
        l2: Optional[List[Tuple[int, int]]],
    ) -> Optional[List[int]]:
        next1 = None
        for num in l1[::-1]:
            next1 = ListNode(num, next1)

        next2 = None
        for num in l2[::-1]:
            next2 = ListNode(num, next2)

        return self.addTwoNumbers(next1, next2)

    def linked_list_to_list(self, head: ListNode) -> List:
        result = []
        curr = head
        while curr is not None:
            result.append(curr.val)
            curr = curr.next
        return result

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head1 = l1
        head2 = l2

        new_head = ListNode(0)
        add_head = new_head

        carry_number = 0

        while (head1) or (head2) or carry_number:
            n1 = head1.val if head1 else 0
            n2 = head2.val if head2 else 0

            carry_number, n_new = divmod((n1 + n2 + carry_number), 10)

            add_head.next = ListNode(n_new)
            add_head = add_head.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        return self.linked_list_to_list(new_head.next)
