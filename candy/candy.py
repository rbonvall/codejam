#!/usr/bin/env python

from operator import xor as xor_op

def xor(values):
    return reduce(xor_op, values)

def bits(n, length):
    return map(int, bin(n)[2:].zfill(length))

def piles(mask, C):
    sean, patrick = [], []
    for c, m in zip(C, mask):
        (sean if m else patrick).append(c)
    return sean, patrick

def solve(C):
    C.sort()
    N = len(C)
    max_value = 0
    i = 1
    while i < 2 ** (N - 1):
        mask = bits(i, N)
        sean, patrick = piles(mask, C)
        if xor(sean) == xor(patrick):
            max_value = max(max_value, sum(sean), sum(patrick))
        i += 1
    return max_value

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        N = int(raw_input())
        C = map(int, raw_input().split())
        max_value = solve(C)
        print "Case #{0}: {1}".format(t, max_value if max_value else 'NO')


if __name__ == '__main__':
    main()
