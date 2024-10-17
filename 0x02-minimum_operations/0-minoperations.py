#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Minimum Operations needed to get n characters from single character"""
    next = 1
    current = 1
    op = 0
    while current < n:
        if n % current == 0:
            op += 2
            next = current
            current += current
        else:
            op += 1
            current += next
    if current != n:
        return 0
    return op
