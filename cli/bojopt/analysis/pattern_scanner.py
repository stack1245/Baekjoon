import json
import re
from pathlib import Path


class PatternScanner:
    def __init__(self, language):
        self.language = language
        self.rules = []
        self._load_rules()
    
    def _load_rules(self):
        rules_dir = Path(__file__).parent.parent / 'rules'
        rules_file = rules_dir / f'{self.language}_rules.json'
        
        if rules_file.exists():
            with open(rules_file, 'r', encoding='utf-8') as f:
                self.rules = json.load(f)
    
    def scan(self, parser):
        issues = []
        
        for rule in self.rules:
            pattern = rule.get('pattern')
            message = rule.get('message')
            severity = rule.get('severity', 'info')
            check_type = rule.get('check_type', 'regex')
            
            if check_type == 'regex':
                found_issues = self._check_regex_pattern(parser, pattern, message, severity)
                issues.extend(found_issues)
            elif check_type == 'parser_method':
                found_issues = self._check_parser_method(parser, pattern, message, severity)
                issues.extend(found_issues)
        
        return issues
    
    def _check_regex_pattern(self, parser, pattern, message, severity):
        issues = []
        
        for i, line in enumerate(parser.code_lines, 1):
            if isinstance(line, str) and re.search(pattern, line):
                in_loop = self._is_in_loop(parser, i)
                if in_loop or 'loop' not in message.lower():
                    issues.append({
                        'line': i,
                        'message': message,
                        'severity': severity,
                        'code': line.strip()
                    })
        
        return issues
    
    def _check_parser_method(self, parser, method_name, message, severity):
        issues = []
        
        if hasattr(parser, method_name):
            method = getattr(parser, method_name)
            results = method()
            
            if isinstance(results, list):
                for result in results:
                    issues.append({
                        'line': result.get('lineno', 0),
                        'message': message,
                        'severity': severity,
                        'code': ''
                    })
            elif isinstance(results, bool) and not results:
                issues.append({
                    'line': 0,
                    'message': message,
                    'severity': severity,
                    'code': ''
                })
        
        return issues
    
    def _is_in_loop(self, parser, lineno):
        if not hasattr(parser, 'loops'):
            return False
        
        for loop in parser.loops:
            loop_line = loop.get('lineno', 0)
            if loop_line <= lineno <= loop_line + 50:
                return True
        
        return False
