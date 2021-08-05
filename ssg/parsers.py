from typing import ClassVar, List
from pathlib import Path

class Parser:
    extensions: List[str] = list()

    def validate_extension(self, extension: str) -> bool:
        return extension in self.extensions