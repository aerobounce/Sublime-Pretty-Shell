# Pretty Shell

## Shell Script beautifier plugin for Sublime Text 3.
Utilizes [mvdan/sh](https://github.com/mvdan/sh), quality shell script formatter.

## Recommended for shell scripting beginners.
I've written this plugin for myself to learn how to write scripts in correct syntax.

## Install
1. `Package Control: Install Package`
2. Type `PrettyShell` and Install
3. You're ready

## Install (Manual)
1. Quit Sublime Text
2. Clone this repository

```bash
git clone https://github.com/aerobounce/Sublime-Pretty-Shell.git "$HOME/Library/Application Support/Sublime Text 3/Packages/PrettyShell"
```

3. You're ready

- It should work on Linux too. Follow the same steps as macOS' with the equivalent clone target directory.

## Dependency
Make sure you have installed `shfmt` as this package utilizes the formatter.\
You can install it with Homebrew:

```bash
brew install shfmt
```

## Tips
Highly recommended to use this plugin with:

- [SublimeLinter-shellcheck](https://packagecontrol.io/packages/SublimeLinter-shellcheck)

## Options
```javascript
    "simplify": true,    // Simplify the code
    "language": "bash",  // Language variant to parse (bash / posix / mksh)
    "indent": 4,         // 0 for tabs
    "binop": false,      // Binary operators such as '&&' and '|' may start a line
    "switchcase": true,  // Indent switch cases
    "rediop": true,      // Redirect operators will be followed by a space
    "align": false,      // Keep column alignment paddings
    "minify": false,     // Minify program to reduce its size
    "pretty_on_save": true
```

# Todo
- [ ] Show parsing errors

# Special Thanks
- [dzhibas/SublimePrettyJson](https://github.com/dzhibas/SublimePrettyJson) (This project is inspired by the package)
- [mvdan/sh](https://github.com/mvdan/sh) (Shell formatter)
