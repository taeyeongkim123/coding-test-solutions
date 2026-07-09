"""Programmers Lv.2 - 광물 캐기 (Mineral Mining)
https://school.programmers.co.kr/learn/courses/30/lessons/172927

문제
----
다이아몬드/철/돌 곡괭이를 각각 picks[0], picks[1], picks[2]개 가지고
있다. 한 번 사용을 시작한 곡괭이는 광물 5개를 캐거나(또는 광물이
떨어질 때까지) 계속 사용해야 하며, 광물은 주어진 순서대로만 캘 수 있다.
곡괭이·광물 종류별 피로도가 표로 주어질 때, 모든 광물을 캐거나 곡괭이가
바닥날 때까지 최소 피로도로 채굴한 총 피로도를 구하라.

접근
----
광물을 순서대로 5개씩 묶어 "구간(chunk)"으로 나누면, 매 구간마다 곡괭이
하나를 선택해 그 구간 전체를 캐는 것과 같다. 사용 가능한 구간 수는
min(구간 개수, 곡괭이 총 개수)로 고정되므로, 그 구간들에 대해 어떤
곡괭이를 배정할지만 정하면 된다.

다이아몬드 곡괭이는 어떤 광물에도 피로도 1로, 다른 곡괭이보다 항상
같거나 낫다(우월 전략). 따라서:
1. 다이아몬드 곡괭이는 구간 내 다이아몬드 개수가 많은 구간부터 배정한다
   (다이아몬드 곡괭이를 아낄수록 손해가 큰 구간에 우선 배정).
2. 남은 구간 중에서는, 철 곡괭이 대신 돌 곡괭이를 썼을 때 손해
   (다이아몬드는 20, 철은 4 차이가 나므로 5*다이아몬드+철 개수 기준)가
   큰 구간부터 철 곡괭이를 배정한다.
3. 나머지는 돌 곡괭이로 채굴한다.

시간복잡도: O(K log K) (K = 사용되는 구간 수, 정렬 비용)
"""

COST = {
    "diamond": (1, 5, 25),  # (다이아몬드 곡괭이, 철 곡괭이, 돌 곡괭이) 사용 시 피로도
    "iron": (1, 1, 5),
    "stone": (1, 1, 1),
}


def solution(picks: list[int], minerals: list[str]) -> int:
    chunks = [minerals[i : i + 5] for i in range(0, len(minerals), 5)]
    total_picks = sum(picks)
    num_used = min(len(chunks), total_picks)
    used_chunks = chunks[:num_used]

    counts = []
    for chunk in used_chunks:
        counts.append(
            (chunk.count("diamond"), chunk.count("iron"), chunk.count("stone"))
        )

    assigned: list[int | None] = [None] * num_used

    diamond_order = sorted(range(num_used), key=lambda i: -counts[i][0])
    diamond_left = picks[0]
    for i in diamond_order:
        if diamond_left > 0:
            assigned[i] = 0
            diamond_left -= 1

    remaining = [i for i in range(num_used) if assigned[i] is None]
    remaining.sort(key=lambda i: -(5 * counts[i][0] + counts[i][1]))
    iron_left = picks[1]
    for i in remaining:
        if iron_left > 0:
            assigned[i] = 1
            iron_left -= 1

    for i in range(num_used):
        if assigned[i] is None:
            assigned[i] = 2

    total = 0
    for i in range(num_used):
        diamond_cnt, iron_cnt, stone_cnt = counts[i]
        pick_idx = assigned[i]
        total += (
            diamond_cnt * COST["diamond"][pick_idx]
            + iron_cnt * COST["iron"][pick_idx]
            + stone_cnt * COST["stone"][pick_idx]
        )
    return total
