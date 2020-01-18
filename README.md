# Pretty Shell

## Shell Script beautifier plugin for Sublime Text 3.
Utilizes [mvdan/sh](https://github.com/mvdan/sh), quality shell script formatter.

## Recommended for shell scripting beginners.
I've written this plugin for myself to learn how to write scripts in correct syntax.<br>
Highly recommended to use this plugin with:

- [SublimeLinter-shellcheck](https://packagecontrol.io/packages/SublimeLinter-shellcheck)

## Dependency
Make sure you have installed `shfmt` as this package utilizes the formatter.<br>
You can install it with Homebrew:

```bash
brew install shfmt
```

## Install
1. `Package Control: Install Package`
2. Type `PrettyShell` and Install
3. You're ready

### Install (Manually)
1. Quit Sublime Text
2. Clone this repository as shown below
3. You're ready

- It should work on Linux too. Follow the same steps as above with the equivalent clone target directory.

```bash
git clone https://github.com/aerobounce/Sublime-Pretty-Shell.git "$HOME/Library/Application Support/Sublime Text 3/Packages/PrettyShell"
```

## Usage
1. `Command Palette...`
2. `Pretty Shell: Format`

or just save script file you are editing while `pretty_on_save` is `true`.

### Key Binding
Default Key Binding

- macOS: <kbd>cmd</kbd>+<kbd>ctrl</kbd>+<kbd>s</kbd>
- Linux: <kbd>alt</kbd>+<kbd>ctrl</kbd>+<kbd>s</kbd>

## Options
```javascript
"simplify": true, // Simplify the code
"language": "bash", // Language variant to parse (bash / posix / mksh)
"indent": 4, // 0 for tabs
"binop": false, // Binary operators such as '&&' and '|' may start a line
"switchcase": true, // Indent switch cases
"rediop": true, // Redirect operators will be followed by a space
"align": false, // Keep column alignment paddings
"minify": false, // Minify program to reduce its size
"pretty_on_save": true,
"shfmt_bin_path": "shfmt"
```

## Todo
- [ ] Show parsing errors
- [ ] Format only selection

## Special Thanks
- [dzhibas/SublimePrettyJson](https://github.com/dzhibas/SublimePrettyJson) (This project is inspired by the package)
- [mvdan/sh](https://github.com/mvdan/sh) (Shell formatter)
