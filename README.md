## 🐚 Pretty Shell

> Shell Script Formatter / Syntax Checker for Sublime Text 3<br>
> For Every Shell Scripters.<br>
> [Available via Package Control](https://packagecontrol.io/packages/Pretty%20Shell)

<table width="100%" style="border-spacing: 0px;">
<tr>
    <th><b>🚅 Blazingly Fast Formatting / Minifying</b></th>
    <th><b><a href="https://github.com/mvdan/sh#replacing-bash--n">🚦 Syntax Checking</a></b></th>
</tr>
<tr>
    <td colspan="2" style="padding: 0px; margin: 0px;">
        <img src="https://user-images.githubusercontent.com/10491362/78775969-0c057a00-79d2-11ea-942e-582f81849491.gif" style="display: block; width: 100%;" />
    </td>
</tr>
</table>


## 📦 Install
1. <kbd>Package Control: Install Package</kbd>
2. Type <kbd>PrettyShell</kbd> and Install
3. You're ready to script.
4. Recommended to use [SublimeLinter-shellcheck](https://packagecontrol.io/packages/SublimeLinter-shellcheck).

<blockquote>
<b>Manual Install</b>

```sh
# 1. Clone this repository as shown below
# 2. You're ready (Restart Sublime Text if the package is not recognized)

# Example on macOS (It should work on Linux / Windows too.
# Follow the same steps with the equivalent clone target directory)

cd "$HOME/Library/Application Support/Sublime Text 3/Packages"
git clone https://github.com/aerobounce/Sublime-Pretty-Shell.git "Pretty Shell"
```

</blockquote>

## ⚠️ Dependency
Pretty Shell **does not work without `shfmt`** as this package utilizes the formatter.<br>
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

> If Sublime Text does not recognize `shfmt`, specify the absolute path in the settings:
>
> ```JavaScript
> "shfmt_bin_path": "Absolute Path to shfmt"
> ```

## 📝 Available Commands

| Caption                                   | Command                         | Default Key Bindings                                              |
| ----------------------------------------- | ------------------------------- | ----------------------------------------------------------------- |
| <kbd>Pretty Shell: Format</kbd>           | `pretty_shell`                  | <kbd>cmd</kbd> or <kbd>alt</kbd> + <kbd>ctrl</kbd> + <kbd>s</kbd> |
| <kbd>Pretty Shell: Format Selection</kbd> | `pretty_shell_selection`        | None                                                              |
| <kbd>Pretty Shell: Minify</kbd>           | `pretty_shell_minify`           | None                                                              |
| <kbd>Pretty Shell: Minify Selection</kbd> | `pretty_shell_minify_selection` | None                                                              |

- **Command** is the name of the command you can use for **Key-Bindings**.
- Be aware that any manual modifications with `Format Selection` commands might be lost upon saving a file if `format_on_save` is `true`, which it is by default.

## 🛠 Default Settings

```javascript
/* Pretty Shell */
"format_selection_only": false, // Entire file will be used if no selection available
"format_on_save": true,         // Invoke "Pretty Shell: Format" command on save
"shfmt_bin_path": "shfmt",

/* shfmt */
"simplify": true,   // Simplify the code
"minify": false,    // Minify the code to reduce its size (implies "simplify")
"language": "bash", // Language variant to parse (bash / posix / mksh)
"indent": 4,        // 0 for tabs
"binop": false,     // Binary operators such as '&&' and '|' may start a line
"switchcase": true, // Indent switch cases
"rediop": true,     // Redirect operators will be followed by a space
"align": false,     // Keep column alignment paddings
"fnbrace": false    // Place function opening braces on a separate line
```

## 🤝 Thank you

- [dzhibas/SublimePrettyJson](https://github.com/dzhibas/SublimePrettyJson) — Inspired by this project
- [mvdan/sh](https://github.com/mvdan/sh) — Pretty Shell is powerd by shfmt, the quality formatter
- [realm/strip-frameworks.sh](https://github.com/realm/realm-cocoa/blob/master/scripts/strip-frameworks.sh) — Script used in the demo gif
