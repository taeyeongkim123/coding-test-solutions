"""Baekjoon 2110 - 공유기 설치
https://www.acmicpc.net/problem/2110

문제
----
수직선 위에 N개의 집이 있다. 이 중 C개의 집에 공유기를 설치해서, 공유기
사이의 최소 거리가 최대한 커지도록 하려고 한다. 그 최대 최소 거리를
구하라.

접근
----
답(공유기 사이 최소 거리) D를 이분 탐색한다. 후보 D가 실현 가능한지는,
집 좌표를 오름차순 정렬한 뒤 맨 왼쪽 집부터 탐욕적으로 설치해보면 확인할
수 있다: 마지막으로 설치한 집에서 D 이상 떨어진 다음 집이 나올 때마다
설치한다. 이렇게 설치한 개수가 C 이상이면 D는 실현 가능하다(간격을
넓게 잡을수록 설치 가능 개수가 줄어드는 단조성이 있으므로 이분 탐색이
성립한다).

시간복잡도: O(N log N) (정렬) + O(N log(max coordinate)) (이분 탐색) = O(N log N)
"""

import sys


def _can_install(houses: list[int], c: int, distance: int) -> bool:
    count = 1
    last = houses[0]

    for x in houses[1:]:
        if x - last >= distance:
            count += 1
            last = x

            if count >= c:
                return True

    return False


def solve(n: int, c: int, houses: list[int]) -> int:
    houses = sorted(houses)

    lo, hi = 1, houses[-1] - houses[0]
    result = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        if _can_install(houses, c, mid):
            result = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return result


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, c = int(data[0]), int(data[1])
    houses = [int(x) for x in data[2 : 2 + n]]

    print(solve(n, c, houses))


if __name__ == "__main__":
    main()
