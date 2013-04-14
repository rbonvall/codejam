#!/usr/bin/env python

from itertools import chain

def status(b):
    rows = b
    cols = map(''.join, zip(*b))
    diag1 = ''.join(b[i][i]     for i in range(4))
    diag2 = ''.join(b[i][3 - i] for i in range(4))

    items = chain(rows, cols, [diag1, diag2])
    sets = map(set, items)

    x_wins = [{'X', 'T'}, {'X'}].__contains__
    o_wins = [{'O', 'T'}, {'O'}].__contains__
    if any(x_wins(s) for s in sets):
        return 'X won'
    elif any(o_wins(s) for s in sets):
        return 'O won'
    elif any('.' in s for s in sets):
        return 'Game has not completed'
    return 'Draw'


def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        board = [raw_input() for _ in range(4)]
        raw_input()
        print 'Case #{}: {}'.format(t, status(board))

if __name__ == '__main__':
    main()

