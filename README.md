# Insert Timestamp

Sublime Text 3 Plugin to insert an ISO 8601 timestamp

## Usage

Press

	`super+shift+t` (OSX)
	`ctrl+shift+t` (Linux, Windows)

to insert an ISO 8601 formatted timestamp such as

	`2017-02-18T12:38:48+0100`

at cursor(s)/selection(s).

You can also define your own formats by passing a `strftime` [format string](https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior) as `fmt` to the `insert_timestamp` command. Just define a new User keybinding in `Preferences > Key Bindings`:

    {
        "keys": ["super+alt+shift+t"], "command": "insert_timestamp", "args": { "fmt": "%c" }
    }
