from typing import ClassVar, List, Type
from marshmallow_dataclass import dataclass
from marshmallow import Schema

@dataclass
class Workspace:
    workspace_id: int
    type: int
    is_archived: int  
    name: str
    Schema: ClassVar[Type[Schema]] = Schema

@dataclass
class Response:
    data: List[Workspace]
    Schema: ClassVar[Type[Schema]] = Schema