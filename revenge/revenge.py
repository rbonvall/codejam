#!/usr/bin/env python

from numpy import *
from scipy.optimize import fmin
from functools import partial

def take_time(center, positions, D):
    N = positions.size
    span = float(D * (N - 1))
    final_positions = linspace(center - span/2, center + span/2, N)

    #lhalf = int(floor(N/2.))
    #hhalf = int(ceil(N/2.))
    #final_positions[:lhalf] = where(positions[:lhalf] < final_positions[:lhalf], positions[:lhalf], final_positions[:lhalf])
    #final_positions[hhalf:] = where(positions[hhalf:] > final_positions[hhalf:], positions[hhalf:], final_positions[hhalf:])

    return (abs(final_positions - positions)).max()

def min_time(positions, D):
    x0 = positions[0]
    x1 = positions[-1]

    f = partial(take_time, positions=positions, D=D)
    result = fmin(f, float(x0 + x1)/2, ftol=5e-6, disp=0)
    return f(result[0])

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        C, D = map(int, raw_input().split())
        positions = []
        for c in range(C):
            P, V = map(int, raw_input().split())
            positions.extend([P] * V)

        m = min_time(array(positions), D)
        print 'Case #{0}: {1:.10f}'.format(t, m)

if __name__ == '__main__':
    main()

