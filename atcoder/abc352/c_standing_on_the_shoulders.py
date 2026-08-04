"""AtCoder Beginner Contest 352 - C: Standing On The Shoulders
https://atcoder.jp/contests/abc352/tasks/abc352_c

문제
----
N명의 거인이 있고, 거인 i는 어깨 높이 A_i, 머리 높이 B_i를 갖는다
(땅에 혼자 서면 어깨가 A_i, 머리가 B_i). 거인들을 순서 P_1,...,P_N으로
어깨 위에 어깨를 올려 쌓는다: P_1은 땅에 서고, P_{k}의 어깨가 높이
t이면 그 위에 선 P_{k+1}의 어깨는 t + A_{P_{k+1}}, 머리는
t + B_{P_{k+1}}에 위치한다. 순서를 잘 골라서 맨 위(P_N)의 머리 높이를
최대화하라.

접근
----
맨 위 거인 P_N의 머리 높이를 전개하면
  sum_{i=1}^{N-1} A_{P_i} + B_{P_N}
인데, 앞의 합은 "맨 위를 제외한 나머지 N-1명의 A값 합"이라 그 나머지의
순서(누가 몇 번째로 쌓이는지)는 최종 답에 전혀 영향을 주지 않는다
(어차피 다 더해지므로). 즉
  sum_{i=1}^{N-1} A_{P_i} = (전체 A의 합) - A_{P_N}
이므로 답은
  (전체 A의 합) + (B_{P_N} - A_{P_N})
으로 정리되고, 이를 최대화하려면 (B_i - A_i)가 가장 큰 거인을 맨
위에 두면 된다. 결국 최적해는 정렬이나 그리디한 순서 배치 없이,
"전체 A 합 + max(B_i - A_i)" 한 줄로 구해진다.

시간복잡도: O(N)
"""

import sys


def solve(n: int, ab: list[tuple[int, int]]) -> int:
    total_a = sum(a for a, b in ab)
    best_gain = max(b - a for a, b in ab)
    return total_a + best_gain


def main() -> None:
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    ab = []
    for _ in range(n):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        ab.append((a, b))
    print(solve(n, ab))


if __name__ == "__main__":
    main()
