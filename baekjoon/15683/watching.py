"""Baekjoon 15683 - 감시 (삼성 SW 역량테스트 기출)
https://www.acmicpc.net/problem/15683

문제
----
N*M 사무실 지도(0=빈칸, 6=벽, 1~5=CCTV, 최대 8개)가 주어진다. CCTV 종류별로
가능한 감시 방향 조합(1번:1방향 4가지, 2번:마주보는 2방향 2가지, 3번:꺾인
2방향 4가지, 4번:3방향 4가지, 5번:4방향 1가지)이 있고, 감시는 벽만 막고
다른 CCTV 칸은 통과한다. 모든 CCTV의 방향을 독립적으로 정할 때, 어떤
CCTV도 못 보는 빈 칸(사각지대)의 최소 개수를 구한다.

접근
----
CCTV 개수<=8, 종류별 회전 경우의 수도 최대 4가지라 전체 조합 수가 작다
(itertools.product로 각 CCTV의 방향 선택을 카테시안 곱으로 전부 순회).
조합 하나마다 각 CCTV에서 정해진 방향으로 벽을 만날 때까지 직선으로 뻗어가며
관측된 칸을 집합에 기록하고, 마지막에 원래 빈 칸(0)이면서 관측 안 된 칸의
개수를 세어 최솟값을 갱신한다.
"""

import sys
from itertools import product


def solve(N: int, M: int, grid: list[list[int]]) -> int:
    cctv_list = [(i, j, grid[i][j]) for i in range(N) for j in range(M) if grid[i][j] in (1, 2, 3, 4, 5)]
    if not cctv_list:
        return sum(row.count(0) for row in grid)

    dr = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dc = [0, 0, -1, 1]

    D_list = [
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [[0, 2], [0, 3], [1, 2], [1, 3]],
        [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
        [[0, 1, 2, 3]],
    ]

    def count_blind(assign) -> int:
        watched = set()
        for (i, j, t), dirs in zip(cctv_list, assign):
            for d in dirs:
                ni, nj = i + dr[d], j + dc[d]
                while 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != 6:
                    watched.add((ni, nj))
                    ni += dr[d]
                    nj += dc[d]
        return sum(1 for x in range(N) for y in range(M) if grid[x][y] == 0 and (x, y) not in watched)

    options = [D_list[t - 1] for (i, j, t) in cctv_list]
    best = N * M
    for assign in product(*options):
        best = min(best, count_blind(assign))
    return best


def main() -> None:
    N, M = map(int, sys.stdin.readline().split())
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    print(solve(N, M, grid))


if __name__ == "__main__":
    main()
