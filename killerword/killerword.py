#!/usr/bin/env python

def letter_positions(letter, word):
    return [i for i, l in enumerate(word) if letter == l]

def matches(word, positions, letter):
    return all(word[i] == letter for i in positions)

def choose(words, letters):
    max_points_lost = 0
    max_word = words[0]
    for word in words:
        points_lost = 0
        remaining = [w for w in words if len(w) == len(word)]
        for c in letters:
            if all(c not in w for w in remaining):
                continue
            positions = letter_positions(c, word)
            if not positions:
                points_lost += 1
            remaining = [w for w in remaining if matches(w, positions, c)]
            if len(remaining) == 1:
                break
        assert remaining[0] == word
        if points_lost > max_points_lost:
            max_points_lost = points_lost
            max_word = word
    return max_word


def solve(words, lists):
    ws = []
    for l in lists:
        ws.append(choose(words, l))
    return ws

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        N, M = map(int, raw_input().split())
        words = []
        for n in range(N):
            words.append(raw_input())
        lists = []
        for m in range(M):
            lists.append(raw_input())

        ws = solve(words, lists)
        print 'Case #{0}: {1}'.format(t, ' '.join(ws))



if __name__ == '__main__':
    main()
