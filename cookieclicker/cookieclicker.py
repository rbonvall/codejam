#!/usr/bin/env python

# TODO: find closed form
def solve(farm_cost, farm_rate, goal):
    t = 0.0  # current time
    p = 2.0  # production rate

    total_time_to_goal = t + goal / p
    while True:
        # buy
        t += farm_cost / p
        p += farm_rate
        total_time_to_goal_with_farm = t + goal / p

        if total_time_to_goal <= total_time_to_goal_with_farm:
            # buying didn't help
            break

        total_time_to_goal = total_time_to_goal_with_farm

    return total_time_to_goal

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        C, F, X = map(float, raw_input().split())
        print 'Case #{}: {:.7f}'.format(t, solve(C, F, X))

if __name__ == '__main__':
    main()

