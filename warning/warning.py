#!python3

from fractions import gcd
from functools import reduce

def gcd_n(l):
    return reduce(gcd, l, l[0])

def y(t):
    t.sort()
    differences = [y - x for x, y in zip(t, t[1:])]
    g = gcd_n(differences)
    return (g - (t[0] % g)) % g

def main():
    C = int(input())

    for i in range(1, C + 1):
        N, *t = map(int, input().split())
        print("Case #{}: {}".format(i, y(t)))

if __name__ == '__main__':
    main()

