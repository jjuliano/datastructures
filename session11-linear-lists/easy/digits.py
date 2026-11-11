"""Long addition on digit rows, the Python twin of digits.easy.

Original, written for The Data Structures Notebook. MIT, copyright (c)
2026 Joel Bryan Juliano. See LICENSE-EASY.md.

Digits sit low to high. 99 is [9, 9]. Adding 1 yields [0, 0, 1].
Easy counts cells from 1. Python counts from 0, so cell i is a[i - 1].

>>> add([9, 9], [1])
[0, 0, 1]
>>> add([5], [7])
[2, 1]
"""


# Easy: digits.easy, procedure Add(a, na, b, nb, c, nc).
# len(a) is na, len(b) is nb, and len(c) is nc when the loop ends.
def add(a: list[int], b: list[int]) -> list[int]:
    na = len(a)
    nb = len(b)
    c: list[int] = []
    # Easy Add: i <- 1; carry <- 0
    i = 1
    carry = 0
    # Easy Add: while i <= na or i <= nb or carry != 0 do
    while i <= na or i <= nb or carry != 0:
        # Easy Add: da <- 0; db <- 0
        da = 0
        db = 0
        # Easy Add: if i <= na then da <- a(i)
        if i <= na:
            da = a[i - 1]
        # Easy Add: if i <= nb then db <- b(i)
        if i <= nb:
            db = b[i - 1]
        # Easy Add: sum <- da + db + carry
        total = da + db + carry
        # Easy Add: c(i) <- sum mod 10
        c.append(total % 10)
        # Easy Add: carry <- floor(sum / 10)
        carry = total // 10
        # Easy Add: i <- i + 1
        i += 1
    # Easy Add: nc <- i - 1, which is len(c)
    return c


# Easy: digits.easy, procedure MAIN.
if __name__ == "__main__":
    # Easy MAIN: a is 9, 9 and b is 1; call Add(a, 2, b, 1, c, nc)
    c = add([9, 9], [1])
    # Easy MAIN: output c(1) c(2) c(3)
    print(*c)
