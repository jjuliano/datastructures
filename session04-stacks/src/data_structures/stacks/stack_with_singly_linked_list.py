"""A Stack using a linked list like structure"""

from __future__ import annotations

from collections.abc import Iterator
from typing import TypeVar

T = TypeVar("T")


# Easy: linked_pile.easy, node(info, link). data is info, next is link.
class Node[T]:
    def __init__(self, data: T) -> None:
        self.data = data
        self.next: Node[T] | None = None

    def __str__(self) -> str:
        return f"{self.data}"


class LinkedStack[T]:
    """
    Linked List Stack implementing push (to top),
    pop (from top) and is_empty

    >>> stack = LinkedStack()
    >>> stack.is_empty()
    True
    >>> stack.push(5)
    >>> stack.push(9)
    >>> stack.push('python')
    >>> stack.is_empty()
    False
    >>> stack.pop()
    'python'
    >>> stack.push('algorithms')
    >>> stack.pop()
    'algorithms'
    >>> stack.pop()
    9
    >>> stack.pop()
    5
    >>> stack.is_empty()
    True
    >>> stack.pop()
    Traceback (most recent call last):
        ...
    IndexError: pop from empty stack
    """

    # Easy MAIN: top <- nil
    def __init__(self) -> None:
        self.top: Node[T] | None = None

    def __iter__(self) -> Iterator[T]:
        node = self.top
        while node:
            yield node.data
            node = node.next

    def __str__(self) -> str:
        """
        >>> stack = LinkedStack()
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> str(stack)
        'a->b->c'
        """
        return "->".join([str(item) for item in self])

    def __len__(self) -> int:
        """
        >>> stack = LinkedStack()
        >>> len(stack) == 0
        True
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> len(stack) == 3
        True
        """
        return len(tuple(iter(self)))

    def is_empty(self) -> bool:
        """
        >>> stack = LinkedStack()
        >>> stack.is_empty()
        True
        >>> stack.push(1)
        >>> stack.is_empty()
        False
        """
        return self.top is None

    # Easy: linked_pile.easy, procedure Push(top, x).
    def push(self, item: T) -> None:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Python")
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> str(stack)
        'C->Java->Python'
        """
        # Easy Push: call GETNODE(p); info(p) <- x
        node = Node(item)
        # Easy Push: link(p) <- top. On an empty stack next stays None,
        # which is the nil that top already holds.
        if not self.is_empty():
            node.next = self.top
        # Easy Push: top <- p
        self.top = node

    # Easy: linked_pile.easy, procedure Pop(top, x).
    def pop(self) -> T:
        """
        >>> stack = LinkedStack()
        >>> stack.pop()
        Traceback (most recent call last):
            ...
        IndexError: pop from empty stack
        >>> stack.push("c")
        >>> stack.push("b")
        >>> stack.push("a")
        >>> stack.pop() == 'a'
        True
        >>> stack.pop() == 'b'
        True
        >>> stack.pop() == 'c'
        True
        """
        # Not in Easy: Pop trusts its caller not to pop an empty chain.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        assert isinstance(self.top, Node)
        # Easy Pop: old <- top
        pop_node = self.top
        # Easy Pop: top <- link(top)
        self.top = self.top.next
        # Easy Pop: x <- info(old). The garbage collector does RETNODE(old).
        return pop_node.data

    def peek(self) -> T:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> stack.push("Python")
        >>> stack.peek()
        'Python'
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")

        assert self.top is not None
        return self.top.data

    def clear(self) -> None:
        """
        >>> stack = LinkedStack()
        >>> stack.push("Java")
        >>> stack.push("C")
        >>> stack.push("Python")
        >>> str(stack)
        'Python->C->Java'
        >>> stack.clear()
        >>> len(stack) == 0
        True
        """
        self.top = None


if __name__ == "__main__":
    from doctest import testmod

    testmod()
