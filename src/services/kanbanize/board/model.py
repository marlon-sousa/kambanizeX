from typing import ClassVar, List, Type
from marshmallow_dataclass import dataclass
from marshmallow import Schema

@dataclass
class Board:
    board_id: int
    workspace_id: int
    is_archived: int
    name: str
    description: str
    Schema: ClassVar[Type[Schema]] = Schema

@dataclass
class Response:
    data: List[Board]
    Schema: ClassVar[Type[Schema]] = Schema