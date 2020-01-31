# 🐚 Pretty Shell

### Shell Script beautifier plugin for Sublime Text 3
- [packagecontrol.io/packages/Pretty Shell](https://packagecontrol.io/packages/Pretty%20Shell)
- Powered by [mvdan/sh](https://github.com/mvdan/sh), quality shell script formatter.

#### Recommended for shell scripting beginners
I've written this plugin for myself to learn how to write scripts in correct syntax.<br>
Highly recommended to use this plugin with:

- [SublimeLinter-shellcheck](https://packagecontrol.io/packages/SublimeLinter-shellcheck)

## Install
1. <kbd>Package Control: Install Package</kbd>
2. Type <kbd>PrettyShell</kbd> and Install
3. You're ready

### Manual Install on macOS / Linux / Windows
1. Quit Sublime Text
2. Clone this repository as shown below
3. You're ready

```bash
git clone https://github.com/aerobounce/Sublime-Pretty-Shell.git "$HOME/Library/Application Support/Sublime Text 3/Packages/PrettyShell"
```

- It should work on Linux / Windows too. Follow the same steps with the equivalent clone target directory.

### Dependency
**Pretty Shell** does not work without `shfmt` as this package utilizes the formatter.<br>
`shfmt` is available via several package managers.<br>

#### macOS
- [Homebrew](https://formulae.brew.sh/formula/shfmt)
- [MacPorts](https://ports.macports.org/port/shfmt/summary)

#### \*nix
- [Alpine](https://pkgs.alpinelinux.org/packages?name=shfmt)
- [Arch](https://www.archlinux.org/packages/community/x86_64/shfmt/)
- [FreeBSD](https://www.freshports.org/devel/shfmt)
- [NixOS](https://github.com/NixOS/nixpkgs/blob/HEAD/pkgs/tools/text/shfmt/default.nix)
- [Snapcraft](https://snapcraft.io/shfmt)
- [Void](https://github.com/void-linux/void-packages/blob/HEAD/srcpkgs/shfmt/template)

#### Windows
- [Scoop](https://github.com/ScoopInstaller/Main/blob/HEAD/bucket/shfmt.json)

#### Manual Download
- [mvdan/sh/releases](https://github.com/mvdan/sh/releases)

----

If installed via a package manager and **Sublime Text** recognize its path, that's it.<br>
Otherwise, specify full path to the executable in the settings:

```
"shfmt_bin_path": "FULL PATH to shfmt"
```

## Usage
1. <kbd>Command Palette...</kbd>
2. <kbd>Pretty Shell: Format</kbd>

or just save script file you are editing while `pretty_on_save` is `true`.

### Default Key Bindings
- macOS:   <kbd>cmd</kbd> + <kbd>ctrl</kbd> + <kbd>s</kbd>
- Linux:   <kbd>alt</kbd> + <kbd>ctrl</kbd> + <kbd>s</kbd>
- Windows: <kbd>alt</kbd> + <kbd>ctrl</kbd> + <kbd>s</kbd>

### Options
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
- [x] Show parsing errors
- [ ] Format only selection

## Special Thanks
- [dzhibas/SublimePrettyJson](https://github.com/dzhibas/SublimePrettyJson) (This project is inspired by the package)
- [mvdan/sh](https://github.com/mvdan/sh) (Shell formatter)
