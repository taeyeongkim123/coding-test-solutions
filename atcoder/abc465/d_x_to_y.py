"""AtCoder Beginner Contest 465 - D: X to Y
https://atcoder.jp/contests/abc465/tasks/abc465_d

문제
----
x=X에서 시작해, 다음 연산을 반복할 수 있다: 정수 y를 골라 floor(x/K)=y
(내려가기, y는 유일) 이거나 floor(y/K)=x (올라가기, y는 x*K ~ x*K+K-1 중 하나)를
만족하면 x를 y로 바꾼다. x=Y로 만드는 최소 연산 횟수를 구한다 (T개 쿼리).

접근
----
"내려가기 = 부모로 이동, 올라가기 = 자식(K개) 중 하나로 이동"인 0을 루트로 하는
K진 트리로 보면, X에서 Y까지 최소 연산 = 트리에서의 최단 거리
= depth(X) + depth(Y) - 2*depth(LCA(X,Y)).
depth(v)는 v를 K로 나눠 0이 될 때까지 걸리는 횟수 (O(log_K v), 최대 약 60).
더 깊은 쪽을 얕은 쪽 depth까지 끌어올린 뒤, 두 값이 같아질 때까지 동시에 K로
나누면서 소모한 총 연산 횟수를 세면 그게 곧 트리 거리(정답)다.
쿼리당 O(log_K X)이고 T<=2*10^5라 충분히 빠르다.
"""

import sys


def get_A(X: int, Y: int, K: int) -> int:
    ops = 0

    def depth(v: int) -> int:
        d = 0
        while v > 0:
            v //= K
            d += 1
        return d

    dx, dy = depth(X), depth(Y)

    while dx > dy:
        X //= K
        dx -= 1
        ops += 1
    while dx < dy:
        Y //= K
        dy -= 1
        ops += 1
    while X != Y:
        X //= K
        Y //= K
        ops += 2

    return ops


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        x, y, k = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        out.append(str(get_A(x, y, k)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
