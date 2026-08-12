"""AtCoder Beginner Contest 350 - C: Sort (복습용 재풀이)
https://atcoder.jp/contests/abc350/tasks/abc350_c

문제
----
(1,2,...,N)의 순열 A가 주어진다. "1≤i<j≤N인 (i,j)를 골라 A_i와 A_j를
스왑"하는 작업을 0회 이상 N-1회 이하로 수행해 A를 (1,2,...,N)으로
만드는 스왑 시퀀스를 하나 출력하라.

접근
----
순열을 "각 위치가 자기가 있어야 할 값을 가리키는 방향 그래프"로 보면
몇 개의 사이클로 분해된다. 앞에서부터(k=0..N-1) 훑으면서, A[k]가
제자리(k+1)가 아니면 "A[k]가 있어야 할 자리(j = A[k]-1)"와 스왑하고
(k+1, j+1)을 기록하는 과정을 A[k]가 제자리에 올 때까지 반복한다.
매 스왑마다 적어도 하나의 원소가 확정적으로 제자리에 놓이므로, 전체
스왑 횟수는 N - (사이클 개수)로 항상 N-1 이하다.

시간복잡도: O(N)
"""

import sys


def solve(n: int, a: list[int]) -> list[tuple[int, int]]:
    a = a[:]
    swaps = []
    for k in range(n):
        while a[k] != k + 1:
            j = a[k] - 1
            a[k], a[j] = a[j], a[k]
            swaps.append((k + 1, j + 1))
    return swaps


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))

    swaps = solve(n, a)
    out = [str(len(swaps))]
    for i, j in swaps:
        out.append(f"{i} {j}")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
