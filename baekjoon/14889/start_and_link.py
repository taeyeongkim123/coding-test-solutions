"""Baekjoon 14889 - 스타트와 링크 (삼성 SW 역량테스트 기출)
https://www.acmicpc.net/problem/14889

문제
----
N명(N은 짝수, 4<=N<=20)을 N/2명씩 두 팀(스타트/링크)으로 나눈다.
같은 팀인 두 사람 i, j 사이의 기여도는 S[i][j]+S[j][i] (행렬은 비대칭).
한 팀의 능력치는 팀 내 모든 쌍의 기여도 합. 두 팀 능력치 차이의 최솟값을 구한다.

접근
----
N<=20이라 완전탐색 가능. range(N) 중 N//2명을 고르는 조합을 전부 순회하며
(itertools.combinations(range(N), N//2)) 그 팀과 나머지 팀의 능력치를 각각
itertools.combinations(team, 2)로 팀 내 쌍을 만들어 합산하고, 차이의 최솟값을 갱신한다.
전체 시간복잡도는 C(N, N/2) * O(N) 수준이라 N=20에서도 충분히 빠르다.
"""

import sys
import itertools


def ability(team: tuple[int, ...], s: list[list[int]]) -> int:
    total = 0
    for i, j in itertools.combinations(team, 2):
        total += s[i][j] + s[j][i]
    return total


def solve(n: int, s: list[list[int]]) -> int:
    best = float('inf')
    for q in itertools.combinations(range(n), n // 2):
        other = [x for x in range(n) if x not in q]
        diff = abs(ability(q, s) - ability(other, s))
        if diff < best:
            best = diff
    return best


def main() -> None:
    n = int(sys.stdin.readline())
    s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(solve(n, s))


if __name__ == "__main__":
    main()
