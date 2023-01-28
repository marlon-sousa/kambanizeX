from typing import List
import aiohttp

from services.kanbanize.board.model import Board, Response

async def getBoards(apiKey: str) -> List[Board]:
    headers = {'apikey': apiKey}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://remessaonline.kanbanize.com/api/v2/boards', headers=headers) as resp:
            resp = await resp.text()
            return Response.Schema().loads(resp).data

