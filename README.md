# Twine 1.4.3-alt

## Introduction

A visual tool for creating interactive stories for the Web, based on the [Twee](https://github.com/tweecode/twee) story engine. See [https://twinery.org/](https://twinery.org/) for more.

## Changes from Twine 1.4.2

 * Fix file opening & closing
 * Allow passages to overlap (messy)
 * Fix *some* 1.4.2 [bugs](https://twinery.org/wiki/twine_1.4.2_bugs) (already in repo upon fork)
 * Collapse toolbar
 * Fix size of annotation/note passages
 * Include [SugarCube](https://www.motoslave.net/sugarcube/2/#downloads) story format

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
   cd twine/
   ```

2. Follow [these instructions](http://davixx.fr/blog/2016/01/25/wxpython-on-os-x-el-capitan/) ([mirror](https://web.archive.org/web/20170926104627/http://davixx.fr/blog/2016/01/25/wxpython-on-os-x-el-capitan/)) to install wxPython 3.0.2.0 on OS X 10.11 (there's a bug with the .pkg installer). 

3. Run `python app.py` to launch. Build with `python buildapp.py py2app`.

## Contact

[@frozenpandaman](https://twitter.com/frozenpandaman) on Twitter