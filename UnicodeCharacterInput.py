import sublime
import sublime_plugin

class UnicodeCharacterInputHandler(sublime_plugin.TextInputHandler):
    def name(self):
        return "character"

    def placeholder(self):
        return "Hexadecimal code point"

    def preview(self, expr):
        if expr != "":
            try:
                actual_character = chr(int(expr, 16))

                return actual_character
            except:
                return "Invalid code point"

class UnicodeCharacterInputCommand(sublime_plugin.TextCommand):
    def run(self, edit, character):
        print(character)
        for region in self.view.sel():
            actual_character = chr(int(character, 16))
            self.view.replace(edit, region, actual_character)

    def input(self, args):
        return UnicodeCharacterInputHandler()
