# Unicode Character Input

Sublime Text plugin (ST3/4) for inserting any Unicode character,
by entering its hexadecimal code.

Provides the “Ctrl-Shift-U” functionality that’s available under Linux but not in Sublime Text. In order to avoid clashes with other plugins though, this keymap is not enabled by default. To enable it, add the following to your keybindings:

    { "keys": ["ctrl+shift+u"], "command": "unicode_character_input" }

