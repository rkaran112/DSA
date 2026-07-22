# DSA

Personal practice repository for data structures and algorithms problems, written in Python.

## What's here

- `array/` — array fundamentals and algorithm practice:
  - `array_basics.py` — manual insertion/deletion at the beginning, middle, and end of an array; element removal by value
  - `neetcode_array.py` — classic array problems (duplicate detection, finding largest/second-largest element, array rotation), loosely following NeetCode-style problem sets
  - `sortingArray.py` — sorting algorithms (bubble sort, insertion sort)
- `String/String_basic.py` — string fundamentals (length, character search, substring match, palindrome check, anagram check)
- `slidingWindow.py` — sliding window technique: fixed-size window max sum, and max profit (best time to buy/sell stock)

## Tech stack

Python 3, standard library only. No external dependencies, build steps, or tests.

## Running

Each file is a standalone script. Run any one directly, e.g.:

```bash
python array/neetcode_array.py
```

Most files call their own functions at the bottom of the file and print results, so output can be inspected by running the script.

## Status

Work in progress — this is an active practice/learning repo, not a finished library. Specifically:

- No automated tests or error handling; scripts are meant to be run and read manually

If you're browsing this for reference, treat it as in-progress scratch work rather than production-quality solutions.
