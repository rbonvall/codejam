#!/usr/bin/env python

from collections import defaultdict

def has_opposed(opposed, elist, element):
    return bool(set(elist) & opposed[element])

def invoke(combining, opposed, string):
    element_list = []

    #print '===', string
    for element in string:
        #print ''.join(element_list)

        last_two = (element_list[-1] if element_list else '') + element
        if last_two in combining:
            element_list.pop()
            element_list.append(combining[last_two])
        elif has_opposed(opposed, element_list, element):
            del element_list[:]
        else:
            element_list.append(element)

    #print ''.join(element_list)
    return element_list

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        values = raw_input().split()
        C = int(values[0])
        D = int(values[1 + C])
        N = int(values[-2])

        combining = dict()
        for a, b, c in values[1:C + 1]:
            combining[a + b] = c
            combining[b + a] = c

        opposed = defaultdict(set)
        for a, b in values[C + 2: C + 2 + D]:
            opposed[a].add(b)
            opposed[b].add(a)

        string = values[-1]

        elist = invoke(combining, opposed, string)
        print 'Case #{0}: {1}'.format(t, repr(elist).replace("'", ""))

if __name__ == '__main__':
    main()



