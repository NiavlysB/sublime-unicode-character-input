# Unicode Character Input

**ARCHIVED: Recent changes in GTK and/or iBus (?) seem to have brought the native Linux "Ctrl-Shift-U" behavior in ST4. Archiving this repository as a result (the plugin was never officially published).**

Sublime Text plugin (ST3/4) for inserting any Unicode character,
by entering its hexadecimal code.

Provides the “Ctrl-Shift-U” functionality that’s available under Linux but not in Sublime Text. In order to avoid clashes with other plugins though, this keymap is not enabled by default. To enable it, add the following to your keybindings:

    { "keys": ["ctrl+shift+u"], "command": "unicode_character_input" }

