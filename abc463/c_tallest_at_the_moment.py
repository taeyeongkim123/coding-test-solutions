"""AtCoder Beginner Contest 463 - C: Tallest at the Moment
https://atcoder.jp/contests/abc463/tasks/abc463_c

문제
----
회의실에 N명이 있고, 사람 i는 키 H_i, 퇴장 시각 L_i를 가진다(L은 오름차순
정렬되어 입력된다). Q개의 질의마다 시각 T_i + 0.5분에 남아있는 사람들 중
최대 키를 구하라. 시각 T+0.5에 사람 i가 남아있다는 것은 L_i > T 라는 뜻이다.

접근
----
L이 이미 오름차순으로 주어지므로, 뒤에서부터 접미사 최댓값 배열
suf_max[k] = max(H_k, H_{k+1}, ..., H_{N-1}) 을 미리 만들어 둔다. 질의 T가
오면, L_i > T 를 만족하는 가장 앞쪽 인덱스를 이분 탐색(bisect_right)으로
찾아 그 위치의 접미사 최댓값을 답으로 낸다.

시간복잡도: O((N + Q) log N)
"""

import bisect
import sys


def solve(heights: list[int], leave_times: list[int], queries: list[int]) -> list[int]:
    n = len(heights)
    suf_max = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf_max[i] = max(heights[i], suf_max[i + 1])

    answers = []
    for t in queries:
        pos = bisect.bisect_right(leave_times, t)
        answers.append(suf_max[pos])
    return answers


def main() -> None:
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    heights = []
    leave_times = []
    for _ in range(n):
        heights.append(int(data[idx]))
        leave_times.append(int(data[idx + 1]))
        idx += 2

    q = int(data[idx])
    idx += 1
    queries = [int(data[idx + i]) for i in range(q)]

    answers = solve(heights, leave_times, queries)
    sys.stdout.write("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    main()
