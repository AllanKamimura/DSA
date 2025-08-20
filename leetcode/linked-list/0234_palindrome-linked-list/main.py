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

        return self.isPalindrome(next_)

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_ = curr.next

            curr.next = prev
            prev = curr
            curr = next_

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0

        fast = head
        slow = head
        switch = True

        while fast:
            fast = fast.next
            if switch:
                slow = slow.next
            switch = not switch

        reversed_head = self.reverseList(slow)

        left = head
        right = reversed_head

        while left and right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
