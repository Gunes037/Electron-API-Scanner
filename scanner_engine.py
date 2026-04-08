import re
from abc import ABC, abstractmethod

class Scanner(ABC):
    @abstractmethod
    def scan(self, content):
        pass

class APIKeyScanner(Scanner):
    def __init__(self):
        self.patterns = {
            'AWS': re.compile(r'AKIA[0-9A-Z]{16}'),
            'Google': re.compile(r'AIza[0-9A-Za-z-_]{35}')
        }

    def scan(self, content):
        results = []
        for key_type, pattern in self.patterns.items():
            for match in pattern.finditer(content):
                results.append({'type': key_type, 'key': match.group()})
        return results
