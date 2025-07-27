from dataclasses import dataclass
from pathlib import Path

from fastapi.templating import Jinja2Templates


@dataclass
class Notebook:
    name: str
    path: Path

    def __post_init__(self) -> None:
        ovrds = {'app1': 'Dashboard 1', 'app2': 'Dashboard 2'}
        self.name = ovrds.get(self.name, self.name)


Notebooks = list[Notebook]


def get_notebooks(dir: Path) -> Notebooks:
    notebooks = []
    for file in dir.iterdir():
        if file.suffix == '.py':
            notebooks.append(Notebook(file.stem, file.as_posix()))
    return sorted(notebooks, key=lambda nb: nb.name)


home = Path(__file__).parent.parent
templates = Jinja2Templates(directory=home / 'templates')
notebooks = get_notebooks(home / 'notebooks')
