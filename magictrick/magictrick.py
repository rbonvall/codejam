#!/usr/bin/env python

def solve(a1, m1, a2, m2):
    return set(m1[a1 - 1]) & set(m2[a2 - 1])

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        first_answer = int(raw_input())
        first_arrangement = [map(int, raw_input().split()) for _ in range(4)]
        second_answer = int(raw_input())
        second_arrangement = [map(int, raw_input().split()) for _ in range(4)]

        cards = solve(first_answer,  first_arrangement,
                      second_answer, second_arrangement)

        if len(cards) == 0:
            print 'Case #{0}: Volunteer cheated!'.format(t)
        elif len(cards) == 1:
            print 'Case #{0}: {1}'.format(t, cards.pop())
        else:
            print 'Case #{0}: Bad magician!'.format(t)

if __name__ == '__main__':
    main()

