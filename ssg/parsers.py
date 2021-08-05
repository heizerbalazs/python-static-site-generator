from typing import ClassVar, List
from pathlib import Path

class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension: str) -> bool:
        return extension in self.extensions
    
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path) -> str:
        with open(path, 'r') as file:
            return file.read()

    def write(self, path: Path, dest: Path, content: str, ext: str = '.html'):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)