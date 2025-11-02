"""
Homework 08: Document Statistics Program
===========================
Course:   CS 5001
Student:  Brad Wing

Update this file by adding required functions.

Small program that builds document statistics from a command line input.
"""
import sys

from doc_stats_builder import (
    get_number_lines,
    get_number_words,
    get_sentence_palindromes,
    get_vowel_count,
    get_word_palindromes,
)
from doc_view import get_input, print_stats
from doc_file_view import read_file, write_json_file

# provided functions


def get_stats_block(doc: tuple) -> tuple:
    """
    Builds a tuple of statistics from a tuple of strings.

    Args:
        doc (tuple): A tuple of strings.

    Returns:
        tuple: A tuple of statistics in the order of lines, words, vowels,
        palindromes and sentence palindromes.
    """
    return (
        get_number_lines(doc),
        get_number_words(doc),
        get_vowel_count(doc),
        get_word_palindromes(doc),
        get_sentence_palindromes(doc),
    )


def check_args_for_help(args: list) -> bool:
    """
    Checks to see if -h is in the args, if so, prints the help message and returns True.

    Args:
        args (list): A list of command line arguments.

    Returns:
        bool: True if -h is in the args, False otherwise.
    """
    if "-h" in args or "--help" in args:
        print_help()
        return True
    return False


def print_help() -> None:
    """
    Prints the help message for the program.
    """
    print(
        "Usage: python doc_stats.py [-h|--help] [-f filename]  [-o filename]")
    print("Options:")
    print("  -f filename: The name of the file to analyze.")
    print("  -h or --help: Print this help message and exit")
    print("  -o filename: The name of the file to write the output to.",
          "If filename is not provided, but -o is used then the default file",
          "name is out.txt.")

# end provided functions
# edit the following functions


def get_input_file(args: list) -> str:
    """
    Checks to see if -f file_name is in the args, if so, returns the file name,
    or returns an empty string if it is not there.

    On a bad format, such as -f (nothing) or -f followed by a -- or - (another flag),
    raises a ValueError.

    Args:
        args (list): A list of command line arguments.

    Returns:
        str: The file name if it exists in the args and is valid, otherwise an empty string.
    """
    if "-f" not in args:
        return ""

    f_index = args.index("-f")

    # Check if -f is the last argument (no filename after it)
    if f_index == len(args) - 1:
        raise ValueError("No filename provided after -f")

    filename = args[f_index + 1]

    # Check if filename starts with - (indicating it's another flag)
    if filename.startswith("-"):
        raise ValueError("Invalid filename after -f")

    return filename


def get_output_file(args: list) -> str:
    """
    Checks to see if a -o file_name is in the args, if so returns the file name or
    the empty string if it is not there.

    If -o is provided without a following file name, it uses the default 'out.txt'.

    Args:
        args (list): A list of command line arguments.

    Returns:
        str: A file name if -o is in the args, otherwise an empty string.
    """
    if "-o" not in args:
        return ""

    o_index = args.index("-o")

    # Check if -o is the last argument (no filename after it)
    if o_index == len(args) - 1:
        return "out.txt"  # Default filename

    next_arg = args[o_index + 1]

    # Check if next argument starts with - (indicating it's another flag)
    if next_arg.startswith("-"):
        return "out.txt"  # Default filename

    return next_arg


def main(args) -> None:
    """
    Main function for the program.
    """
    # Check for help first
    if check_args_for_help(args):
        return

    # Get input and output file options
    input_file = get_input_file(args)
    output_file = get_output_file(args)

    # Get the document data
    if input_file:
        # Read from file
        doc = read_file(input_file)
    else:
        # Get input from user (like Homework 07)
        doc = get_input()

    # Generate statistics
    stats = get_stats_block(doc)

    # Output the results
    if output_file:
        # Write to JSON file
        write_json_file(stats, output_file)
        print(f"Statistics written to {output_file}")
    else:
        # Print to console (like Homework 07)
        print_stats(stats)


if __name__ == "__main__":
    main(sys.argv)
