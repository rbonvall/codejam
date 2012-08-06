#!/usr/bin/env python

def avg(xs):
    return float(sum(xs)) / len(xs)

def compute_rpis(lines):
    n = len(lines)
    wins = [s.count('1') for s in lines]
    losses = [s.count('0') for s in lines]

    opponents = [[i for i, r in enumerate(s) if r != '.']
                 for s in lines]

    wps = [float(w) / (w + l) for w, l in zip(wins, losses)]

    owps = []
    for team in range(n):
        # compute wps of opponents without team
        op_lines = [s[:team] + '.' + s[team  + 1:] for s in lines]
        op_wins = [s.count('1') for s in op_lines]
        op_losses = [s.count('0') for s in op_lines]
        op_wps = [float(w) / (w + l) for w, l in zip(op_wins, op_losses)]
        owps.append(avg([op_wps[op] for op in opponents[team]]))

    oowps = [avg([owps[op] for op in opponents[team]]) for team in range(n)]

    return [.25 * wp + .5 * owp + .25 * oowp
            for wp, owp, oowp in zip(wps, owps, oowps)]

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        N = int(raw_input())
        lines = []
        for n in range(N):
            lines.append(raw_input())
        rpis = compute_rpis(lines)
        print 'Case #{0}:'.format(t)
        for rpi in rpis:
            print '{0:.10f}'.format(rpi)

if __name__ == '__main__':
    main()
