#!python3

def basins(elevations):


T = int(input())
for i in range(1, T + 1):
    H, W = map(int, input().split())
    elevations = [list(map(int, input().split())) for _ in range(H)]
    print("Case #{}:".format(i))
    print(basins(elevations))

