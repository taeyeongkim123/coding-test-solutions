"""Baekjoon 14502 - 연구소 (삼성 SW 역량테스트 기출)
https://www.acmicpc.net/problem/14502

문제
----
N*M 지도(0=빈칸, 1=벽, 2=바이러스)에서 빈 칸 중 정확히 3곳을 새 벽으로 세운 뒤,
바이러스를 상하좌우로 인접한 빈 칸에 계속 퍼뜨린다. 확산이 끝난 뒤 남은 빈 칸
(안전 영역)의 개수를 최대화하라.

접근
----
N,M<=8이라 벽 3개를 세우는 모든 조합(C(N*M,3), 최대 약 4만)을 완전탐색한다.
조합마다 원본 지도를 복사해 벽을 세우고(이미 벽/바이러스인 칸이 섞이면 무효
조합이므로 스킵), 바이러스 좌표들을 시작점으로 BFS를 돌려 확산시킨 뒤 남은
빈 칸 개수를 세어 최댓값을 갱신한다.
"""

import sys
from itertools import combinations
from collections import deque
import copy


def get_c(Q: int, N: int) -> tuple[int, int]:
    x = Q % N
    y = Q // N
    return x, y


def solve(N: int, M: int, grid: list[list[int]]) -> int:
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    virus_list = [(i, j) for i in range(N) for j in range(M) if grid[i][j] == 2]

    ans = 0
    for Q in combinations(range(N * M), 3):
        contin = True
        n_grid = copy.deepcopy(grid)
        for R in Q:
            x, y = get_c(R, N)
            if n_grid[x][y] == 0:
                n_grid[x][y] = 1
            else:
                contin = False
                break
        if not contin:
            continue

        queue = deque(virus_list)
        visited_list = set(virus_list)

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if (0 <= nx < N) and (0 <= ny < M) and (nx, ny) not in visited_list and n_grid[nx][ny] == 0:
                    visited_list.add((nx, ny))
                    n_grid[nx][ny] = 2
                    queue.append((nx, ny))

        safe = sum(row.count(0) for row in n_grid)
        ans = max(ans, safe)

    return ans


def main() -> None:
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solve(N, M, grid))


if __name__ == "__main__":
    main()
