"""Programmers Lv.2 - 지게차와 크레인 (Forklift and Crane)
https://school.programmers.co.kr/learn/courses/30/lessons/468379

문제
----
n x m 격자에 컨테이너가 배치되어 있다. 요청이 한 글자(예: "A")이면 지게차
요청으로, "현재 창고 외부와 연결된"(4면 중 최소 1면이 외부와 연결) 해당
종류 컨테이너를 모두 꺼낸다. 요청이 두 글자(예: "BB")이면 크레인 요청으로,
위치와 상관없이 해당 종류 컨테이너를 전부 꺼낸다. 모든 요청을 순서대로
처리한 뒤 남은 컨테이너 수를 구하라.

접근
----
핵심은 "외부와 연결"의 정확한 의미다. 단순히 "제거된 칸에 인접하면 노출"로
보면 안 된다 — 제거된 칸이라도 사방이 남은 컨테이너로 완전히 막혀 있으면
그 빈 칸은 진짜 바깥과 연결되지 않은 "고립된 구멍"이다. 따라서 매 지게차
요청마다, 격자 테두리(진짜 바깥)에서 시작해 빈 칸을 통해서만 이동하는
BFS를 돌려 "바깥과 실제로 연결된 빈 칸 영역"을 구하고, 그 영역에 인접한
컨테이너만 노출된 것으로 간주해 제거한다(같은 요청 안에서 연쇄적으로 더
파고들지 않고, 요청 시작 시점의 상태 기준으로 한 번에 판정).

크레인 요청은 위치 판정 없이 해당 종류를 전부 제거하면 된다.

시간복잡도: O(요청 수 x 격자 크기) — 격자가 최대 50x50, 요청이 최대 100개라
매 요청마다 새로 BFS를 돌려도 충분히 빠르다.
"""

from collections import deque


def solution(storage: list[str], requests: list[str]) -> int:
    rows = len(storage)
    cols = len(storage[0])
    grid = [list(row) for row in storage]
    remaining = rows * cols

    def exposed_cells() -> set[tuple[int, int]]:
        visited = [[False] * cols for _ in range(rows)]
        exposed: set[tuple[int, int]] = set()
        queue: deque[tuple[int, int]] = deque()

        for r in range(rows):
            for c in range(cols):
                if r in (0, rows - 1) or c in (0, cols - 1):
                    if grid[r][c] is None:
                        if not visited[r][c]:
                            visited[r][c] = True
                            queue.append((r, c))
                    else:
                        exposed.add((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] is None:
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                    else:
                        exposed.add((nr, nc))
        return exposed

    for request in requests:
        if len(request) == 1:
            container_type = request
            to_remove = [
                (r, c) for r, c in exposed_cells() if grid[r][c] == container_type
            ]
            for r, c in to_remove:
                grid[r][c] = None
                remaining -= 1
        else:
            container_type = request[0]
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == container_type:
                        grid[r][c] = None
                        remaining -= 1

    return remaining
