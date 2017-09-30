# Twine 1.4.3-alt

## Introduction

A visual tool for creating interactive stories for the Web, based on the [Twee](https://github.com/tweecode/twee) story engine. See [https://twinery.org/](https://twinery.org/) for more.

## Changes from Twine 1.4.2

 * Update to wxPython Phoenix (4.0) for easier installation
   * Using Unicode instead of ASCII
 * Save and restore window size on save/open
 * Fix file opening & closing
   * Program stays open even with zero stories open
 * Macro auto-insertion via Story menu
 * Add option to allow passage (widget) overlapping
 * Fix size of annotation passages; add note passages
 * Test play from seleted passage with Cmd-T across story formats
   * If invalid (e.g. stylesheet, special passage), plays from Start
 * Fix 1.4.2 [bugs](https://twinery.org/wiki/twine_1.4.2_bugs) #1, 3, 5, 7, and 8
 * Use smaller toolbar icons
 * Use Flat Design(TM) mode by default; update dock icon
 * Include [SugarCube](https://www.motoslave.net/sugarcube/2/#downloads) story format

 ## Issues / improvements

 - [ ] Recent file menu broken (segfault – disabled for now)
 - [ ] Error about opening stories on launch (supressed for now)
 - [ ] Cannot import images over https
 - [ ] Exported .rtf is unreadable
 - [ ] To add: Emoji support (?)
 - [ ] To add: Open compiled HTML file from web URL

## Development environment setup

These are specific setup instructions for my MacBook Pro, running Mac OS X 10.11 (El Capitan). The original readme and setup instructions can be found at [https://github.com/tweecode/twine](https://github.com/tweecode/twine).

Notes:
 - The most recent version of py2app (0.14) is fine; we don't need 0.6.4 specifically.
 - We're not using virtualenv (as the original repo's instructions do).
 - Removed Windows stuff like the py2exe dependency and `buildexe.py` (might restore later).
 - Moved `requirements.txt` packages into steps below.

1. Install [Python 2.7](https://www.python.org/downloads/) and run:
   ```
   git clone https://github.com/frozenpandaman/twine.git
   pip install py2app
   pip install wxpython
   cd twine/
   ```

2. Run `python app.py` to launch. Build (to the `dist/` folder) with `python buildapp.py py2app`.

Something behaving weird or not working as it should (probably because you have both Twine 1.4.2 and 1.4.3-alt installed)? Try deleting the file `~/Library/Preferences/Twine Preferences`.

## Contact

[@frozenpandaman](https://twitter.com/frozenpandaman) on Twitter