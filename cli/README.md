# BOJOpt - BOJ 코드 자동 최적화 분석기

Python, C++, Java로 작성된 백준(BOJ) 문제 풀이 코드를 분석하여 비효율적인 패턴과 성능 개선 포인트를 찾아주는 CLI 도구입니다.

## 설치

```bash
cd cli
pip install .
```

## 사용법

```bash
bojopt <소스코드_경로>
```

### 예시

```bash
bojopt solution.py
bojopt main.cpp
bojopt Solution.java
```

## 지원 언어

- Python (.py)
- C++ (.cpp, .cc, .cxx, .h, .hpp)
- Java (.java)

## 분석 기능

### 공통 분석
- 중첩 반복문 깊이 분석
- 시간 복잡도 추정
- 반복문 내 비효율적인 연산 감지

### Python 규칙
- 반복문 내 `input()` 사용 → `sys.stdin.readline()` 권장
- `list.pop(0)` 사용 감지 (O(n)) → `collections.deque` 권장
- 리스트에서 `in` 연산 → `set` 사용 권장
- 문자열 `+=` 반복 연결 → `join()` 권장
- 반복문 내 `print()` 사용 최적화

### C++ 규칙
- `cin/cout` 사용 시 `sync_with_stdio(false)` 확인
- `vector` 사용 시 `reserve()` 권장
- `map` → `unordered_map` 제안
- 반복문에서 `.size()` 반복 호출 최적화

### Java 규칙
- `Scanner` → `BufferedReader` 권장
- `String +=` 반복 연결 → `StringBuilder` 권장
- 배열/리스트 복사 최적화
- 반복문 내 출력 최적화

## 출력 예시

분석 결과는 색상이 있는 표 형식으로 출력되며, 다음 정보를 포함합니다:

- 시간 복잡도 추정
- 경고(Warning): 성능에 큰 영향을 주는 이슈
- 제안(Suggestion): 개선 가능한 패턴
- 정보(Info): 참고할 만한 최적화 팁

## 라이선스

MIT License
