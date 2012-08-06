#!/usr/bin/python

def advance(s):
    return next(s, (None, None))
def sign(x):
    return -1 if x < 0 else 1

def solve(seq):
    t = 0
    b, o = 1, 1
    b_buttons = ((n, button) for (n, (color, button)) in enumerate(seq) if color == 'B')
    o_buttons = ((n, button) for (n, (color, button)) in enumerate(seq) if color == 'O')
    n_b, next_b = advance(b_buttons)
    n_o, next_o = advance(o_buttons)

    while next_b or next_o:
        t += 1
        #print 't =', t

        b_pushes, o_pushes = False, False

        if not next_o:
            pass
            #print 'o finished'
        elif next_o != o:
            o += sign(next_o - o)
            #print 'o moves to', o
        elif (next_b and n_o < n_b) or not next_b:
            o_pushes = True
            #print 'o pushes'
        else:
            pass
            #print 'o waits'


        if not next_b:
            pass
            #print 'b finished'
        elif next_b != b:
            b += sign(next_b - b)
            #print 'b moves to', b
        elif (next_o and n_b < n_o) or not next_o:
            b_pushes = True
            #print 'b pushes'
        else:
            pass
            #print 'b waits'

        if b_pushes:
            n_b, next_b = advance(b_buttons)
        elif o_pushes:
            n_o, next_o = advance(o_buttons)

    return t

T = int(raw_input())
for t in range(1, T + 1):
    values = raw_input().split()
    seq = zip(values[1::2], map(int, values[2::2]))
    print 'Case #{0}: {1}'.format(t, solve(seq))
    #print seq


