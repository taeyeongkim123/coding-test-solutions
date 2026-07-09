"""AtCoder Beginner Contest 464 - C: Plumage Palette
https://atcoder.jp/contests/abc464/tasks/abc464_c

문제
----
N마리의 새를 M일 동안 관찰한다. 새 i는 D_i일이 되기 전까지 색 A_i이고,
D_i일부터는 색 B_i이다(D_i=1이면 1일차부터 이미 B_i). 각 날짜 1..M에
대해, 그 날 관찰되는 서로 다른 색의 개수를 구하라.

접근
----
새 N마리, 날짜 M일 모두 최대 3*10^5라 O(N*M) 완전탐색은 시간 초과다.
대신 "색깔 등장 횟수" 배열과 "현재 등장 중인 서로 다른 색의 개수"를
유지하면서, 색이 바뀌는 시점(D_i)에만 갱신하는 이벤트 방식으로 O(N+M)에
푼다.

1) 1일차 초기 상태를 만든다: D_i > 1인 새는 A_i, D_i == 1인 새는 이미
   B_i로 카운트한다.
2) D_i > 1인 새는 "D_i일에 A_i를 빼고 B_i를 더한다"는 이벤트로 등록한다.
3) 날짜를 1부터 M까지 순회하며, 그 날짜에 등록된 이벤트를 먼저 적용한
   뒤(색이 바뀐 뒤) 현재의 distinct 색 개수를 답으로 기록한다.

시간복잡도: O(N + M)
"""

import sys


def solve(n: int, m: int, birds: list[tuple[int, int, int]]) -> list[int]:
    events: list[list[tuple[int, int]]] = [[] for _ in range(m + 1)]
    count_color = [0] * (n + 1)
    distinct = 0

    for a, d, b in birds:
        if d == 1:
            if count_color[b] == 0:
                distinct += 1
            count_color[b] += 1
        else:
            if count_color[a] == 0:
                distinct += 1
            count_color[a] += 1
            events[d].append((a, b))

    answers = []
    for day in range(1, m + 1):
        for a, b in events[day]:
            count_color[a] -= 1
            if count_color[a] == 0:
                distinct -= 1
            if count_color[b] == 0:
                distinct += 1
            count_color[b] += 1
        answers.append(distinct)

    return answers


def main() -> None:
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    birds = []
    for _ in range(n):
        a = int(data[idx])
        d = int(data[idx + 1])
        b = int(data[idx + 2])
        idx += 3
        birds.append((a, d, b))

    answers = solve(n, m, birds)
    sys.stdout.write("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    main()
