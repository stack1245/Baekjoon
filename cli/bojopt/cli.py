import argparse
import sys
from pathlib import Path

from bojopt.detectors.language_detector import LanguageDetector
from bojopt.parsers.python_parser import PythonParser
from bojopt.parsers.cpp_parser import CppParser
from bojopt.parsers.java_parser import JavaParser
from bojopt.analysis.complexity_estimator import ComplexityEstimator
from bojopt.analysis.pattern_scanner import PatternScanner
from bojopt.report.reporter import Reporter


def get_parser_for_language(language, filepath):
    parsers = {
        'python': PythonParser,
        'cpp': CppParser,
        'java': JavaParser
    }
    
    parser_class = parsers.get(language)
    if parser_class:
        return parser_class(filepath)
    return None


def analyze_file(filepath):
    reporter = Reporter()
    
    if not Path(filepath).exists():
        reporter.print_error(f"파일을 찾을 수 없습니다: {filepath}")
        return 1
    
    language = LanguageDetector.detect(filepath)
    
    if not language:
        reporter.print_error(f"지원하지 않는 파일 형식입니다: {filepath}")
        reporter.print_error("지원 언어: Python (.py), C++ (.cpp, .cc, .cxx, .h, .hpp), Java (.java)")
        return 1
    
    parser = get_parser_for_language(language, filepath)
    
    if not parser:
        reporter.print_error(f"파서를 생성할 수 없습니다: {language}")
        return 1
    
    if not parser.parse():
        reporter.print_error(f"파일 파싱에 실패했습니다: {filepath}")
        return 1
    
    reporter.print_header(filepath, language)
    
    complexity = ComplexityEstimator.estimate_from_parser(parser, language)
    reporter.print_complexity(complexity)
    
    scanner = PatternScanner(language)
    issues = scanner.scan(parser)
    
    reporter.print_issues(issues)
    reporter.print_summary(issues)
    
    return 0


def main():
    parser = argparse.ArgumentParser(
        prog='bojopt',
        description='BOJ 코드 자동 최적화 분석기',
        epilog='예시: bojopt solution.py'
    )
    
    parser.add_argument(
        'filepath',
        type=str,
        help='분석할 소스 코드 파일 경로'
    )
    
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='bojopt 0.1.0'
    )
    
    args = parser.parse_args()
    
    return analyze_file(args.filepath)


if __name__ == '__main__':
    sys.exit(main())
