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
pip install -r requirements.txt

# for development
pacman -S antlr4
```

## Running

    python run.py

## Development

I used ANTLR 4 for generating my lexers and parsers. I use the following
command:

    antlr4 -Dlanguage=Python3 -visitor Types.g4


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

