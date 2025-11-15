"""
Homework 07: Document Statistics Builder
===========================
Course:   CS 5001
Student:  Brad Wing

Functions for reading document stats. They all assume a 'document' is
a tuple or list of strings, where each string is a line of the document.

For example:
    ('Hello', 'World') is the document
    Hello
    World


    ('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho')
    An old silent pond...
    A frog jumps into the pond—
    Splash! Silence again.
    - Matsuo Basho

"""

from word_lib import clean_word, count_vowels, is_palindrome


def get_number_lines(lines: tuple) -> int:
    """
    Gets the number of lines in the document.

    Examples:
        >>> get_number_lines(('Hello', 'World'))
        2
        >>> get_number_lines(())
        0
        >>> get_number_lines(('Single line',))
        1
        >>> get_number_lines(('Line 1', 'Line 2', 'Line 3', 'Line 4'))
        4
        >>> get_number_lines(('', '', ''))
        3

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of lines in the document
    """
    return len(lines)


def get_number_words(lines: tuple) -> int:
    """
    Gets the number of words in the document.
    Note, make sure to clean the words before counting them,
    and an 'empty' word should not be counted.

    Examples:
        >>> get_number_words(('Hello', 'World'))
        2
        >>> get_number_words(('Aloha!', '-', 'World'))
        2
        >>> get_number_words(())
        0
        >>> get_number_words(('',))
        0
        >>> get_number_words(('!!!', '---', '...'))
        0
        >>> get_number_words(('One two three', 'Four five'))
        5
        >>> get_number_words(('Hello!', 'World...', '!!!'))
        2
        >>> get_number_words(('The quick brown fox', 'jumps over the lazy dog'))
        8

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of words in the document
    """
    count = 0
    for line in lines:
        words = line.split()
        for word in words:
            cleaned_word = clean_word(word)
            if cleaned_word:
                count += 1
    return count


def get_vowel_count(lines: tuple) -> int:
    """
    Gets the number of vowels in the document.

    Examples:
        >>> get_vowel_count(('Hello', 'World'))
        3
        >>> get_vowel_count(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        24
        >>> get_vowel_count(())
        0
        >>> get_vowel_count(('',))
        0
        >>> get_vowel_count(('aeiou',))
        5
        >>> get_vowel_count(('AEIOU',))
        5
        >>> get_vowel_count(('bcdfg',))
        0
        >>> get_vowel_count(('Python programming',))
        5
        >>> get_vowel_count(('!!!', '...'))
        0

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of vowels in the document
    """
    count = 0
    for line in lines:
        words = line.split()
        for word in words:
            cleaned_word = clean_word(word)
            count += count_vowels(cleaned_word)
    return count


def get_word_palindromes(lines: tuple) -> int:
    """
    Gets the number of palindromes in the document. Ignores punctuation.

    Examples:
        >>> get_word_palindromes(('Hello', 'World'))
        0
        >>> get_word_palindromes(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        1
        >>> get_word_palindromes(('raceCar', 'kayak!', 'sator arepo tenet opera rotas!'))
        3
        >>> get_word_palindromes(())
        0
        >>> get_word_palindromes(('',))
        0
        >>> get_word_palindromes(('mom', 'dad', 'sister'))
        2
        >>> get_word_palindromes(('noon', 'level', 'radar', 'civic'))
        4
        >>> get_word_palindromes(('Was it a car or a cat I saw',))
        1
        >>> get_word_palindromes(('racecar!!!', '...level...', 'RADAR'))
        3

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of palindromes in the document
    """
    count = 0
    for line in lines:
        words = line.split()
        for word in words:
            cleaned_word = clean_word(word)
            if cleaned_word and is_palindrome(cleaned_word):
                count += 1
    return count


def get_sentence_palindromes(lines: tuple) -> int:
    """
    Gets the number of palindromes in the document. Ignores punctuation.

    Examples:
        >>> get_sentence_palindromes(('Hello', 'World'))
        0
        >>> get_sentence_palindromes(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        0
        >>> get_sentence_palindromes(('A raceCar', 'A kayak!', 'sator arepo tenet opera rotas!'))
        1
        >>> get_sentence_palindromes(())
        0
        >>> get_sentence_palindromes(('',))
        0
        >>> get_sentence_palindromes(('racecar', 'madam', 'civic'))
        3
        >>> get_sentence_palindromes(('aba', 'level', 'noon'))
        3
        >>> get_sentence_palindromes(('Hello world', 'Not a palindrome'))
        0
        >>> get_sentence_palindromes(('a', 'i', 'mom', 'dad'))
        4
        >>> get_sentence_palindromes(('Never odd or even!', 'Not a palindrome', 'Was it a rat I saw?'))
        2

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of palindromes in the document
    """
    count = 0
    for line in lines:
        cleaned_line = clean_word(line)
        if cleaned_line and is_palindrome(cleaned_line):
            count += 1
    return count


# just running the file will automatically run doctest
if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
