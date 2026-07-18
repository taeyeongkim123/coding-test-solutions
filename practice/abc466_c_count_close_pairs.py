"""AtCoder Beginner Contest 466 - C: Count Close Pairs (인터랙티브)
https://atcoder.jp/contests/abc466/tasks/abc466_c

문제
----
수직선 위에 점 1, 2, ..., N이 왼쪽에서 오른쪽 순서로 놓여 있다(실제
좌표는 비공개). "1≤i<j≤N인 i, j를 골라 점 i와 점 j 사이 거리가 1
이하인지" 질문("? i j")을 최대 2N번까지 할 수 있다. 거리가 1 이하인
점 쌍의 개수를 구해 "! 답"으로 출력하라.

접근
----
좌표가 오름차순이므로, 고정된 i에 대해 "거리 1 이하인 j"들은 i+1부터
어떤 지점까지의 연속 구간을 이룬다(투 포인터의 전형적인 단조성 조건).
또한 i가 커질수록 이 구간의 오른쪽 끝도 절대 줄어들지 않는다: 같은 j에
대해 좌표 차이 coord(j)-coord(i)는 i가 커질수록만 줄어들기 때문에,
이전 i에서 이미 "거리 1 이하"로 확인된 j는 다음 i에서도 다시 물어볼
필요 없이 자동으로 성립한다.

그래서 포인터 j를 리셋 없이 이어서 사용한다. 각 i마다: (1) j가 i를
못 따라잡았으면 i+1로 끌어올리고, (2) ask(i, j)가 Yes인 동안 j를
계속 늘리다가, (3) 루프가 끝난 시점의 [i+1, j-1] 구간 전체 크기를
답에 더한다(새로 확인한 것 + 이전부터 자동으로 이어받은 것을 합친 값).

질문 횟수는 j가 총 N번 정도 전진하는 것과, 각 i마다 멈추는 데 드는
질문 한 번씩을 합쳐 대략 2N에 맞춰진다.

시간복잡도: O(N) 질의, O(N) 연산
"""

import sys


def ask(i: int, j: int) -> bool:
    print(f"? {i} {j}", flush=True)
    return sys.stdin.readline().strip() == "Yes"


def main() -> None:
    n = int(sys.stdin.readline())
    answer = 0
    j = 2
    for i in range(1, n + 1):
        if j <= i:
            j = i + 1
        while j <= n and ask(i, j):
            j += 1
        answer += max(0, j - 1 - i)
    print(f"! {answer}", flush=True)


if __name__ == "__main__":
    main()
