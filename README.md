# Sublime Pretty Shell
[shfmt](https://github.com/mvdan/sh) wrapper plugin for Sublime Text 3.


# Install
Waiting for merge...


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


# Tips
Highly recommended to use this plugin with:

- [SublimeLinter-shellcheck](https://packagecontrol.io/packages/SublimeLinter-shellcheck)
