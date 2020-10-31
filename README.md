<h1 align="center">🐚 Pretty Shell</h1>
<h3 align="center">Shell Script Formatter / Syntax Checker for Sublime Text 3</h3>

<p align="center">
    <img src="https://img.shields.io/badge/Linux-yellow.svg" />
    <img src="https://img.shields.io/badge/macOS-blue.svg" />
    <img src="https://img.shields.io/badge/Windows-green.svg" />
    <img src="https://img.shields.io/badge/Sublime Text-3-brightgreen.svg" />
</p>

<p align="center">
    <b>⚡️Blazingly Fast Formatting / Minifying</b><br>
    <b>❗️User Friendly Syntax Error Indication</b><br>
    <b><a href="https://github.com/mvdan/sh#replacing-bash--n">🚦 Syntax Checking</a></b><br>
    <img src="https://user-images.githubusercontent.com/10491362/78775969-0c057a00-79d2-11ea-942e-582f81849491.gif" style="display: block; width: 100%;" />
</p>


---


## 📦 Install

- [Available via Package Control][packagecontrol]
1. `Package Control: Install Package`
2. Type `Pretty Shell` and Install

#### Manual Install

1. Clone this repository as shown below (**Note that target directory name must be `Pretty Shell`**)
2. You're ready (Restart Sublime Text if the package is not recognized)

```sh
# Example on macOS
# In other platforms, follow the same steps with the equivalent clone target directory

cd "$HOME/Library/Application Support/Sublime Text 3/Packages"
git clone https://github.com/aerobounce/Sublime-Pretty-Shell.git "Pretty Shell"
```


## ⚠️ Dependency

- **macOS Users**
    - If your default shell does not have the path to `shfmt`, you need to specify it in the settings.
- **\*nix / Windows Users**
    - You need to specify the path to `shfmt` in the settings.
- Example
    ```
    "shfmt_bin_path": "Absolute Path to shfmt"
    ```

**Pretty Shell does not work without `shfmt` as this package utilizes the formatter.**<br>
It is available via several package managers, and in pre-built binary form.<br>

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
- **Pre-Built Binary Releases**
    - [mvdan/sh/releases](https://github.com/mvdan/sh/releases)


## 📝 Available Commands

> **Command** is the name of the command you can use for **Key-Bindings**.

| Caption                            | Command                         | Default Key Bindings   |
| ---------------------------------- | ------------------------------- | ---------------------- |
| **Pretty Shell: Format**           | `pretty_shell`                  | (CMD / Alt) + Ctrl + S |
| **Pretty Shell: Format Selection** | `pretty_shell_selection`        | None                   |
| **Pretty Shell: Minify**           | `pretty_shell_minify`           | None                   |
| **Pretty Shell: Minify Selection** | `pretty_shell_minify_selection` | None                   |


## 🛠 Default Settings

```javascript
/* Pretty Shell */
"format_selection_only": false, // Entire file will still be formatted if there's no selection
"format_on_save": true,
"shfmt_bin_path": "shfmt",

/* shfmt */
/* (Leave these settings untouched to use shfmt's default behavior) */
"simplify": false,   // Simplify the code
"minify": false,     // Minify the code to reduce its size (implies "simplify")
"language": "",      // bash / posix / mksh (default: bash)
"indent": "",        // 0 for tabs
"binop": false,      // Binary operators such as '&&' and '|' may start a line
"switchcase": false, // Indent switch cases
"rediop": false,     // Redirect operators will be followed by a space
"align": false,      // Keep column alignment paddings
"fnbrace": false     // Place function opening braces on a separate line
```

## 🤝 Thank you

- [dzhibas/SublimePrettyJson][prettyjson] — Inspired by this project
- [mvdan/sh][shfmt] — Pretty Shell is powerd by shfmt, the quality formatter
- [realm/strip-frameworks.sh][realm] — Script used in the demo gif

[packagecontrol]: https://packagecontrol.io/packages/Pretty%20Shell
[shfmt]: https://github.com/mvdan/sh
[realm]: https://github.com/realm/realm-cocoa/blob/master/scripts/strip-frameworks.sh
[prettyjson]: https://github.com/dzhibas/SublimePrettyJson
