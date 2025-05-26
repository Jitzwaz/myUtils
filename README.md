# myUtils

Just some simple utility functions I made to make life a bit easier.

**Current version:** 1.1.6

## Features (functions)

- `calcTime(func, *args)`:  
  Calculates the time it takes to execute a function, with or without arguments.

- `newline(lines=1)`:  
  Prints a newline (or multiple). Mostly here so I can just call `newline()` — because I'm lazy.

- `debugPrint(debug, *args)`:  
  Prints any given arguments if `debug` is `True`. Quick way to toggle debug/test output.

- `displayDictionary(d)`:  
  Displays a dictionary line-by-line so it looks cleaner and more readable.

- `invertDictionary(d, debugMode)`:  
  Inverts a dictionary. If a value isn’t hashable, logs the error. Debug mode prints errors and returns them.

- `displayList(l)`:  
  Same idea as `displayDictionary`, but for lists instead.
  
- `getPackageVersion(packageName, username`
  Gets the version of a package from github, useful as a helper function for `updatePackage`

- `updatePackage(packageName, username)`
  Updates the specified package from github. **WARNING:** Does not do any version checking on it's own. You'll have to use `getPackageVersion` for that.
