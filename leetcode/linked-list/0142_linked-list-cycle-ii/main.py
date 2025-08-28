from typing import List, Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def _entrypoint(self, head: List[int], pos: int) -> int:
        """
        Build the linked list from `head`, create a cycle by connecting the tail
        to the node at index `pos` (or no cycle if pos == -1), run detectCycle,
        and return the index of the cycle entry (or -1 if no cycle).
        """
        if not head:
            return -1

        # 1) Build nodes in order and remember their indices
        nodes: List[ListNode] = []
        for val in head:
            nodes.append(ListNode(val))
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        head_node = nodes[0]

        # 2) Create the cycle if pos != -1
        if pos != -1:
            nodes[-1].next = nodes[pos]

        # 3) Run detectCycle and map node back to index
        start = self.detectCycle(head_node)
        if start is None:
            return -1

        # Map identity of nodes to indices to avoid O(n) search
        index_by_node = {node: idx for idx, node in enumerate(nodes)}
        return index_by_node.get(start, -1)

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return None

        slow = head
        fast = head.next
        i = 1
        cycle = False
        while fast.next and fast.next.next:
            if fast == slow:
                cycle = True
                break

            i += 1
            slow = slow.next
            fast = fast.next.next

        if not cycle:
            return None

        look_ahead = head

        for _ in range(i):
            look_ahead = look_ahead.next

        curr = head

        while curr != look_ahead:
            curr = curr.next
            look_ahead = look_ahead.next

        return curr
