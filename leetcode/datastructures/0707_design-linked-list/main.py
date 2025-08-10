from typing import Iterator, Optional


class ListNode:
    def __init__(self, x, next=None, prev=None):
        self.val = x
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.val}"


class MyLinkedList:
    def __init__(self):
        self.fake_head = ListNode(0)
        self.fake_tail = ListNode(0)
        self.fake_head.next = self.fake_tail
        self.fake_tail.prev = self.fake_head
        self.length = 0

    def __str__(self) -> str:
        vals = list(self)
        return " -> ".join(map(str, vals)) if vals else "[]"

    def __len__(self) -> int:
        return self.length

    def iter_nodes(self) -> Iterator["ListNode"]:
        """Yield real nodes (skip sentinels)."""
        node = self.fake_head.next
        while node is not self.fake_tail:
            yield node
            node = node.next

    def __iter__(self) -> Iterator[int]:
        """Yield values (user-facing)."""
        for node in self.iter_nodes():
            yield node.val

    def _node_at(self, index) -> Optional[ListNode]:
        if index < 0 or index >= self.length:
            return None

        node = self.fake_head.next
        for _ in range(index):
            if node is None:
                return None
            node = node.next
        return node

    def _prev_node_at(self, index: int) -> Optional[ListNode]:
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.fake_head

        return self._node_at(index - 1)

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        else:
            node = self._node_at(index)
            return node.val

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val, next=self.fake_head.next, prev=self.fake_head)

        if self.fake_head.next:
            self.fake_head.next.prev = new_node

        self.fake_head.next = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val, next=self.fake_tail, prev=self.fake_tail.prev)

        if self.fake_tail.prev:
            self.fake_tail.prev.next = new_node

        self.fake_tail.prev = new_node

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index > self.length:
            return
        else:
            left = self._prev_node_at(index)
            next = left.next
            new_node = ListNode(val, next=next, prev=left)

            if next:
                next.prev = new_node

            left.next = new_node

            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
            left = self._prev_node_at(index)

            del_node = left.next
            next = del_node.next

            left.next = next
            next.prev = left

            del del_node

            self.length -= 1
