#!python3

import re

def count_words(pattern, words):
    '''Count how many words math the pattern'''

    pattern = pattern.replace('(', '[').replace(')', ']')
    p = re.compile(pattern)
    return sum(1 for word in words if p.match(word))






L, D, N = map(int, input().split())
words = [input().strip() for _ in range(D)]
for i in range(1, N + 1):
    pattern = input()
    print("Case #{}: {}".format(i, count_words(pattern, words)))

