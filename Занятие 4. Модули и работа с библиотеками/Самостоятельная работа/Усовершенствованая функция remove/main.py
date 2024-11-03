# TODO написать функцию remove
from typing import Any


def remove(l: list, val: Any):
    if not val in l:
        raise ValueError("Element not in the list")
    new_l = l[::-1]
    new_l.remove(val)
    return new_l[::-1]


print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
