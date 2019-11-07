# Information-Retrieval-System
A project that will attend to an information need.

## Project Structure
| Directory | File | Purpose |
| ----------|:-------------|:-----|
|  Indices  | header-document.index | Index to keep track of headers in documents |
|  Indices  | ngram-term.index | Index of terms with corresponding n-grams |
| Indices | term-document.index | Index of terms with corresponding document postings |
| Indices | term-occurence-document.index | Index of terms with the number of occurences by document |
|raw_text | * | Contains a file holding the results for each Wikipedia search |
|src|config.py| Script that contains configurations, paths, value dictionaries|
|src|count.py| Script that deterines term-document frequency|
|src|create_collections.py| Script that asks for user input and returns Wikipedia results|
|src|index_collections.py| Script that parses raw text to produce various indices|
|src|main.py| Script that contains the entry point into the program|
|src|normalize.py| Script that removes whitespace, punctuation and other non-alphabetic characters from text|
|src|search.py| Script that performs the searches on the documents|
|src|sort.py| Script that sorts the terms prior to indexing|
|src|spelling.py| Script that performs spelling correction|
|src|tokenize.py| Script that breaks documents into smaller tokens for parsing|
