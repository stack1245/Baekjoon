import os
from pathlib import Path


class LanguageDetector:
    EXTENSIONS = {
        'python': ['.py'],
        'cpp': ['.cpp', '.cc', '.cxx', '.h', '.hpp'],
        'java': ['.java']
    }

    @classmethod
    def detect(cls, filepath):
        ext = Path(filepath).suffix.lower()
        
        for language, extensions in cls.EXTENSIONS.items():
            if ext in extensions:
                return language
        
        return None

    @classmethod
    def is_supported(cls, filepath):
        return cls.detect(filepath) is not None
