import asyncio
import os
from typing import List
from functional import seq
from .model import Board, GetBoardsPresenter
from services.kanbanize.board import getBoards as getBoardsSvc
from services.kanbanize.workspace import getWorkspaces as getWorkspacesSvc
from services.kanbanize.workspace.model import Workspace

async def getBoards() -> GetBoardsPresenter:
    apiKey = os.getenv('API_KEY')
    [boards, workspaces] = await asyncio.gather(getBoardsSvc(apiKey), getWorkspacesSvc(apiKey))
    boards = seq(boards).map(lambda board: Board(board.board_id, board.description, board.name, getWorkspaceName(workspaces, board.workspace_id))).to_list()
    return GetBoardsPresenter(boards)

def getWorkspaceName(source: List[Workspace], workspaceId: int) -> str:
    return seq(source).find(lambda workspace: workspace.workspace_id == workspaceId).name or 'Umspecified'

