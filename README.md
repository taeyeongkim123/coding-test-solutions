# atcoder-solutions

CS 알고리즘 학습 기록용으로 [AtCoder](https://atcoder.jp/) 문제를 풀고 정리하는
저장소입니다. 각 풀이는 실제 저지에 제출 가능한 형태(표준입력 → 표준출력)로
작성하고, 공식 예제 입출력을 그대로 pytest 테스트로 남겨서 나중에 코드를
고쳐도 회귀(regression)가 바로 드러나게 했습니다.

## 구조

```
atcoder-solutions/
├── abc458/
│   └── c_stands_for_center.py
├── abc462/
│   └── c_not_covered_points.py
├── abc463/
│   ├── c_tallest_at_the_moment.py
│   └── d_maximize_the_gap.py
├── abc464/
│   └── c_plumage_palette.py
└── tests/
    └── test_solutions.py   # 문제별 공식 예제 입출력으로 회귀 테스트
```

콘테스트별로 폴더를 나누고, 파일명은 `{문제기호}_{영문제목_스네이크케이스}.py`
형식을 씁니다.

## 풀이 목록

| 문제 | 난이도 | 핵심 아이디어 | 시간복잡도 |
|---|---|---|---|
| [ABC458 C - C Stands for Center](https://atcoder.jp/contests/abc458/tasks/abc458_c) | 400 | 각 'C'를 중심으로 대칭 확장 가능한 반지름 계산 | O(N) |
| [ABC462 C - Not Covered Points](https://atcoder.jp/contests/abc462/tasks/abc462_c) | 300 | X 오름차순 정렬 + Y의 접두사 최솟값(prefix minimum) | O(N log N) |
| [ABC463 C - Tallest at the Moment](https://atcoder.jp/contests/abc463/tasks/abc463_c) | 300 | 접미사 최댓값 배열 + 이분 탐색 | O((N+Q) log N) |
| [ABC463 D - Maximize the Gap](https://atcoder.jp/contests/abc463/tasks/abc463_d) | 500 | 이분 탐색(정답) + 구간 스케줄링 탐욕으로 실현 가능성 판정 | O(N log N log C) |
| [ABC464 C - Plumage Palette](https://atcoder.jp/contests/abc464/tasks/abc464_c) | 300 | 색이 바뀌는 날짜만 이벤트로 처리해 distinct 개수 증분 관리 | O(N+M) |

각 풀이 파일 맨 위 docstring에 문제 요약과 접근 방식을 한국어로 정리해뒀습니다.

## 실행 방법

```bash
python abc463/c_tallest_at_the_moment.py < input.txt
```

각 스크립트는 표준입력으로 문제의 입력 형식을 그대로 받고, 표준출력으로
답을 출력합니다 — AtCoder 코드 테스트 창에 그대로 붙여넣어도 동작하는
형태입니다.

## 테스트

```bash
pip install -r requirements-dev.txt
pytest
```

`tests/test_solutions.py`는 각 문제의 공식 예제 입력을 서브프로세스로 실제
스크립트에 흘려보내고, 표준출력을 공식 예제 출력과 비교합니다. 예제 테스트가
통과한다고 해서 실제 저지에서 통과(특히 시간복잡도)한다는 보장은 아니지만,
로직이 깨졌는지는 바로 잡아냅니다.

## 새 문제 추가하는 법

1. `{콘테스트명}/` 폴더가 없으면 새로 만듭니다 (예: `abc465/`).
2. `{문제기호}_{영문제목}.py` 형식으로 풀이 파일을 추가합니다. 표준입력을
   읽어 표준출력에 답을 쓰는 `main()` 함수 형태를 따르고, 파일 상단에 문제
   요약·접근 방식·시간복잡도를 docstring으로 남깁니다.
3. `tests/test_solutions.py`의 `CASES` 리스트에 공식 예제 입출력을
   추가합니다.
4. 이 README의 "풀이 목록" 표에 한 줄 추가합니다.
5. `pytest`로 통과하는지 확인 후 커밋합니다.

## 라이선스

MIT
