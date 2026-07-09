"""AtCoder Beginner Contest 463 - D: Maximize the Gap
https://atcoder.jp/contests/abc463/tasks/abc463_d

문제
----
수직선 위에 N개의 구간(천) [L_i, R_i]가 있다. 이 중 서로 겹치지 않는 K개를
골라서, 고른 것들 사이 모든 쌍의 거리 중 최솟값(점수)을 최대화하라. 그런
K개를 고를 수 없으면 -1을 출력한다. 두 구간이 겹치지 않을 때 그 거리는
(오른쪽 구간의 왼쪽 끝) - (왼쪽 구간의 오른쪽 끝)이다.

접근
----
답을 이분 탐색한다. 후보 값 g("모든 인접 쌍의 간격이 g 이상")가 실현
가능한지는, 구간들을 오른쪽 끝(R) 오름차순으로 정렬한 뒤 탐욕적으로
고르면 확인할 수 있다: 마지막으로 고른 구간의 오른쪽 끝을 last_r이라 할
때, 다음 구간의 L이 last_r + g 이상이면 그 구간을 고른다(고전적인 구간
스케줄링 탐욕과 동일한 원리로, 이 방식이 K개를 고를 수 있는지 여부를
최적으로 판정한다). 고른 개수가 K 이상이면 g는 실현 가능하다.

g=1(가장 느슨한, 즉 서로 겹치지만 않으면 되는 경우)조차 K개를 고를 수
없으면 -1을 출력한다. 그렇지 않으면 실현 가능한 최대 g를 이분 탐색으로
찾는다.

시간복잡도: O(N log N log(max coordinate))
"""

import sys


def _feasible(intervals: list[tuple[int, int]], k: int, gap: int) -> bool:
    count = 0
    last_r = -(10**18)
    for left, r in intervals:
        if left - last_r >= gap:
            count += 1
            last_r = r
            if count >= k:
                return True
    return count >= k


def solve(n: int, k: int, intervals: list[tuple[int, int]]) -> int:
    intervals = sorted(intervals, key=lambda lr: lr[1])

    if not _feasible(intervals, k, 1):
        return -1

    lo, hi = 1, 2 * 10**9
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if _feasible(intervals, k, mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


def main() -> None:
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    k = int(data[idx + 1])
    idx += 2
    intervals = []
    for _ in range(n):
        left = int(data[idx])
        r = int(data[idx + 1])
        idx += 2
        intervals.append((left, r))

    print(solve(n, k, intervals))


if __name__ == "__main__":
    main()
