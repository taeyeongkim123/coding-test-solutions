"""AtCoder Beginner Contest 450 - C: Puddles
https://atcoder.jp/contests/abc450/tasks/abc450_c

문제
----
H*W 격자가 있고 각 칸은 흰색('.') 또는 검은색('#')이다. 흰색 칸들이
상하좌우로 연결된 덩어리 중, 격자의 가장자리(1행, H행, 1열, W열)에
닿지 않는 덩어리를 "웅덩이"라 한다. 웅덩이의 개수를 구하라.

접근
----
아직 방문하지 않은 흰색 칸을 시작점으로 BFS를 돌며 하나의 덩어리를
전부 탐색한다. 탐색 도중 가장자리 칸을 하나라도 방문하면 그 덩어리는
고립되지 않은 것이므로 제외하고, 그렇지 않은 덩어리만 개수를 센다.

시간복잡도: O(H*W)
"""

import sys
from collections import deque


def solve(h: int, w: int, grid: list[str]) -> int:
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited_list = set()
    ans = 0

    for i in range(h):
        for k in range(w):
            if (i, k) in visited_list or grid[i][k] == "#":
                continue

            queue = deque()
            queue.append([i, k])
            visited_list.add((i, k))

            is_isolated = True

            while queue:
                I, K = queue.popleft()

                if I == 0 or I == h - 1 or K == 0 or K == w - 1:
                    is_isolated = False

                for z in range(4):
                    n_x = I + dx[z]
                    n_y = K + dy[z]

                    if 0 <= n_x < h and 0 <= n_y < w:
                        if (n_x, n_y) not in visited_list and grid[n_x][n_y] == ".":
                            visited_list.add((n_x, n_y))
                            queue.append([n_x, n_y])

            if is_isolated:
                ans += 1

    return ans


def main() -> None:
    data = sys.stdin.buffer.read().split()
    h = int(data[0])
    w = int(data[1])
    grid = [data[2 + i].decode() for i in range(h)]

    print(solve(h, w, grid))


if __name__ == "__main__":
    main()
