"""AtCoder Beginner Contest 459 - C: Drop Blocks (복습용 재풀이)
https://atcoder.jp/contests/abc459/tasks/abc459_c

문제
----
N개의 셀이 일렬로 있고 처음엔 모두 비어있다. Q개의 쿼리를 순서대로
처리한다:
- 타입 1 (1 x): x번째 셀에 블록 1개 추가. 그 후 모든 셀에 블록이 1개
  이상이면, 모든 셀에서 블록을 1개씩 제거한다.
- 타입 2 (2 y): 블록을 y개 이상 가진 셀의 개수를 출력한다.

접근
----
"모든 셀에서 1개씩 제거"를 실제로 배열 전체에 반영하면 O(N)이 걸려
느리므로, 오프셋(m_block)으로 퉁친다.

- D_list[x]: 셀 x에 실제로 추가된 블록 수(raw 값, 절대 감소하지 않음)
- max_list[k]: raw 값이 k 이상인 셀의 개수 (누적 카운트)
- m_block: 지금까지 "전부 제거" 이벤트가 발생한 횟수. 셀 x의 현재
  실제 블록 수는 D_list[x] - m_block과 같다.

타입 1 쿼리에서 D_list[x]를 늘릴 때마다 max_list[새 값]을 1 증가시킨다
(이전 값에 대한 감소 처리는 필요 없다 — max_list[k]가 "k 이상"의
누적 카운트이기 때문에, 예전 임계값들은 이미 올바르게 카운트돼 있음).

"모든 셀이 1개 이상"인지는 max_list[m_block+1] >= N으로 판정한다
(raw 값이 m_block+1 이상인 셀이 N개, 즉 전부라는 뜻). 한 번의 쿼리로는
raw 값이 최대 1만 증가하므로, 이 조건은 한 번에 최대 한 단계만
넘어간다 (cascade 없이 if 한 번으로 충분).

타입 2 쿼리(y)의 답은 "실제 블록 수 >= y"인 셀의 개수 = "raw >= y +
m_block"인 셀의 개수 = max_list[y + m_block].

배열 크기 주의: max_list는 인덱스로 y + m_block(둘 다 최대 3×10^5
근처까지 갈 수 있음, 특히 N=1이면 m_block이 쿼리마다 거의 매번
증가할 수 있어 최악의 경우 Q에 근접)을 쓰므로, 합이 6×10^5 근처까지
갈 수 있어 넉넉하게 잡아야 한다.

시간복잡도: O(N + Q)
"""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx])
    q = int(data[idx + 1])
    idx += 2

    limit = 6 * 10**5 + 5
    raw = [0] * (3 * 10**5 + 1)
    at_least = [0] * limit

    m_block = 0
    out = []
    for _ in range(q):
        t = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        if t == 1:
            raw[v] += 1
            at_least[raw[v]] += 1
            if at_least[m_block + 1] >= n:
                m_block += 1
        else:
            out.append(str(at_least[v + m_block]))

    print("\n".join(out))


if __name__ == "__main__":
    main()
