import ast


class PythonParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tree = None
        self.code_lines = []
        self.loops = []
        self.functions = []
        
    def parse(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            code = f.read()
            self.code_lines = code.split('\n')
            
        try:
            self.tree = ast.parse(code)
            self._analyze_tree()
            return True
        except SyntaxError:
            return False
    
    def _analyze_tree(self):
        for node in ast.walk(self.tree):
            if isinstance(node, (ast.For, ast.While)):
                self.loops.append({
                    'type': 'for' if isinstance(node, ast.For) else 'while',
                    'lineno': node.lineno,
                    'node': node
                })
            elif isinstance(node, ast.FunctionDef):
                self.functions.append({
                    'name': node.name,
                    'lineno': node.lineno,
                    'node': node
                })
    
    def get_loop_depth(self, node=None):
        if node is None:
            node = self.tree
            
        max_depth = 0
        
        for child in ast.walk(node):
            if isinstance(child, (ast.For, ast.While)):
                depth = 1 + self._count_nested_loops(child)
                max_depth = max(max_depth, depth)
        
        return max_depth
    
    def _count_nested_loops(self, node):
        max_depth = 0
        
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.For, ast.While)):
                depth = 1 + self._count_nested_loops(child)
                max_depth = max(max_depth, depth)
            else:
                depth = self._count_nested_loops(child)
                max_depth = max(max_depth, depth)
        
        return max_depth
    
    def find_pattern_in_loops(self, pattern):
        results = []
        
        for loop in self.loops:
            for node in ast.walk(loop['node']):
                if self._match_pattern(node, pattern):
                    results.append({
                        'lineno': getattr(node, 'lineno', loop['lineno']),
                        'type': pattern
                    })
        
        return results
    
    def _match_pattern(self, node, pattern):
        if pattern == 'input':
            return (isinstance(node, ast.Call) and 
                   isinstance(node.func, ast.Name) and 
                   node.func.id == 'input')
        elif pattern == 'list.pop(0)':
            return (isinstance(node, ast.Call) and
                   isinstance(node.func, ast.Attribute) and
                   node.func.attr == 'pop' and
                   len(node.args) > 0 and
                   isinstance(node.args[0], ast.Constant) and
                   node.args[0].value == 0)
        elif pattern == 'sort':
            return (isinstance(node, ast.Call) and
                   isinstance(node.func, ast.Attribute) and
                   node.func.attr == 'sort')
        elif pattern == 'print':
            return (isinstance(node, ast.Call) and
                   isinstance(node.func, ast.Name) and
                   node.func.id == 'print')
        elif pattern == 'string_concat':
            return (isinstance(node, ast.AugAssign) and
                   isinstance(node.op, ast.Add))
        
        return False
    
    def has_in_operator_on_list(self):
        results = []
        
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Compare):
                for op in node.ops:
                    if isinstance(op, (ast.In, ast.NotIn)):
                        results.append({
                            'lineno': node.lineno,
                            'type': 'in_operator'
                        })
        
        return results
