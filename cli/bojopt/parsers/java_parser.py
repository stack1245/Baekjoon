import re


class JavaParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.code_lines = []
        self.loops = []
        
    def parse(self):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.code_lines = f.readlines()
            
            self._find_loops()
            return True
        except Exception:
            return False
    
    def _find_loops(self):
        for i, line in enumerate(self.code_lines, 1):
            if re.search(r'\bfor\s*\(', line):
                self.loops.append({'type': 'for', 'lineno': i})
            elif re.search(r'\bwhile\s*\(', line):
                self.loops.append({'type': 'while', 'lineno': i})
    
    def get_loop_depth(self):
        max_depth = 0
        current_depth = 0
        
        for line in self.code_lines:
            if re.search(r'\b(for|while)\s*\(', line):
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            
            if '}' in line:
                if current_depth > 0:
                    current_depth -= 1
        
        return max_depth
    
    def find_scanner_usage(self):
        results = []
        for i, line in enumerate(self.code_lines, 1):
            if re.search(r'\bScanner\b', line):
                results.append({'lineno': i})
        return results
    
    def find_string_concat(self):
        results = []
        for i, line in enumerate(self.code_lines, 1):
            if re.search(r'String\s+\w+\s*=\s*["\']', line):
                continue
            if re.search(r'\w+\s*\+=\s*["\']', line):
                results.append({'lineno': i})
        return results
    
    def find_buffered_reader(self):
        for line in self.code_lines:
            if re.search(r'\bBufferedReader\b', line):
                return True
        return False
    
    def find_string_builder(self):
        for line in self.code_lines:
            if re.search(r'\bStringBuilder\b', line):
                return True
        return False
