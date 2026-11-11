from collections import deque

from .hash_table import HashTable


class HashTableWithLinkedList(HashTable):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    # Easy: hash.easy, the chain half of Put(head, key). key is the
    # slot b, data is the key, and each slot holds a deque, the chain.
    def _set_value(self, key, data) -> None:
        # Easy MAIN: head(i) <- nil until the first key lands in slot i
        self.values[key] = (
            deque() if self.values[key] is None else self.values[key]
        )
        # Easy Put: call GETNODE(p); info(p) <- key
        # Easy Put: link(p) <- head(b); head(b) <- p, a push at the front
        self.values[key].appendleft(data)
        # Not in Easy: keep the slot-to-chain map current
        self._keys[key] = self.values[key]

    def balanced_factor(self) -> float:
        return (
            sum(self.charge_factor - len(slot) for slot in self.values)
            / self.size_table
            * self.charge_factor
        )

    def _collision_resolution(self, key, data=None):
        if not (
            len(self.values[key]) == self.charge_factor and self.values.count(None) == 0
        ):
            return key
        return super()._collision_resolution(key, data)
