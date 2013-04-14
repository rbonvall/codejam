#!/usr/bin/env python

from math import floor, ceil, sqrt

def invert(i):
    return int(str(i)[::-1])

def is_palindrome(i):
    return i == invert(i)

def split_number(i):
    '''
    >>> split_number(1234)
    (12, 34)
    >>> split_number(12345)
    (123, 345)
    '''

    n = len(str(i))
    s = str(i)
    return (int(s[      :n // 2 + n % 2]),
            int(s[n // 2:              ]))

def next_palindrome(i):
    # i isn't necessarily a palindrome
    s = str(i)
    n = len(s)

    # ugly corner case
    if s == '9' * n:
        return i + 2

    first_half, second_half = split_number(i)
    if second_half >= invert(first_half):
        first_half += 1
    h = str(first_half)
    if n % 2 == 0:
        return int(h + h[::-1].zfill(len(h)))
    else:
        return int(h[:-1] + h[::-1].zfill(len(h)))

def palindromes_between(a, b):
    p = next_palindrome(a - 1)
    while p <= b:
        yield p
        p = next_palindrome(p)

def solve(A, B):
    a = int(ceil(sqrt(A)))
    b = int(floor(sqrt(B)))
    return sum(1 for n in palindromes_between(a, b)
                 if is_palindrome(n ** 2))

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        A, B = map(int, raw_input().split())
        print "Case #{}: {}".format(t, solve(A, B))


if __name__ == '__main__':
    main()

