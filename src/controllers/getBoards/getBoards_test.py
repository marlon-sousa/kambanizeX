from unittest import IsolatedAsyncioTestCase

import dotenv
from . import getBoards

events = []


class Test(IsolatedAsyncioTestCase):

    async def test1(self):
        events.append("test_response")
        self.assertEqual(1, 1)
        print("aa")
        
    async def test2(self):
        dotenv.load_dotenv()
        res = await getBoards()
        self.assertEqual(1, 1)
        print(res)
