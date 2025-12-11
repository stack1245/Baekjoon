class ComplexityEstimator:
    @staticmethod
    def estimate(loop_depth, has_sort=False, has_nested_operations=False):
        if loop_depth == 0:
            return "O(1)"
        elif loop_depth == 1:
            if has_sort:
                return "O(n log n)"
            return "O(n)"
        elif loop_depth == 2:
            if has_sort:
                return "O(n^2 log n)"
            return "O(n^2)"
        elif loop_depth == 3:
            return "O(n^3)"
        else:
            return f"O(n^{loop_depth})"
    
    @staticmethod
    def estimate_from_parser(parser, language):
        loop_depth = parser.get_loop_depth()
        has_sort = False
        
        if language == 'python':
            sort_patterns = parser.find_pattern_in_loops('sort')
            has_sort = len(sort_patterns) > 0
        elif language in ['cpp', 'java']:
            for line in parser.code_lines:
                if 'sort' in line.lower():
                    has_sort = True
                    break
        
        return ComplexityEstimator.estimate(loop_depth, has_sort)
