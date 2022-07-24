from typing import List
from pathlib import Path
import shutil

class Parser:
    extensions: List[str] = []
    def valid_extension(self, extension):
        return extension.isin(self.extensions)

    def parse(path: Path, source: Path, dest: Path):
        raise NotImplementedError
    
    def read(path):
        with open(path) as file:
            return file.read()

    def write(path, dest, content, ext = ".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path) as file:
            file.write(content)
        
    def copy(path, source, dest):
        shutil.copy2(path, source)

class ResourceParse(Parser):
    extensions: List[str] = [".html", ".jpg", ".png", ".gif", ".css"]
    def parse(path, source, dest):
        Parser.copy(path, source, dest)