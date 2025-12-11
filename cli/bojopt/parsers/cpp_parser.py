import re


class CppParser:
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
            
            if '{' in line:
                pass
            if '}' in line:
                if current_depth > 0:
                    current_depth -= 1
        
        return max_depth
    
    def find_pattern(self, pattern):
        results = []
        
        for i, line in enumerate(self.code_lines, 1):
            if pattern == 'cin_cout':
                if re.search(r'\b(cin|cout)\b', line):
                    results.append({'lineno': i, 'type': pattern, 'line': line.strip()})
            elif pattern == 'sync_off':
                if re.search(r'sync_with_stdio\s*\(\s*false\s*\)', line):
                    return True
            elif pattern == 'vector_reserve':
                if re.search(r'\.reserve\s*\(', line):
                    return True
            elif pattern == 'map':
                if re.search(r'\bmap\s*<', line):
                    results.append({'lineno': i, 'type': pattern})
            elif pattern == 'size_in_loop':
                if re.search(r'\.size\s*\(\s*\)', line):
                    results.append({'lineno': i, 'type': pattern})
        
        return results if results else False
    
    def has_sync_off(self):
        for line in self.code_lines:
            if re.search(r'sync_with_stdio\s*\(\s*false\s*\)', line):
                return True
        return False
    
    def has_vector_reserve(self):
        for line in self.code_lines:
            if re.search(r'\.reserve\s*\(', line):
                return True
        return False
    
    def find_map_usage(self):
        results = []
        for i, line in enumerate(self.code_lines, 1):
            if re.search(r'\bmap\s*<', line) and not re.search(r'\bunordered_map\s*<', line):
                results.append({'lineno': i})
        return results
    
    def find_size_in_loop(self):
        results = []
        in_loop = False
        loop_start = 0
        
        for i, line in enumerate(self.code_lines, 1):
            if re.search(r'\b(for|while)\s*\(', line):
                in_loop = True
                loop_start = i
            
            if in_loop and re.search(r'\.size\s*\(\s*\)', line):
                if re.search(r'\bfor\s*\(', self.code_lines[loop_start - 1]):
                    if '.size()' in line:
                        results.append({'lineno': i})
        
        return results
