""" 
Homework 08: File "View" For the Application
===========================
Course:   CS 5001
Student:  Your Name

This file contains functions to help with manipulating files and JSON.
"""


def read_file(file_path: str) -> tuple:
    """
    Reads in a file and returns a tuple with each line as a string.
    Each line will have leading and trailing whitespace removed.
    Empty lines are removed

    Args:
        file_path (str): The path of the file to be read.

    Returns:
        tuple: A tuple with each line of the file as a string.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
    return tuple(line.strip() for line in lines if line.strip())


def write_json_file(doc_stats: tuple, file_path: str) -> None:
    """
    Writes the document statistics as a JSON string to a file.


    See:
        stats_to_json

    Args:
        doc_stats (tuple | list): the document statistics
        file_path (str): The path of the file to be written.
    """
    json_string = stats_to_json(doc_stats)
    with open(file_path, "w") as f:
        f.write(json_string)


def stats_to_json(doc_stats: tuple) -> str:
    """
    Writes the document statistics as a JSON string, format would be:
    {"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}
    with the numbers replaced with the actual values.

    Examples:
        >>> stats_to_json((1, 2, 3, 4, 5))
        '{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'
        >>> stats_to_json((0, 0, 0, 0, 0))
        '{"lines": 0, "words": 0, "vowels": 0, "palindromes": 0, "sentence_palindromes": 0}'
        >>> stats_to_json((12, 102, 33, 42, 0))
        '{"lines": 12, "words": 102, "vowels": 33, "palindromes": 42, "sentence_palindromes": 0}'

    Args:
        doc_stats (tuple | list): the document statistics

    Returns:
        str: the JSON formatted string
    """
    json_template = ('{"lines": %d, "words": %d, "vowels": %d, '
                     '"palindromes": %d, "sentence_palindromes": %d}') % doc_stats
    return json_template


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
