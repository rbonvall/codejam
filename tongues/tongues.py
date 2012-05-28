#!/usr/bin/python3

from_ = 'abcdefghijklmnopqrstuvwxyz '
to    = 'yhesocvxduiglbkrztnwjpfmaq '
from_ += from_.upper()
to    += to.upper()
mapping = dict(zip(from_, to))

T = int(input())
for t in range(T):
    g = input()
    s = ''.join(mapping[c] for c in g)
    print('Case #{}: {}'.format(t + 1, s))
