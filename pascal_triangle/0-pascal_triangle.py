#!/usr/bin/python3
""" Pascal's Triangle."""


def pascal_triangle(a):
    """Generate Pascal's Triangle up to row 'a'"""
    if a <= 0:
        return []
    triangle = [[1]]
    for i in range(1, a):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
