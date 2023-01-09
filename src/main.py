import wx
from ui.mainWindow import MainFrame

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame(None, title='Main Frame')
    frame.Show()
    app.MainLoop()
