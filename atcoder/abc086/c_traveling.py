"""AtCoder Beginner Contest 086 - C: Traveling
https://atcoder.jp/contests/abc086/tasks/arc089_a

문제
----
AtCoDeer는 시각 0에 점 (0,0)에서 출발해, 각 시각 t_i에 점 (x_i,y_i)를
차례로 방문해야 한다(t_i는 오름차순). 매 시각 t에서 t+1로 넘어갈 때
상하좌우 인접한 4칸 중 한 곳으로 반드시 이동해야 한다(제자리 정지 불가).
이 일정이 실행 가능한지 판정하라.

접근
----
이전 방문 지점에서 다음 방문 지점까지, 걸리는 시간 dt와 맨해튼 거리
dist를 각각 구한다. dt < dist 이면 시간 내에 도착이 불가능하고, 매 이동이
반드시 위치를 바꾸므로 남는 시간(dt - dist)은 한 칸 갔다가 되돌아오는
식으로만 소모할 수 있어 항상 짝수여야 한다. 두 조건 중 하나라도 어기는
구간이 있으면 전체 일정이 불가능하다.

시간복잡도: O(N)
"""

import sys


def solve(points: list[tuple[int, int, int]]) -> str:
    c_t, c_x, c_y = 0, 0, 0

    for n_t, n_x, n_y in points:
        dt = n_t - c_t
        dist = abs(n_x - c_x) + abs(n_y - c_y)

        if dt < dist or (dt - dist) % 2 != 0:
            return "No"

        c_t, c_x, c_y = n_t, n_x, n_y

    return "Yes"


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    points = []
    idx = 1
    for _ in range(n):
        t, x, y = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        points.append((t, x, y))
        idx += 3

    print(solve(points))


if __name__ == "__main__":
    main()
