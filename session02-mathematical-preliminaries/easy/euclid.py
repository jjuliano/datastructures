"""Euclid's remainder loop, the Python twin of euclid.easy.

Original, written for The Data Structures Notebook. MIT, copyright (c)
2026 Joel Bryan Juliano. See LICENSE-EASY.md.

>>> gcd(48, 18)
6
>>> gcd(608, 133)
19
"""


# Easy: euclid.easy, procedure GCD(a, b).
# The arguments are copies, so the caller's names stay put.
def gcd(a: int, b: int) -> int:
    # Easy GCD: while b != 0 do
    while b != 0:
        # Easy GCD: r <- a mod b
        r = a % b
        # Easy GCD: a <- b; b <- r
        a = b
        b = r
    # Easy GCD: return(a)
    return a


# Easy: euclid.easy, procedure MAIN.
if __name__ == "__main__":
    # Easy MAIN: output GCD(48, 18)
    print(gcd(48, 18))
    # Easy MAIN: output GCD(608, 133)
    print(gcd(608, 133))
