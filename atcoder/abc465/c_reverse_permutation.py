"""AtCoder Beginner Contest 465 - C: Reverse Permutation
https://atcoder.jp/contests/abc465/tasks/abc465_c

문제
----
정수 N과 길이 N인 문자열 S('o'/'x')가 주어진다. 수열 A = (1, 2, ..., N)에서 시작해
k = 1..N을 순서대로 보면서 S[k] = 'o'이면 A의 앞 k개 원소를 뒤집는다. 최종 A를 출력.

접근
----
매번 실제로 앞 k개를 뒤집으면 최악 O(N^2)라 시간초과 (N <= 5*10^5).
값 k를 1..N 순서로 하나씩 "현재 배열의 진짜 오른쪽 끝"에 추가한다고 생각하면,
R_k는 그 직후에 적용되는 뒤집기이므로 deque에 실제로 반영하지 않고
"진짜 오른쪽 끝이 deque의 어느 쪽인지"를 나타내는 방향 플래그만 토글해서 O(1)에 처리 가능.
=> 방향에 따라 append/appendleft로 값을 넣고, S[k]='o'면 방향을 뒤집는다 (넣은 다음에 뒤집는 순서가 중요).
루프 종료 시 direction이 -1이면 deque의 좌우가 실제 정답과 반대이므로 마지막에 한 번 더 뒤집어야 한다.
전체 O(N).
"""

import sys
from collections import deque


def solve(n: int, s: str) -> list[int]:
    queue: deque[int] = deque()
    direction = 1
    for i in range(1, n + 1):
        if direction == 1:
            queue.append(i)
        else:
            queue.appendleft(i)

        if s[i - 1] == "o":
            direction *= -1

    result = list(queue)
    if direction == -1:
        result.reverse()
    return result


def main() -> None:
    n = int(sys.stdin.readline().rstrip())
    s = sys.stdin.readline().rstrip()
    print(' '.join(map(str, solve(n, s))))


if __name__ == "__main__":
    main()
