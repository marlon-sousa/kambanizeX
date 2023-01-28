from typing import List
import aiohttp

from services.kanbanize.workspace.model import Response, Workspace

async def getWorkspaces(apiKey: str) -> List[Workspace]:
    headers = {'apikey': apiKey}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://remessaonline.kanbanize.com/api/v2/workspaces', headers=headers) as resp:
            resp = await resp.text()
            return Response.Schema().loads(resp).data

