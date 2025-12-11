# 사용 예시

## 1. 기본 사용법

프로젝트를 설치한 후 다음과 같이 사용합니다:

```bash
bojopt <파일경로>
```

## 2. Python 코드 분석

```bash
bojopt solution.py
bojopt problem/python/1874.py
```

## 3. C++ 코드 분석

```bash
bojopt main.cpp
bojopt solution.cc
```

## 4. Java 코드 분석

```bash
bojopt Solution.java
```

## 5. 설치

```bash
cd cli
pip install -e .
```

개발 모드로 설치하면 코드 수정 시 재설치 없이 바로 적용됩니다.

## 6. 버전 확인

```bash
bojopt --version
```

## 7. 도움말

```bash
bojopt --help
```

## 실행 결과 예시

분석 결과는 다음과 같이 표시됩니다:

1. **헤더**: 파일 경로와 언어 정보
2. **시간 복잡도**: 예상 시간 복잡도 (색상으로 구분)
   - 초록색: O(1), O(n), O(n log n)
   - 노란색: O(n^2)
   - 빨간색: O(n^3) 이상
3. **이슈 목록**: 발견된 최적화 포인트
   - ⚠ WARNING: 심각한 성능 문제
   - 💡 SUGGESTION: 개선 제안
   - ℹ INFO: 참고 정보
4. **요약**: 전체 이슈 개수

## 8. 주요 탐지 패턴

### Python
- 반복문 내 `input()` → `sys.stdin.readline()` 권장
- `list.pop(0)` → `collections.deque` 권장
- 리스트에서 `in` 검색 → `set` 권장
- 문자열 `+=` 반복 → `''.join()` 권장

### C++
- `cin/cout` 사용 시 `sync_with_stdio(false)` 확인
- `vector.reserve()` 사용 권장
- `map` → `unordered_map` 제안
- `.size()` 반복 호출 최적화

### Java
- `Scanner` → `BufferedReader` 권장
- `String +=` → `StringBuilder` 권장
- 반복문 내 출력 최적화
