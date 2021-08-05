from pathlib import Path

class Site:
    def __init__(self, source: str, dest: str) -> None:
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path: Path):
        destination = self.dest / path.relative_to(self.source)