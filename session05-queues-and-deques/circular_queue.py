# Implementation of Circular Queue (using Python lists)


class CircularQueue:
    """Circular FIFO queue with a fixed capacity"""

    # Easy: ring.easy, array q(1:n) with front and count. Python counts
    # from 0 and keeps rear, the next free cell, where Easy computes it.
    def __init__(self, n: int) -> None:
        self.n = n
        # Easy: array q(1:n)
        self.array = [None] * self.n
        self.front = 0  # index of the first element
        # Easy: rear is ((front - 1 + count) mod n) + 1, kept up to date
        self.rear = 0
        # Easy MAIN: count <- 0
        self.size = 0

    def __len__(self) -> int:
        """
        >>> cq = CircularQueue(5)
        >>> len(cq)
        0
        >>> cq.enqueue("A")  # doctest: +ELLIPSIS
        <data_structures.queues.circular_queue.CircularQueue object at ...>
        >>> cq.array
        ['A', None, None, None, None]
        >>> len(cq)
        1
        """
        return self.size

    def is_empty(self) -> bool:
        """
        Checks whether the queue is empty or not
        >>> cq = CircularQueue(5)
        >>> cq.is_empty()
        True
        >>> cq.enqueue("A").is_empty()
        False
        """
        return self.size == 0

    def first(self):
        """
        Returns the first element of the queue
        >>> cq = CircularQueue(5)
        >>> cq.first()
        False
        >>> cq.enqueue("A").first()
        'A'
        """
        return False if self.is_empty() else self.array[self.front]

    # Easy: ring.easy, procedure Enqueue(q, n, front, count, x).
    def enqueue(self, data) -> "CircularQueue":
        """
        This function inserts an element at the end of the queue using self.rear value
        as an index.

        >>> cq = CircularQueue(5)
        >>> cq.enqueue("A")  # doctest: +ELLIPSIS
        <data_structures.queues.circular_queue.CircularQueue object at ...>
        >>> (cq.size, cq.first())
        (1, 'A')
        >>> cq.enqueue("B")  # doctest: +ELLIPSIS
        <data_structures.queues.circular_queue.CircularQueue object at ...>
        >>> cq.array
        ['A', 'B', None, None, None]
        >>> (cq.size, cq.first())
        (2, 'A')
        >>> cq.enqueue("C").enqueue("D").enqueue("E")  # doctest: +ELLIPSIS
        <data_structures.queues.circular_queue.CircularQueue object at ...>
        >>> cq.enqueue("F")
        Traceback (most recent call last):
           ...
        Exception: QUEUE IS FULL
        """
        # Easy Enqueue: if count = n then [ output "full"; stop ]
        if self.size >= self.n:
            raise Exception("QUEUE IS FULL")

        # Easy Enqueue: slot <- ((front - 1 + count) mod n) + 1
        # Easy Enqueue: q(slot) <- x
        self.array[self.rear] = data
        # Not in Easy: step rear, so the next free slot is ready
        self.rear = (self.rear + 1) % self.n
        # Easy Enqueue: count <- count + 1
        self.size += 1
        # Not in Easy: return the queue so calls can chain
        return self

    # Easy: ring.easy, procedure Dequeue(q, n, front, count, x).
    def dequeue(self):
        """
        This function removes an element from the queue using on self.front value as an
        index and returns it

        >>> cq = CircularQueue(5)
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: UNDERFLOW
        >>> cq.enqueue("A").enqueue("B").dequeue()
        'A'
        >>> (cq.size, cq.first())
        (1, 'B')
        >>> cq.dequeue()
        'B'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: UNDERFLOW
        """
        # Easy Dequeue: if count = 0 then [ output "empty"; stop ]
        if self.size == 0:
            raise Exception("UNDERFLOW")

        # Easy Dequeue: x <- q(front)
        temp = self.array[self.front]
        # Not in Easy: clear the cell so the old value can be freed
        self.array[self.front] = None
        # Easy Dequeue: front <- (front mod n) + 1
        self.front = (self.front + 1) % self.n
        # Easy Dequeue: count <- count - 1
        self.size -= 1
        return temp
