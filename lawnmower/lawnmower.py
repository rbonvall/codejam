#!/usr/bin/env python

import numpy

def possible(lawn):
    a = numpy.array(lawn)
    rows, cols = a.shape
    for i in range(rows):
        for j in range(cols):
            if a[i, j] != a.max(1)[i] and a[i, j] != a.max(0)[j]:
                return 'NO'
    return 'YES'

def read_ints():
    return map(int, raw_input().split())

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        N, M = read_ints()
        lawn = []
        for n in range(N):
            lawn.append(read_ints())
        print 'Case #{}: {}'.format(t, possible(lawn))

if __name__ == '__main__':
    main()

