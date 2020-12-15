# [![](https://adventofcode.com/favicon.png)![aoc text](assets/aoc_text.png)](https://adventofcode.com/)

--------------------------------------------------------------------------------
![Python](https://github.com/amrit110/aoc/workflows/Python/badge.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Template solution
To quickstart or bootstrap a solution script in python, (and optionally in C++ using `--cpp` flag)

```bash
./bootstrap.py -y <year> -d <day>
```

That creates a folder `<year>/<day>` and copies `template.py`. It also 
has functionality to use the [aocd package](https://github.com/wimglenn/advent-of-code-data)
to fetch input for the given day. To use it, export your session ID:

```bash
export AOC_SESSION=<session_id>
```

### Retrieving session id
It's stored in a cookie on your machine <img src="https://pbs.twimg.com/profile_images/1092451626781163523/0YzJMi-8.jpg" height="30px"/>
