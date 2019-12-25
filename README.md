# Sublime Pretty Shell
Shell Script beautifier plugin for Sublime Text 3.\
Utilizes [mvdan/sh](https://github.com/mvdan/sh).\
\
Recommended for shell scripting beginners.\
I've written this plugin for myself to learn how to write scripts in correct syntax.


# Install
- Make sure you have `shfmt` installed.
- Currently waiting for merge into: [wbond/package_control_channel](https://github.com/wbond/package_control_channel).
- Til it's done, however, you can also manually install it (on macOS. Should work on Linux too by doing the same thing in the equivalent directory.):
```bash
git clone https://github.com/aerobounce/Sublime-Pretty-Shell.git "$HOME/Library/Application Support/Sublime Text 3/Packages/PrettyShell"
```
- And now you're ready, have fun — Make sure you restart ST3.


# Tips
Highly recommended to use this plugin with:

- [SublimeLinter-shellcheck](https://packagecontrol.io/packages/SublimeLinter-shellcheck)


# Options
```json
"language": "bash",  // Language variant to parse (bash / posix / mksh)
"simplify": true,    // Simplify the code
"binop": false,      // Binary operators such as '&&' and '|' may start a line
"switchcase": true,  // Indent switch cases
"rediop": true,      // Redirect operators will be followed by a space
"align": false,      // Keep column alignment paddings
"minify": false,     // Minify program to reduce its size
"indent": 4,         // 0 for tabs
"pretty_on_save": true
```


# Todo
- [ ] Show parsing errors
