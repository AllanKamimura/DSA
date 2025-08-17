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

        over_number = 0

        while (head1) and (head2):
            n1 = head1.val
            n2 = head2.val

            n_new = (n1 + n2 + over_number) % 10
            over_number = (n1 + n2 + over_number) // 10

            add_head.next = ListNode(n_new)
            add_head = add_head.next
            head1 = head1.next
            head2 = head2.next

        if (head1) or (head2):
            remainder_head = head1 if head1 else head2

            while remainder_head:
                n = remainder_head.val

                n_new = (n + over_number) % 10
                over_number = (n + over_number) // 10

                add_head.next = ListNode(n_new)
                add_head = add_head.next
                remainder_head = remainder_head.next

        if over_number:
            add_head.next = ListNode(over_number)
            add_head = add_head.next

        return self.linked_list_to_list(new_head.next)
