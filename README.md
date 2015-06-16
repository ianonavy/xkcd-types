xkcd-types
==========

Implementation of http://xkcd.com/1537/ in Python using ANTLR

## Requirements

- Python 3
- pip
- ANTLR 4.5 (for development)

## Setup

```
git clone git@github.com:ianonavy/xkcd-types.git
cd xkcd-types
pip install -e .

# for development
pacman -S antlr4
```

## Running

    xkcdtypes

Looks like this:

![Screenshot mimicking original xkcd](http://files.ianonavy.com/YzUw.png)

And to prove it's not just printing lines and has real 'logic':

![Screenshot showing it really working](http://files.ianonavy.com/NmFl.png)

## Development

I use ANTLR 4 for generating my lexers and parsers using the following
commands:

    cd grammars
    antlr4 -Dlanguage=Python3 -visitor Types.g4 -o ../xkcd_types/gen/

## Todo

- Clean up the packaging and maybe make it pip installable for people to play
  with it. I was going to do it in JavaScript initially, but the JS runtime
  seemed incomplete (in particular, the visitor prototype was incomplete), so I
  opted for Python.
- Colors (both the 'module' from the title text and the interface).
- Come up with a cooler name.
- Readline support for history and emacs-like line editing.
- Documentation? Do we even care? I thought this was supposed to be terrible.
- Fix EOFError on Ctrl+D.

