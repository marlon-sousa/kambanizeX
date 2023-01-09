import wx

class SettingsDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, title="settings")

        # Create the tab control
        self.tab_ctrl = wx.Notebook(self)

        # Create the first tab
        self.tab1 = wx.Panel(self.tab_ctrl)
        self.tab_ctrl.AddPage(self.tab1, "Test1")

        # Create the edit field and label for the API key
        self.api_key_label = wx.StaticText(self.tab1, label="API Key:")
        self.api_key_field = wx.TextCtrl(self.tab1)

        # Create the sizer for the tab
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.api_key_label, 0, wx.ALL, 5)
        sizer.Add(self.api_key_field, 0, wx.ALL, 5)

        # Set the sizer for the tab
        self.tab1.SetSizer(sizer)

        # Create the buttons
        self.ok_button = wx.Button(self, wx.ID_OK)
        self.apply_button = wx.Button(self, wx.ID_APPLY)
        self.cancel_button = wx.Button(self, wx.ID_CANCEL)

        # Create the button sizer
        button_sizer = wx.StdDialogButtonSizer()
        button_sizer.AddButton(self.ok_button)
        button_sizer.AddButton(self.apply_button)
        button_sizer.AddButton(self.cancel_button)
        button_sizer.Realize()

        # Create the main sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(self.tab_ctrl, 1, wx.EXPAND)
        main_sizer.Add(button_sizer, 0, wx.EXPAND|wx.BOTTOM|wx.TOP, 5)

        # Set the main sizer for the dialog
        self.SetSizer(main_sizer)
        main_sizer.Fit(self)

