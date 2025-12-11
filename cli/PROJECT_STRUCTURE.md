# BOJOpt 프로젝트 구조

```
cli/
├── bojopt/                          # 메인 패키지
│   ├── __init__.py                 # 패키지 초기화 (버전 정보)
│   ├── cli.py                      # CLI 진입점 (argparse 기반)
│   │
│   ├── detectors/                  # 언어 감지 모듈
│   │   ├── __init__.py
│   │   └── language_detector.py   # 파일 확장자 기반 언어 감지
│   │
│   ├── parsers/                    # 코드 파싱 모듈
│   │   ├── __init__.py
│   │   ├── python_parser.py       # Python AST 기반 파서
│   │   ├── cpp_parser.py          # C++ 정규식 기반 파서
│   │   └── java_parser.py         # Java 정규식 기반 파서
│   │
│   ├── analysis/                   # 분석 모듈
│   │   ├── __init__.py
│   │   ├── complexity_estimator.py # 시간 복잡도 추정
│   │   └── pattern_scanner.py     # 규칙 기반 패턴 스캐너
│   │
│   ├── rules/                      # JSON 규칙 파일
│   │   ├── python_rules.json      # Python 최적화 규칙
│   │   ├── cpp_rules.json         # C++ 최적화 규칙
│   │   └── java_rules.json        # Java 최적화 규칙
│   │
│   └── report/                     # 결과 출력 모듈
│       ├── __init__.py
│       └── reporter.py            # Rich 기반 출력
│
├── pyproject.toml                  # 패키지 설정
├── README.md                       # 프로젝트 설명
├── USAGE.md                        # 사용법 가이드
└── .gitignore                      # Git 제외 파일
```

## 모듈 설명

### 1. detectors/language_detector.py
- 파일 확장자를 기반으로 언어 감지
- 지원: Python (.py), C++ (.cpp, .cc, .cxx, .h, .hpp), Java (.java)

### 2. parsers/
- **python_parser.py**: Python `ast` 모듈을 사용한 구문 분석
  - 반복문 깊이 계산
  - 패턴 매칭 (input, pop(0), sort, print 등)
  
- **cpp_parser.py**: 정규식 기반 C++ 코드 분석
  - 반복문 감지
  - cin/cout, map, vector, size() 패턴 검색
  
- **java_parser.py**: 정규식 기반 Java 코드 분석
  - Scanner, String 연결, BufferedReader 등 검사

### 3. analysis/
- **complexity_estimator.py**: 반복문 깊이를 기반으로 시간 복잡도 추정
- **pattern_scanner.py**: JSON 규칙을 로드하여 패턴 스캔

### 4. rules/
각 언어별 최적화 규칙을 JSON 형식으로 정의

```json
{
  "pattern": "정규식_패턴",
  "message": "사용자에게 보여줄 메시지",
  "severity": "warning|suggestion|info",
  "check_type": "regex|parser_method"
}
```

### 5. report/reporter.py
- Rich 라이브러리를 사용한 컬러풀한 출력
- 테이블, 패널, 텍스트 스타일링
- 심각도별 색상 구분

### 6. cli.py
- argparse를 사용한 CLI 구현
- 전체 분석 프로세스 조율
- 파일 검증 및 에러 처리

## 실행 흐름

```
1. CLI 진입 (cli.py)
   ↓
2. 파일 존재 확인
   ↓
3. 언어 감지 (LanguageDetector)
   ↓
4. 파서 생성 및 파싱
   ↓
5. 시간 복잡도 추정 (ComplexityEstimator)
   ↓
6. 패턴 스캔 (PatternScanner)
   ↓
7. 결과 출력 (Reporter)
```

## 설치 및 실행

```bash
# 설치
cd cli
pip install -e .

# 실행
bojopt <파일경로>
```

## 주요 기능

1. **언어별 파서**: Python은 AST, C++/Java는 정규식 기반
2. **모듈화된 구조**: 각 모듈이 독립적으로 동작
3. **JSON 규칙 엔진**: 규칙을 JSON으로 관리하여 확장 용이
4. **Rich 출력**: 컬러풀하고 보기 좋은 터미널 출력
5. **시간 복잡도 추정**: 반복문 분석을 통한 자동 추정
6. **패키지 설치**: pip를 통한 간편한 설치 및 사용
