#!/usr/bin/python3
"""Pascal triangle."""


def pascal_triangle(n):
    """Pascal's triangle of n."""
    if n <= 0:
        return []

    ret = [[1]]
    for row in range(1, n):
        newRow = ret[row - 1].copy()
        newRow.append(1)
        for ele in range(0, len(ret[row - 1])):
            if row - 1 >= 0 and ele - 1 >= 0:
                newRow[ele] = ret[row - 1][ele - 1] + ret[row - 1][ele]
        ret.append(newRow)

    return ret
