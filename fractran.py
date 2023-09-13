from typing import List, Tuple

def is_divisible(num: int, den: int) -> bool:
    return num % den == 0

def fractran(fractions: List[Tuple[int, int]], n: int) -> int:
    ended: bool = False
    print(n)
    while not ended:
        ended = True
        for (num, den) in fractions:
            if is_divisible(n, den):
                n = (n // den) * num
                ended = False
                break

    return n
