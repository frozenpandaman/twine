# Twine 1.4.3-alt

## Introduction

A visual tool for creating interactive stories for the Web, based on the [Twee](https://github.com/tweecode/twee) story engine.

See [https://twinery.org/](https://twinery.org/) for more.

## Development environment setup

These are specific setup instructions for my MacBook Pro, running Mac OS X 10.11 (El Capitan). The original readme and setup instructions can be found at [https://github.com/tweecode/twine](https://github.com/tweecode/twine).

Notes:
 - The most recent version of py2app (0.14) is fine; we don't need 0.6.4 specifically.
 - We're not using virtualenv.
 - Removed Windows stuff like the py2exe dependency and `buildexe.py`.
 - I've added the SugarCube-2 story format into `templates/`. The original download page can be found [here](https://www.motoslave.net/sugarcube/2/#downloads).

1. Setup:
   ```
   git clone https://github.com/frozenpandaman/twine.git
   pip install py2app
   cd twine/
   ```

2. Follow [these instructions](http://davixx.fr/blog/2016/01/25/wxpython-on-os-x-el-capitan/) ([mirror](https://web.archive.org/web/20170926104627/http://davixx.fr/blog/2016/01/25/wxpython-on-os-x-el-capitan/)) to install wxPython 3.0.2.0 on OS X 10.11 (there's a bug with the .pkg installer). 

3. Run `python app.py` to launch. Build with `python buildapp.py py2app`.

4. Make sure to add [fixes for bugs](https://twinery.org/wiki/twine_1.4.2_bugs) in projects you create.