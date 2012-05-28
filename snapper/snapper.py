#!python3

def state(n, k):
    if k % (2 ** n) == 2 ** n - 1:
        return "ON"
    else:
        return "OFF"

T = int(input())
for i in range(1, T + 1):
    line = input()
    N, K = map(int, line.split())
    print("Case #{}: {}".format(i, state(N, K)))

