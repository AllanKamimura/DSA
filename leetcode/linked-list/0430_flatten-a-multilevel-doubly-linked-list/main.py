from typing import Optional


class ListNode:
    def __init__(
        self,
        val: int,
        prev: "Optional[ListNode]" = None,
        next: "Optional[ListNode]" = None,
        child: "Optional[ListNode]" = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self) -> str:
        return f"{self.val}"


class Solution:
    def get_tail(self, head: "Optional[ListNode]") -> "Optional[ListNode]":
        curr = head
        while curr:
            if curr.child:
                parent_curr = curr
                child_tail = self.get_tail(parent_curr.child)

                next_ = parent_curr.next

                parent_curr.next = parent_curr.child
                parent_curr.child.prev = parent_curr
                parent_curr.child = None

                child_tail.next = next_
                if next_:
                    next_.prev = child_tail

            if not curr.next:
                return curr
            curr = curr.next

    def flatten(self, head: "Optional[ListNode]") -> "Optional[ListNode]":
        if not head:
            return head
        self.get_tail(head)
        return head
