# Word Completion Finder — Text Search & Autocomplete Engine

A Python text-processing and autocomplete program that builds a searchable vocabulary from a text file and finds words matching user-provided prefixes.

## Overview

The program processes a source text file, normalizes valid words, removes duplicates, and builds an index based on each word's character positions. Prefix searches then use set intersections to identify matching completions.

## Features

- Reads and processes vocabulary data from text files
- Normalizes words by removing surrounding punctuation and converting text to lowercase
- Filters invalid words and short entries
- Removes duplicate vocabulary entries
- Builds a character-position index for prefix searching
- Uses set intersection to find matching completions
- Sorts and displays matching results
- Interactive command-line interface

## Search Approach

Instead of scanning every word for every prefix query, the program creates dictionary keys in the form:

```text
(position, character) -> set of matching words
```

For example, a word beginning with `cat` contributes entries for:

```text
(0, 'c')
(1, 'a')
(2, 't')
```

When a user enters a prefix, the program retrieves the sets associated with each character position and intersects them to find words satisfying all prefix constraints.

## Technical Concepts

- Python
- Dictionaries
- Sets
- Set intersection
- String processing
- File I/O
- Data normalization
- Search algorithms
- Command-line interfaces

## Project Structure

```text
Word-Completion-Finder/
├── README.md
├── .gitignore
└── src/
    └── word_completion_finder.py
```

## Running the Project

```bash
python src/word_completion_finder.py
```

The program prompts for a text file and then accepts prefixes until `#` is entered.

## Example

Given a vocabulary containing words such as:

```text
computer
complete
composition
python
program
```

A search for:

```text
com
```

returns the vocabulary entries beginning with that prefix.

## Future Improvements

- Add automated tests
- Add performance benchmarking against a linear-search implementation
- Support configurable minimum word lengths
- Improve prefix validation
- Explore trie-based indexing as an alternative implementation
