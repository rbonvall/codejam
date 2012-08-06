#!/usr/bin/env python

from functools import wraps
from math import factorial

def memoize(f):
    cache = {}
    @wraps(f)
    def g(*args):
        if args in cache:
            return cache[args]
        cache[args] = f(*args)
        return cache[args]
    return g

def count_sorted(values):
    return sum(1 for i, x in enumerate(values, 1) if i == x)

factorial = memoize(factorial)

@memoize
def T0(n):
    if n == 0:
        return 1
    return n * T0(n - 1) + (-1 if n & 1 else 1)

@memoize
def binom(n, k):
    if k == 0 or n == k:
        return 1
    if n == 0 or k > n:
        return 0
    return binom(n - 1, k - 1)  + binom(n - 1, k)

@memoize
def T(n, c):
    '''How many permutations of [1..n] have c elements in the right position'''
    if c == n:
        return 1
    if c == n - 1:
        return 0
    return T0(n - c) * binom(n, n - c)

@memoize
def E(n):
    if n == 0:
        return 0
    if n == 1:
        return 1 # whatever
    if n == 2:
        return 1
    factor = (factorial(n) - T0(n)) ** -1
    return factor * sum(T(n, i) * E(n - i) for i in range(1, n + 1))


def groups(seq):
    have_group = set()
    groups = []
    for i, x in enumerate(seq, 1):
        if i == x:
            have_group.add(x)
            groups.append({x})
        elif x not in have_group:
            # find x's group by cycling on the list
            new_group = set()
            n_i = i
            while True:
                new_group.add(n_i)
                n_i = seq[n_i - 1]
                if n_i == i:
                    break
            have_group |= new_group
            groups.append(new_group)
    return groups

def expected(n):


def solve(seq):
    gs = groups(seq)
    return sum(expected(len(g)) for g in gs)


def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        N = int(raw_input())
        values = map(int, raw_input().split())
        print 'Case #{0}: {1:.6f}'.format(t, solve(values))

if __name__ == '__main__':
    main()
    pass
