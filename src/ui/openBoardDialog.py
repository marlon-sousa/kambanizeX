import wx

from src.controllers.getBoards.model import Board, GetBoardsPresenter

class OpenBoardDialog(wx.Dialog):
    def __init__(self, parent:str, presenter: GetBoardsPresenter):
        super().__init__(parent, title="Open board")
        self.presenter = presenter
        self.boards: dict[int, Board] = {}
        self.buildLayout()
        self.render()

    def buildLayout(self):
        self.boardsList = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.boardsList.InsertColumn(0, "Name", width=50)
        self.boardsList.InsertColumn(1, "Description", width=200)
        self.boardsList.InsertColumn(2, "path", width=50)
        ok_button = wx.Button(self, wx.ID_OK)
        cancel_button = wx.Button(self, wx.ID_CANCEL)

        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        button_sizer.Add(ok_button)
        button_sizer.Add(cancel_button)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.SetSizer(sizer)

    def render(self):
        for board in self.presenter.boards:
            index = self.boardsList.InsertItem(board.name, board.description, board.path)
            self.boards[index] = board.id

    def getSelectedBoardId(self):
        selectedItem = self.boardsList.GetFirstSelected()
        return self.boards[selectedItem].id

