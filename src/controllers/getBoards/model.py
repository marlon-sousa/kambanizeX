from dataclasses import dataclass
from typing import List

@dataclass
class Board:
    id: int
    description: str
    name: str
    path: str

@dataclass
class GetBoardsPresenter:
    boards: List[Board]