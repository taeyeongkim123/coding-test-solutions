"""AtCoder Beginner Contest 351 - C: Merge the Balls
https://atcoder.jp/contests/abc351/tasks/abc351_c

문제
----
빈 수열에 공을 하나씩 N번 추가한다. i번째 공의 크기는 2^{A_i}. 공을
맨 오른쪽에 추가할 때마다, "맨 오른쪽 두 공의 크기가 같으면 둘을
지우고 그 합(크기가 2배인 공 하나)을 맨 오른쪽에 추가"하는 과정을
더 이상 합칠 수 없을 때까지 반복한다. N번의 추가가 끝난 뒤 남은 공의
개수를 구하라.

접근
----
크기는 항상 2^k 꼴이라 지수 k만 스택에 저장하면 충분하다. 공을
추가할 때마다 지수를 push하고, 스택의 top 두 개가 같으면 pop해서
(값+1)을 다시 push하는 걸 반복한다(2^k + 2^k = 2^{k+1}이므로). 이건
2048류 병합 문제의 전형적인 스택 패턴이다. 각 공은 최대 한 번
push되고, merge로 인한 pop/push는 전체적으로 O(N)번을 넘지 않는다
(원소 하나가 사라지려면 그만큼 이전에 push가 있어야 하므로).

시간복잡도: O(N)
"""

import sys


def solve(n: int, a: list[int]) -> int:
    stack: list[int] = []
    for exp in a:
        stack.append(exp)
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            merged = stack.pop() + 1
            stack.pop()
            stack.append(merged)
    return len(stack)


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))
    print(solve(n, a))


if __name__ == "__main__":
    main()
