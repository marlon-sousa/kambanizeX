import wx

from .settingsDialog import SettingsDialog

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.render()

    def render(self):
        self.createMenus()
        # Create the status bar
        self.CreateStatusBar()

    def createMenus(self):
        # Create the menubar
        menubar = wx.MenuBar()

        # Create the File menu and its submenus
        file_menu = wx.Menu()
        open_board_menu_item = file_menu.Append(wx.ID_OPEN, 'Open Board...')
        settings_menu_item = file_menu.Append(wx.ID_ANY, 'settings...')
        file_menu.AppendSeparator()
        quit_menu_item = file_menu.Append(wx.ID_EXIT, 'Quit')

        # Create the Help menu and its submenu
        help_menu = wx.Menu()
        about_menu_item = help_menu.Append(wx.ID_ABOUT, 'About...')

        # Add the File and Help menus to the menubar
        menubar.Append(file_menu, 'File')
        menubar.Append(help_menu, 'Help')

        # Set the menubar as the top-level menu
        self.SetMenuBar(menubar)

        

        # Bind the events to their respective handlers
        self.Bind(wx.EVT_MENU, self.on_open_board, open_board_menu_item)
        self.Bind(wx.EVT_MENU, self.on_settings, settings_menu_item)
        self.Bind(wx.EVT_MENU, self.on_quit, quit_menu_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_menu_item)

    def on_open_board(self, event):
        # Open the board file
        pass

    def on_settings(self, event):
        # Show the about dialog
        settings_dialog = SettingsDialog(self)
        settings_dialog.ShowModal()
        settings_dialog.Destroy()


    def on_quit(self, event):
        self.Close()

    def on_about(self, event):
        # Show the about dialog
        about_dialog = wx.MessageDialog(self, 'About the program', 'About', wx.OK)
        about_dialog.ShowModal()
        about_dialog.Destroy()
