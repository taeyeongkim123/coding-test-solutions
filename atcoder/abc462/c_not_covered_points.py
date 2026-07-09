"""AtCoder Beginner Contest 462 - C: Not Covered Points
https://atcoder.jp/contests/abc462/tasks/abc462_c

문제
----
평면 위에 N개의 점이 있고, 각 점 i의 좌표는 (X_i, Y_i)이다. X 좌표들과
Y 좌표들은 각각 (1..N)의 순열이다. 점 i에 대해, 원점 (0,0)과 (X_i, Y_i)를
대각선으로 하는 직사각형의 "내부"(경계 제외)에 다른 점이 하나도 들어있지
않으면 그 i를 센다. 그런 i의 개수를 구하라.

접근
----
점 i가 조건을 만족하지 못하는 경우는, X_j < X_i 이면서 Y_j < Y_i 인 점 j가
존재하는 경우뿐이다(그런 점이 직사각형 내부에 들어오므로). X가 순열이라
모든 X 값이 서로 다르므로, 점들을 X 오름차순으로 정렬해 왼쪽에서 오른쪽으로
훑으면서 지금까지 본 Y의 최솟값(prefix minimum)을 유지한다. 현재 점의 Y가
그 최솟값보다 작다면, 왼쪽(X가 더 작은) 어떤 점도 Y가 더 작지 않다는
뜻이므로 조건을 만족한다.

시간복잡도: O(N log N) (정렬 비용)
"""

import sys


def solve(points: list[tuple[int, int]]) -> int:
    points = sorted(points)
    prefix_min = float("inf")
    count = 0
    for _, y in points:
        if y < prefix_min:
            count += 1
            prefix_min = y
    return count


def main() -> None:
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    points = []
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        idx += 2
        points.append((x, y))
    print(solve(points))


if __name__ == "__main__":
    main()
