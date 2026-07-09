"""Programmers - 선인장 숨기기 (Cactus Hiding)
2025 카카오 하반기 2차 코딩테스트
https://school.programmers.co.kr/learn/courses/30/lessons/388353

문제
----
m행 n열 사막에 w x h 크기의 선인장 구역을 하나 배치한다. 빗방울이 drops
순서대로 한 칸씩 떨어지는데, 선인장 구역 안의 칸에 빗방울이 떨어지면 그
구역은 그 시점에 비를 맞는다. 다음 우선순위로 최적의 구역 좌상단 좌표
[r, c]를 구하라: (1) 끝까지 비를 맞지 않는 위치, (2) 그중에서 안 되면
가장 늦게 비를 맞는 위치, (3) 그래도 같으면 가장 위쪽 행, (4) 그래도
같으면 가장 왼쪽 열.

접근
----
칸 (r, c)마다 "그 칸이 처음 비를 맞는 시점"(drops에서 처음 등장하는
1-indexed 순번, 없으면 무한대)을 first_hit[r][c]로 미리 계산해두면, 구역
[r..r+h-1, c..c+w-1]가 비를 맞는 시점은 그 구역 안 first_hit의 최솟값이다.
모든 (r, c) 후보 위치에 대해 이 최솟값을 구해서 그중 최댓값(가장 늦게 맞는
구역)을 찾으면 된다.

전 좌표를 매번 스캔하면 O(칸 수 x 구역 크기)라 너무 느릴 수 있으므로, 2D
슬라이딩 윈도우 최솟값을 단조 deque로 구현해 O(m*n)에 처리한다: 먼저 각
행에서 폭 w짜리 윈도우 최솟값(row_min)을 구하고, 그 결과에 대해 각 열에서
높이 h짜리 윈도우 최솟값을 구하면 그게 바로 모든 (r, c) 구역의 최솟값이다.

시간복잡도: O(m*n) (m*n <= 500,000 제약과 맞물려 충분히 빠르다)
"""

from collections import deque


def solution(m: int, n: int, h: int, w: int, drops: list[list[int]]) -> list[int]:
    INF = float("inf")
    first_hit = [[INF] * n for _ in range(m)]
    for idx, (r, c) in enumerate(drops):
        if first_hit[r][c] == INF:
            first_hit[r][c] = idx + 1

    cols_count = n - w + 1
    row_min = [[INF] * cols_count for _ in range(m)]
    for r in range(m):
        dq: deque[int] = deque()
        row = first_hit[r]
        for c in range(n):
            while dq and row[dq[-1]] >= row[c]:
                dq.pop()
            dq.append(c)
            while dq[0] <= c - w:
                dq.popleft()
            if c >= w - 1:
                row_min[r][c - w + 1] = row[dq[0]]

    rows_count = m - h + 1
    final_min = [[INF] * cols_count for _ in range(rows_count)]
    for c in range(cols_count):
        dq = deque()
        col = [row_min[r][c] for r in range(m)]
        for r in range(m):
            while dq and col[dq[-1]] >= col[r]:
                dq.pop()
            dq.append(r)
            while dq[0] <= r - h:
                dq.popleft()
            if r >= h - 1:
                final_min[r - h + 1][c] = col[dq[0]]

    best_val = -1.0
    best_r = best_c = 0
    for r in range(rows_count):
        for c in range(cols_count):
            val = final_min[r][c]
            if val > best_val:
                best_val = val
                best_r, best_c = r, c

    return [best_r, best_c]
