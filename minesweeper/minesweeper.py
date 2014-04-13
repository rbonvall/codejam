#!/usr/bin/env python

def transpose(matrix):
    return zip(*matrix)

def solve(R, C, M):
    # trivial cases dependent on M
    if M == 0:
        sol = map(list, ['.' * C] * R)
        sol[0][0] = 'c'
        return sol
    if M == R * C - 1:
        sol = map(list, ['*' * C] * R)
        sol[0][0] = 'c'
        return sol

    if R > C:
        return transpose(solve(C, R, M))

    assert R <= C
    assert 1 <= M < R * C - 1
    if R == 1:
        return [list('c' + (C - M - 1) * '.' + M * '*' )]
    if R == 2:
        if M == R * C - 2 or M % 2 == 1:
            return None
        else:
            return map(list, [
                'c' + (C - M/2 - 1) * '.' + (M/2 * '*'),
                      (C - M/2)     * '.' + (M/2 * '*'),
            ])
    if M == R + C - 1:
        sol = solve(R - 1, C - 1, M - (R + C - 1))
        if sol is None: return None
        return [row + ['*'] for x in row] + list(C * '*')
    if M >= R:
        sol = solve(R, C - 1, M - (R + C - 1))


    return [['.'] * C] * R


def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        R, C, M = map(int, raw_input().split())
        board = solve(R, C, M)

        print 'Case #{}:'.format(t)
        if board is None:
            print 'Impossible'
        else:
            print '\n'.join(''.join(cells) for cells in board)

if __name__ == '__main__':
    main()

