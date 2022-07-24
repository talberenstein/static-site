from copyreg import constructor
from pathlib import Path

from yaml import DirectiveToken


class Site:
    def __init__(self, source, dest, parsers = None):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = parsers | []
    
    def create_dir(self, path):
        directory = self.dest / path.relattive_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

    def load_parser(extension):
        for self in self.parsers:
            self.parser