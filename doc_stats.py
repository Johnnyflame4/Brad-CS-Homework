"""
Homework 07: Document Statistics
===========================
Course:   CS 5001

PROVIDED CODE - no need to edit. If you are having import errors (may depend on IDE you use)
you can edit import statements to be relative to the src directory. For example, if you are
getting an error on the line:
from doc_stats_builder import get_number_lines, get_number_words, get_sentence_palindromes, get_vowel_count, get_word_palindromes
you can change it to:
from .doc_stats_builder import get_number_lines, get_number_words, get_sentence_palindromes, get_vowel_count, get_word_palindromes

Small program that builds document statistics from a command line input.
"""
from doc_stats_builder import (
    get_number_lines,
    get_number_words,
    get_sentence_palindromes,
    get_vowel_count,
    get_word_palindromes,
)
from doc_view import get_input, print_stats


def main() -> None:
    """
    Main function for the program.
    """
    input_data = get_input()
    stats_block = (
        get_number_lines(input_data),
        get_number_words(input_data),
        get_vowel_count(input_data),
        get_word_palindromes(input_data),
        get_sentence_palindromes(input_data),
    )
    print_stats(stats_block)


if __name__ == "__main__":
    main()
