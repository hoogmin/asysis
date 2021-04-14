# **Asysis**: Another system information script

Asysis is a lightweight utility program for displaying system information
to a terminal/command-line (i.e. hostname, cpu type, etc). It works on Windows, MacOS, 
GNU/Linux, and almost any other system provided it has python installed. I plan on improving
this project gradually over time as I find more features I would like to implement and bugs
to fix. I would definitely not consider this a focused sort of thing. Just something fun on the
side. In its current state, the program is functional and can be used. See "Setup" section for details.

# Setup
Asysis, in its current state, has no external dependencies. To be able to run this program on your machine you
only need the following requirements:

* A working installation of `python` (preferably python3, [2.7 is out of support](https://www.python.org/doc/sunset-python-2/)).

Yes, its as simple as that. If you are a MacOS or GNU/Linux user, then your machine already has a version
of `python` pre-installed. For Windows users, `python` can be downloaded at the [official python site](https://www.python.org/)
through an installer found under the "downloads" section of the site. Once you have `python` you only need to download the project
to your machine. This can be accomplised by using github and downloading the repo as a compressed zip file (simple way) or through
`git clone` (if you are familiar with `git`). After extracting the zip file of the project, place it anywhere you like on your
machine. Finally, when you decide you want to see your system information, `cd` into the location where you keep `asysis.py`
and run:
* `python asysis.py` (Single-installation of python)
* `python3 asysis.py` (For systems with multiple installations of python)

The above commands will remain the same on Windows, MacOS, GNU/Linux, and most other systems. That is all for the
setup. Now you can display information about your system anytime you like and in a fairly cross-platform manner. Enjoy!

# Contributing
Asysis is an open-source project. This means that its source can be viewed by anyone and is freely redistributable, modifiable, etc.
I mentioned in an earlier section that I would be gradually improving on this program based on additions and bug fixes. However, if
you are looking at this repo and would like submit a contribution/patch, then feel free to. Asysis is a really a simple program
to understand so just jump right in if you have interest. At this moment, everything is in `asysis.py`, so go there if interested
in contributing.

# Notes
At the moment, this program has no dependencies. It only uses built-in libraries.
I am not sure whether or not I will keep it this way. I wanted to keep it
as lightweight as I could to make it easy for people to just download and run the program. This of course limits what I can
do which is why I am unsure of whether I will keep it the way it is. Also, you will notice I use `.format` rather than newer
features like f-strings. This is done intentionally for backwards-compatibility purposes as older versions of python don't
support f-strings. If something changed or I am wrong about this, then feel free to let me know or even submit a patch for
the program to update this.

# License
This project is licensed under the *BSD-3-Clause* License. See `LICENSE` file for details.