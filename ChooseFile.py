from Cocoa import NSOpenPanel, NSApplication, NSApp

class ChooseFile:
    def choose_file(self):
        self.panel = NSOpenPanel.openPanel()
        self.panel.setAllowsMultipleSelection_(False)
        self.panel.setCanChooseDirectories_(False)
        self.panel.setCanChooseFiles_(True)

        result = self.panel.runModal()
        if result == 1:
            self.selected_file_path = self.panel.URLs()[0].path()
            return self.selected_file_path
        else:
            return None