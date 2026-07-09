"""Programmers Lv.2 - 리코쳇 로봇 (Ricochet Robot)
https://school.programmers.co.kr/learn/courses/30/lessons/169199

문제
----
게임판 위 로봇은 한 번의 이동에서 상/하/좌/우 한 방향을 골라, 장애물("D")
이나 게임판 가장자리에 부딪힐 때까지 미끄러진다. 시작 위치("R")에서
목표("G")까지 최소 이동 횟수를 구하라. 도달할 수 없으면 -1을 반환한다.

접근
----
"한 번의 이동 = 한 방향으로 끝까지 미끄러지기"이므로, 한 칸씩 움직이는
일반 BFS가 아니라 "미끄러져 멈추는 위치"를 한 번의 전이로 보는 BFS를
쓴다. 각 상태(위치)에서 4방향으로 미끄러진 도착 위치를 계산해 그래프의
간선으로 삼고, 시작 위치에서 BFS로 최단 거리를 구하면 그게 곧 목표까지의
최소 이동 횟수다. G는 장애물처럼 멈추게 하지 않으므로, 미끄러지다가 우연히
멈춘 칸이 G와 같을 때만 도달한 것으로 센다.

시간복잡도: O(R*C) (칸 수만큼의 상태, 각 상태에서 4방향으로 최대 R+C 칸
이동 — 전체적으로 O((R*C)*(R+C))이며 R, C <= 100 제약에서 충분히 빠르다)
"""

from collections import deque


def solution(board: list[str]) -> int:
    rows = len(board)
    cols = len(board[0])
    grid = [list(row) for row in board]

    start = end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "R":
                start = (r, c)
            elif grid[r][c] == "G":
                end = (r, c)

    def slide(r: int, c: int, dr: int, dc: int) -> tuple[int, int]:
        while True:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "D":
                r, c = nr, nc
            else:
                break
        return r, c

    visited = {start: 0}
    queue = deque([start])
    while queue:
        pos = queue.popleft()
        dist = visited[pos]
        if pos == end:
            return dist
        r, c = pos
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nxt = slide(r, c, dr, dc)
            if nxt not in visited:
                visited[nxt] = dist + 1
                queue.append(nxt)

    return -1
