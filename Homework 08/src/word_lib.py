"""
Homework 07: Library of Word Functions, all written recursively
===========================
Course:   CS 5001
Student:  Brad Wing

Various functions to practice recursion.
"""


def is_palindrome(word: str) -> bool:
    """
    Recursively looks at a string to determine if it is a palindrome.

    Does not remove punctuation or spaces, and assumes the word is
    already in lower case.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('hello')
        False
        >>> is_palindrome("noon")
        True
        >>> is_palindrome("A")
        True
        >>> is_palindrome("")
        True
        >>> is_palindrome("ab")
        False

    Args:
        word (str): the word to check

    Returns:
        bool: True if the word is a palindrome, False otherwise
    """

    if len(word) <= 1:
        return True
    if len(word) == 2:
        return word[0] == word[-1]
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


def count_vowels(word: str) -> int:
    """
    Recursively counts the number of vowels in a string. Case
    does not matter.

    Examples:
        >>> count_vowels('hello')
        2
        >>> count_vowels('aeiou')
        5
        >>> count_vowels('AEIOU')
        5
        >>> count_vowels('a')
        1
        >>> count_vowels('')
        0

    Args:
        word (str): the word to check

    Returns:
        int: the number of vowels in the word
    """
    if len(word) == 0:
        return 0
    vowels = "aeiouAEIOU"
    if word[0] in vowels:
        return 1 + count_vowels(word[1:])
    else:
        return count_vowels(word[1:])


def clean_word(word: str) -> str:
    """
    Recursively removes punctuation from a word, and reduces it to lower case.

    Examples:
        >>> clean_word('Hello!')
        'hello'
        >>> clean_word('World...')
        'world'

    See:
        https://docs.python.org/3/library/stdtypes.html#str.isalnum


    Args:
        word (str): the word to remove punctuation from

    Returns:
        str: the word without punctuation
    """
    if len(word) == 0:
        return ""
    first_char = word[0]
    if first_char.isalnum():
        return first_char.lower() + clean_word(word[1:])
    else:
        return clean_word(word[1:])


# Just running this file will run the doctests
if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
