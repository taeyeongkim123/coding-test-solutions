"""파라메트릭 서치 (답을 이분탐색하는 템플릿)

"최댓값의 최소화" 또는 "최솟값의 최대화"를 구하는 문제에서, 후보 답 g가
"실현 가능한가?"를 판정하는 feasible(g) 함수가 단조성(g가 커질수록/작아질수록
가능→불가능으로 한 번만 바뀜)을 가질 때 사용한다.

여기 템플릿은 feasible(g)가 g가 작을수록 True, 클수록 False로 바뀌는
경우(=가능한 최댓값을 찾는 경우) 기준이다. lo는 항상 "실현 가능한 값"이라는
불변식을 유지하며, mid를 올림 나눗셈으로 계산해 lo=mid로 그 자신을 후보로
남겨두는 방식이라 루프 종료 후 lo가 바로 정답이 된다 (오프바이원 보정 불필요).

출처: ABC463 D - Maximize the Gap (atcoder/abc463/d_maximize_the_gap.py)
"""


def feasible(g: int) -> bool:
    raise NotImplementedError("문제에 맞게 구현")


def parametric_search_max(lo: int, hi: int) -> int:
    """[lo, hi] 범위에서 feasible(g)를 만족하는 가장 큰 g를 찾는다.

    사전 조건: feasible(lo)는 True여야 한다 (아니면 호출 전에 별도로
    -1 등 특수 케이스를 처리해야 함).
    """
    while lo < hi:
        mid = (lo + hi + 1) // 2  # 위로 올림
        if feasible(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo
