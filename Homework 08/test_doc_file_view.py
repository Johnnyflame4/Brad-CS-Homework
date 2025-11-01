import unittest
import sys
import re
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Homework 08 ')))


import doc_file_view    # type: ignore


clean_spaces = lambda string: re.sub(r"\s+", "", string)


class TestDocFileView(unittest.TestCase):

    def test_stats_to_json(self) -> None:
        """Tests stats_to_json with various doc_stats tuples."""
        self.assertEqual(
            clean_spaces(doc_file_view.stats_to_json((1, 2, 3, 4, 5))),
            clean_spaces(
                '{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'
            ),
        )
        # add your own tests
 
    def test_write_json_to_file(self) -> None:
        """Tests write_json_file with various doc_stats tuples."""
        doc_stats = (1, 2, 3, 4, 5)
        doc_file_view.write_json_file(doc_stats, "test.json")
        with open("test.json", "r") as file:
            self.assertEqual(
                clean_spaces(file.read()),
                clean_spaces('{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'),
            )
        # add others

        #clean up
        if os.path.exists("test.json"):
            os.remove("test.json")

    def test_read_file(self) -> None:
        """Reading a typical file, with multiple lines. No blank lines or extra whitespace."""
        self.assertEqual(
            doc_file_view.read_file("data/auto_generated.txt"),
            ("Racecar drivers enjoy their fast cars, zooming past radar traps,", 
            "their racecar's red color reflecting in their", 
            "rearview mirrors. Madam, said the racecar driver,",
            "A Santa at NASA", 
            "made a radar trap a palindrome."),
        )

    # maybe test a few other files, empty files, files with spaces, etc

    


if __name__ == "__main__":
    unittest.main()
