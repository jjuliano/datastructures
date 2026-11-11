"""Towers of Hanoi, the Python twin of hanoi.easy.

Original, written for The Data Structures Notebook. MIT, copyright (c)
2026 Joel Bryan Juliano. See LICENSE-EASY.md.

Each line names the peg the disk leaves and the peg it lands on.

>>> move(3, "A", "B", "C")
A B
A C
B C
A B
C A
C B
A B
"""


# Easy: hanoi.easy, procedure Move(n, src, dst, spare).
def move(n: int, src: str, dst: str, spare: str) -> None:
    # Easy Move: if n = 1 then output src dst
    if n == 1:
        print(src, dst)
    # Easy Move: else [ ... ]
    else:
        # Easy Move: call Move(n - 1, src, spare, dst)
        move(n - 1, src, spare, dst)
        # Easy Move: output src dst
        print(src, dst)
        # Easy Move: call Move(n - 1, spare, dst, src)
        move(n - 1, spare, dst, src)


# Easy: hanoi.easy, procedure MAIN.
if __name__ == "__main__":
    # Easy MAIN: call Move(3, "A", "B", "C")
    move(3, "A", "B", "C")
