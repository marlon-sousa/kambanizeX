import wx
from wxasync import AsyncBind, WxAsyncApp, StartCoroutine
import wxasync
import asyncio
from ui.mainWindow import MainFrame
import dotenv

async def main():
    app = WxAsyncApp()
    frame = MainFrame(None, title='KanbanizeX')
    frame.Show()
    app.SetTopWindow(frame)
    await app.MainLoop()

if __name__ == '__main__':
    dotenv.load_dotenv()
    asyncio.run(main())