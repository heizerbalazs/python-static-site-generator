from typing import ClassVar, List
from pathlib import Path

class Parser:
    extensions: List[str] = list()

    def validate_extension(self, extension: str) -> bool:
        return extension in self.extensions
    
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError