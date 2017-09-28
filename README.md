# Twine 1.4.3-alt

## Introduction

A visual tool for creating interactive stories for the Web, based on the [Twee](https://github.com/tweecode/twee) story engine. See [https://twinery.org/](https://twinery.org/) for more.

## Changes from Twine 1.4.2

 * Update to wxPython Phoenix (4.0) for easier installation
   * Use Unicode instead of ASCII
 * Fix file opening & closing
 * Allow passages to overlap
 * Fix size of annotation passages; add note passages
 * Fix *some* 1.4.2 [bugs](https://twinery.org/wiki/twine_1.4.2_bugs) (already in repo upon fork)
 * Shrink toolbar
 * Use Flat Design(TM) mode by default
 * Include [SugarCube](https://www.motoslave.net/sugarcube/2/#downloads) story format

 ## Issues / improvements

 - [ ] Recent file menu broken (segfault – disabled for now)
 - [ ] Error about opening stories on launch (supressed for now)
 - [ ] Cannot import images over https
 - [ ] Exported .rtf is unreadable
 - [ ] Emoji support (?)

## Development environment setup

These are specific setup instructions for my MacBook Pro, running Mac OS X 10.11 (El Capitan). The original readme and setup instructions can be found at [https://github.com/tweecode/twine](https://github.com/tweecode/twine).

Notes:
 - The most recent version of py2app (0.14) is fine; we don't need 0.6.4 specifically.
 - We're not using virtualenv (as the original repo's instructions do).
 - Removed Windows stuff like the py2exe dependency and `buildexe.py`.

1. Setup:
   ```
   git clone https://github.com/frozenpandaman/twine.git
   pip install py2app
   brew install wxpython
   cd twine/
   ```

2. Run `python app.py` to launch. Build with `python buildapp.py py2app`.

## Contact

[@frozenpandaman](https://twitter.com/frozenpandaman) on Twitter