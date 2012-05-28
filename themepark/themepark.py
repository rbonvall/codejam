#!python3

from collections import deque
from itertools import count

def queue_front(k, g):
    '''Compute, for each group when it is at the front of the queue, how many
    groups will board the roller coaster and how many euros will be made.'''
    to_board, profit = [], []
    N = len(g)
    for i, g_i in enumerate(g):
        available_seats = k - g_i
        nr_remaining_groups = N - 1
        for j in count(1):
            next_group_size = g[(i + j) % N]
            if available_seats - next_group_size < 0 or not nr_remaining_groups:
                to_board.append(j)
                profit.append(k - available_seats)
                break
            available_seats -= next_group_size
            nr_remaining_groups -= 1
    return to_board, profit

def find_loop(g, to_board):
    '''Find a loop in queue configurations.
    Returns the pre-loop sequence and the loop.'''
    already_at_front = set()
    front_history = []
    N = len(g)
    front = 0
    while front not in already_at_front:
        already_at_front.add(front)
        front_history.append(front)
        front = (front + to_board[front]) % N
    i = front_history.index(front)
    pre_loop = front_history[:i]
    loop = front_history[i:]
    return pre_loop, loop

def euros(R, k, g):
    to_board, profit = queue_front(k, g)
    pre_loop, loop = find_loop(g, to_board)
    #print('TO BOARD', to_board)
    #print('PROFIT', profit)
    #print('LOOP:', pre_loop, loop)
    #print('PROFIT WITH PRE LOOP', [profit[i] for i in pre_loop])
    #print('PROFIT WITH LOOP', [profit[i] for i in loop])

    # sum euros of pre_loop
    pre_loop_euros = sum(profit[i] for i in pre_loop[:R])
    R = max(0, R - len(pre_loop))

    nr_loops, R = divmod(R, len(loop))
    #print('divmod(R, len(loop)):', nr_loops, R)
    loop_euros = nr_loops * sum(profit[i] for i in loop)
    remaining_euros = sum(profit[i] for i in loop[:R])

    #print(pre_loop, nr_loops, loop, loop[:R])

    return pre_loop_euros + loop_euros + remaining_euros


T = int(input())
for test_case in range(1, T + 1):
    R, k, N = map(int, input().split())
    g = list(map(int, input().split()))
    print("Case #{}: {}".format(test_case, euros(R, k, g)))

