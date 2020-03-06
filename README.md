# 🐚 Pretty Shell

### Shell Script formatter / syntax checker for Sublime Text 3
- [packagecontrol.io/packages/Pretty Shell](https://packagecontrol.io/packages/Pretty%20Shell)
- Powered by **[mvdan/sh](https://github.com/mvdan/sh)**, quality shell script formatter.
- **Blazingly fast**
- **Syntax check on demand** ([mvdan/sh#replacing-bash--n](https://github.com/mvdan/sh#replacing-bash--n))
- Recommended for shell scripting beginners.
    - I've written this plugin for myself to learn how to write shell scripts in correct syntax.
    - **Highly recommended to use this plugin with: [SublimeLinter-shellcheck](https://packagecontrol.io/packages/SublimeLinter-shellcheck)**

## 📦 Install
1. <kbd>Package Control: Install Package</kbd>
2. Type <kbd>PrettyShell</kbd> and Install
3. You're ready

### 📦 Manual Install
1. Clone this repository as shown below
2. You're ready (Restart Sublime Text if the package is not recognized)

```bash
# Example on macOS
git clone https://github.com/aerobounce/Sublime-Pretty-Shell.git "$HOME/Library/Application Support/Sublime Text 3/Packages/PrettyShell"
# It should work on Linux / Windows too,
# Follow the same steps with the equivalent clone target directory.
```

### ⚠️ Dependency
**Pretty Shell** does not work without `shfmt` as this package utilizes the formatter.<br>
`shfmt` is available via several package managers and binary releases by its author.<br>

- **macOS**
    - [Homebrew](https://formulae.brew.sh/formula/shfmt)
    - [MacPorts](https://ports.macports.org/port/shfmt/summary)
- **\*nix**
    - [Linuxbrew](https://github.com/Homebrew/linuxbrew-core/blob/master/Formula/shfmt.rb)
    - [Alpine](https://pkgs.alpinelinux.org/packages?name=shfmt)
    - [Arch](https://www.archlinux.org/packages/community/x86_64/shfmt/)
    - [FreeBSD](https://www.freshports.org/devel/shfmt)
    - [NixOS](https://github.com/NixOS/nixpkgs/blob/HEAD/pkgs/tools/text/shfmt/default.nix)
    - [Snapcraft](https://snapcraft.io/shfmt)
    - [Void](https://github.com/void-linux/void-packages/blob/HEAD/srcpkgs/shfmt/template)
- **Windows**
    - [Scoop](https://github.com/ScoopInstaller/Main/blob/HEAD/bucket/shfmt.json)
- **Pre-built binary releases**
    - [mvdan/sh/releases](https://github.com/mvdan/sh/releases)

If installed via a package manager and **Sublime Text** recognizes its path, that's it.<br>
Otherwise, specify the absolute path in the settings:

```JavaScript
"shfmt_bin_path": "Absolute Path to shfmt"
```

## ⌨️ Usage

### 📝 Available Commands
| Caption                                   | Command                         | Default Key Bindings                                              |
| ----------------------------------------- | ------------------------------- | ----------------------------------------------------------------- |
| <kbd>Pretty Shell: Format</kbd>           | `pretty_shell`                  | <kbd>cmd</kbd> or <kbd>alt</kbd> + <kbd>ctrl</kbd> + <kbd>s</kbd> |
| <kbd>Pretty Shell: Format Selection</kbd> | `pretty_shell_selection`        | None                                                              |
| <kbd>Pretty Shell: Minify</kbd>           | `pretty_shell_minify`           | None                                                              |
| <kbd>Pretty Shell: Minify Selection</kbd> | `pretty_shell_minify_selection` | None                                                              |

- **Command** is the name of the command you can use for **Key-Bindings**.
- Be aware that any manual modifications with `Format Selection` commands might be lost upon saving a file if `format_on_save` is `true`, which it is by default.

### 🛠 Default Settings
```javascript
// shfmt settings
"simplify": true,   // Simplify the code
"language": "bash", // Language variant to parse (bash / posix / mksh)
"indent": 4,        // 0 for tabs
"binop": false,     // Binary operators such as '&&' and '|' may start a line
"switchcase": true, // Indent switch cases
"rediop": true,     // Redirect operators will be followed by a space
"align": false,     // Keep column alignment paddings
"minify": false,    // Minify program to reduce its size

// Pretty Shell settings
"format_selection_only": false, // Entire file will be used if no selections
"format_on_save": true,
"shfmt_bin_path": "shfmt"
```

## ☑️ Todo
- [ ] Add `Show Syntax Error` option
- [x] Highlight `shfmt`'s error position using Phantom
- [x] ~Make output panel's coloring smarter? (like SublimeLinter)~
- [x] Make output panel always frontmost, as it's always fatal error `shfmt` cannot handle when it needs the panel
- [x] Add `Format Entire File` command
- [x] Add `Format Selection` command
- [x] Add `Minify Entire File` command
- [x] Add `Minify Selection` command
- [x] Add `format_selection_only` option

## 🤝 Special Thanks
- [dzhibas/SublimePrettyJson](https://github.com/dzhibas/SublimePrettyJson) (This project is inspired by the package)
- [mvdan/sh](https://github.com/mvdan/sh) (Shell formatter)
