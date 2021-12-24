<h1 align="center">🐚 Pretty Shell</h1>
<h3 align="center">Shell Script Formatter / Syntax Checker for Sublime Text 3</h3>

<p align="center">
    <img src="https://img.shields.io/badge/Linux / macOS / Windows-blue.svg" />
    <img src="https://img.shields.io/badge/Sublime Text-3-brightgreen.svg" />
</p>

<p align="center">
    <b>⚡️Blazingly Fast Formatting / Minifying</b><br>
    <b>❗️User Friendly Syntax Error Indication</b><br>
    <b><a href="https://github.com/mvdan/sh#replacing-bash--n">🚦Syntax Checking</a></b><br><br>
    <img src="https://user-images.githubusercontent.com/10491362/78775969-0c057a00-79d2-11ea-942e-582f81849491.gif" style="display: block; width: 100%;" />
    <br>
</p>


# Highlights

- ✨ Format on save
- Format selection
- Syntax errors are shown in popup with messages
    - ✨ Popup will be presented at the point error occured
- ✨ Auto-scroll to the point where the syntax error occured


# Install

> [Available via Package Control][packagecontrol]

1. `Package Control: Install Package`
2. Type `Pretty Shell` and Install

### Manual Install

1. Clone this repository to `.../Sublime Text 3/Packages/` (Note that target directory name must be `Pretty Shell`)
2. Ready (Restart Sublime Text if the package is not recognized)

### Requirements

`shfmt`

> Available via variety of ways. Visit [mvdan/sh][shfmt] for the latest information.

- macOS Users:
    - If your shell does not have `PATH` to `shfmt`, you need to specify `shfmt_bin_path`.
- Linux and Windows Users:
    - You need to specify `shfmt_bin_path`.

```javascript
"shfmt_bin_path": "Absolute Path to shfmt"
```


# Commands

**Command** is the name of the command you can use for **Key-Bindings**.

| Caption                            | Command                         | Default Key Bindings   |
| ---------------------------------- | ------------------------------- | ---------------------- |
| **Pretty Shell: Format**           | `pretty_shell`                  | (CMD / Alt) + Ctrl + S |
| **Pretty Shell: Format Selection** | `pretty_shell_selection`        | None                   |
| **Pretty Shell: Minify**           | `pretty_shell_minify`           | None                   |
| **Pretty Shell: Minify Selection** | `pretty_shell_minify_selection` | None                   |


# Settings

```javascript
/* Pretty Shell */
"shfmt_bin_path": "shfmt",
"format_on_save": true,
"format_selection_only": false,
"scroll_to_error_point": true,

/* shfmt (Leave these untouched to use shfmt's default behavior) */
"simplify": false,   // Simplify the code
"minify": false,     // Minify the code (implies "simplify")
"language": "",      // bash / posix / mksh (default: bash)
"indent": "",        // 0 for tabs
"binop": false,      // Operators such as '&&' and '|' may start a line
"switchcase": false, // Indent switch cases
"rediop": false,     // Redirect operators will be followed by a space
"align": false,      // Keep column alignment paddings
"fnbrace": false     // Place function opening braces on a separate line
```

# Acknowledgements

- [dzhibas/SublimePrettyJson][prettyjson] — Inspired by this project
- [mvdan/sh][shfmt] — Pretty Shell is powerd by shfmt, the quality formatter
- [realm/strip-frameworks.sh][realm] — Script used in the demo gif


[packagecontrol]: https://packagecontrol.io/packages/Pretty%20Shell
[shfmt]: https://github.com/mvdan/sh
[realm]: https://github.com/realm/realm-cocoa/blob/master/scripts/strip-frameworks.sh
[prettyjson]: https://github.com/dzhibas/SublimePrettyJson
