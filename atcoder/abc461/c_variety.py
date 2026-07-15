"""AtCoder Beginner Contest 461 - C: Variety
https://atcoder.jp/contests/abc461/tasks/abc461_c

문제
----
N개의 보석이 있고, 보석 i는 색 C_i와 가치 V_i를 가진다. 이 중 정확히 K개를
선택하되, 선택한 보석의 색이 M종류 이상이어야 한다. 선택한 보석의 가치
합의 최댓값을 구하라.

접근
----
먼저 색 구분을 무시하고 가치 상위 K개를 그대로 뽑는다고 하자. 이 K개에
포함된 색의 종류 수 D가 이미 M 이상이면 그 합이 곧 답이다.

D < M이라면, 이미 뽑힌 보석 중 하나를 빼고 아직 뽑히지 않은 색의 보석을
새로 넣는 "교환"을 (M - D)번 반복해 색 종류를 하나씩 늘려야 한다. 각
교환에서 손해를 최소화하려면,
  - 추가할 보석은 "아직 선택되지 않은 색들" 중 최고 가치 보석(각 색의
    1등)이어야 유리하고,
  - 제거할 보석은 "현재 선택에서 같은 색이 2개 이상 뽑혀 있어 하나를
    빼도 그 색이 선택에서 완전히 사라지지 않는" 보석들 중 최소 가치
    보석이어야 유리하다(그래야 종류 수가 줄지 않는다).
매 단계 이 두 후보(추가 후보 최대 힙, 제거 후보 최소 힙)를 갱신하며
(M-D)번 교환하면 된다. K > D인 한(즉 M <= K이므로 아직 목표를 못 채운
동안) 어떤 색은 반드시 2개 이상 뽑혀 있으므로 제거 후보는 항상 존재한다.
이 그리디는 교환 논증(exchange argument)으로 최적성이 보장된다.

각 색의 보석을 가치 내림차순으로 정렬해두면, 상위 K개 선택에서 한 색이
차지하는 항목은 항상 그 색의 "앞쪽 구간(prefix)"이 되므로, 제거 시
꺼낼 다음 후보(그 색에서 남은 것 중 최소값)를 O(log N)에 유지할 수 있다.

시간복잡도: O(N log N)
"""

import sys
from collections import defaultdict
from heapq import heappush, heappop


def solve(k: int, m: int, gems: list[tuple[int, int]]) -> int:
    color_values: dict[int, list[int]] = defaultdict(list)
    for c, v in gems:
        color_values[c].append(v)
    for c in color_values:
        color_values[c].sort(reverse=True)

    top_k = sorted(gems, key=lambda g: -g[1])[:k]
    freq: dict[int, int] = defaultdict(int)
    total = 0
    for c, v in top_k:
        freq[c] += 1
        total += v

    need = m - len(freq)
    if need <= 0:
        return total

    addable: list[tuple[int, int]] = []
    for c, values in color_values.items():
        if freq.get(c, 0) == 0:
            heappush(addable, (-values[0], c))

    removable: list[tuple[int, int]] = []
    for c, count in freq.items():
        if count >= 2:
            heappush(removable, (color_values[c][count - 1], c))

    for _ in range(need):
        neg_add_value, add_color = heappop(addable)
        remove_value, remove_color = heappop(removable)
        total += -neg_add_value - remove_value

        freq[add_color] = 1
        remaining = freq[remove_color] - 1
        freq[remove_color] = remaining
        if remaining >= 2:
            heappush(removable, (color_values[remove_color][remaining - 1], remove_color))

    return total


def main() -> None:
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    k = int(data[idx + 1])
    m = int(data[idx + 2])
    idx += 3
    gems = []
    for _ in range(n):
        c = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        gems.append((c, v))

    print(solve(k, m, gems))


if __name__ == "__main__":
    main()
