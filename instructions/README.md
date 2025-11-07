# Homework 09 - Dictionaries

For this assignment you will explore reading in file data for *large* files, and then adding unique data to a dictionary counting various entries.

## Provided Files

The following files have been provided for you.

* [flight_counter.py](../src/flight_counter.py) - This is the main file you will be working on. It contains the functions you will be writing, along with already built docstrings.
* [airlines.dat](../data/airlines.dat) - This file contains 14 different airlines, in the format of CODE::NAME.
* [flights.dat](../data/flights.dat) - This is a very large file of flights from 2015. It contains 1,048,574 different flights!
* [flights10.dat](../data/flights10.dat) - This a much smaller file of flights from 2015. It contains 10 different flights. It was built by running the following command in linux/mac: `shuf -n 10 flights.dat > flights10.dat`. The `shuf` command randomly samples lines from a file.
* [flights100.dat](../data/flights100.dat) - This is another file you can use for testing counting your flights.(it contains 100 different flights)
* [Tests](../tests/) - Contains default unit tests and files to help with testing. You will add to this directory.

### flight_counter.py

Take a moment to look through flight counter, and evaluate what the provided code does. In its current state, you can run it from the command line, but it doesn't do much. However, we encourage you to do that, and add the -h program argument to see what it does.

```console
$ python3 flight_counter.py -h
```

(on windows, you can run `python flight_counter.py -h`). Note: this example assumes you are in the same directory (`src`) as your file.

:fire: **TASK** - Run the program with the `-h` argument, and copy the output into your Report.md file. In your own words, explain what it is showing you.

> [!NOTE]
> `argparse` is a python library that allows you to easily create command line interfaces. It is very useful for creating programs that can be run from the command line, and we wanted to provide an example of what it does in this assignment.  You do not have to know in full detail how to use `argparse`, but if you dive more into python development beyond this course it is a valuable tool to know.

## Required Functions

:fire: **TASK** - Implement the following functions in flight_counter.py.

You will implement the following functions in flight_counter.py.

* `load_airlines(filename)` - This function will load the airlines.dat file into a dictionary. The key will be the airline code, and the value will be the airline name.
* `build_counters(filename, airlines)` - This function will build a dictionary of counters for each airline. The key will be the airline code, and the value will be the number of flights for that airline.
* `print_flight_info(airlines, counters)` - This function will print out the flight information for each airline. It will print out the the airline name and the number of flights for that airline.

Here is an example of the printed output:

```text
Delta Air Lines Inc.:                1
US Airways Inc.:                     2
Atlantic Southeast Airlines:         1
Southwest Airlines Co.:              2
```

or with the full dataset (but half the airlines)

```text
Alaska Airlines Inc.:           29,614
American Airlines Inc.:         97,549
US Airways Inc.:                73,942
Delta Air Lines Inc.:          147,486
Spirit Air Lines:               19,612
United Air Lines Inc.:          87,606
Hawaiian Airlines Inc.:         14,133
```

Here are some specific constraints:

* When loading the flight information, if the airline code is not in the airlines dictionary, you should skip that flight.
* Flights always start with the two digit airline code which is then followed by an id number.
  * Example: **DL**1668 is for **Delta Airlines** flight number 1668
* Both `load_airlines` and `build_counters` will be reading in from the provided .dat files, and building the required dictionaries *as the file is being read*.

> [!IMPORTANT]
>
> don't try to load the entire file first, and then build - because the 1,000,000+ lines would waste a lot of memory doing that
* You will need to use string format to print the flight information. The Airlines name should be *30* characters wide, and the number of flights should be *7* characters wide, with a space between them. The comma is often the hardest thing to make sure it is included. See below for some hints on how to do this.

### test_flight_counter.py
👉🏽 **TASK** - Run doctests with the `-v` option. You will copy this output into the report.md. However, you will also notice that doctests may not make as much sense for this project, as they are dependant on files (I still included them as examples).

When writing tests for files, it is important to build "unit tests" that work
with designated input files and output files. That way whenever you run the tests,
you can regenerate the actual results. This is a skill you will develop more
in CS 5004, but we would like you to try it a bit with this assignment (it will also
help with the final project giving you more options to test)

In [tests/test_flight_counter.py](../tests/test_flight_counter.py) we have
provided a few example unit tests. Take a look through them, and
make sure you understand what is going on. You will notice for most the tests
we created a **SMALLER** file. This is to ensure that you can manually check to make
sure the output is exactly what the test expects! Otherwise, it would be too large
to use the full flights.dat and actually know if you are correct!

> [!IMPORTANT]
> Generating test files that are smaller in nature, but easier to define
> the expected results is up to the programmer doing the testing! It is good
> to practice this skill, as it causes you to really think through expected
> input (files) and output based on those files.

:fire: **TASK**: You should write *at least* one additional unit test for `build_airlines` and `build_counters`. For each test, you should generate your own test files (add them to the tests folder). Make sure you follow the format of the test. As an example, we will talk through one of the provided tests below.

```python
   def test_build_airlines(self) -> None:  # notice method starts with the word test, and starts indented!
        """Test build airlines with a smaller airlines file""" # docstring
        airlines = flight_counter.load_airlines("airlines_3.dat") # calls the function to test
        self.assertEqual(   # assertsEquals is saying, compare these two values as equals
            airlines,       # actual value from the function
            {               # expected / correct answer
                "AS": "Alaska Airlines Inc.",
                "US": "US Airways Inc.",
                "UA": "United Air Lines Inc.",
            },
        )
```

The above test function is a very specific format in that it's name starts with `test` (as does the file). The important line in there is `self.assertEqual(val1, val2)` this compares two values
returning if they are equal. It can be any value, but should be the same type. In the case above since `load_airlines` returns a dictionary we make sure the 'expected' value is a dictionary.

Another way to word the above test would be.

```python
   def test_build_airlines(self) -> None:
        """Test build airlines with a smaller airlines file"""
        actual = flight_counter.load_airlines("airlines_3.dat")
        expected =  {
                "AS": "Alaska Airlines Inc.",
                "US": "US Airways Inc.",
                "UA": "United Air Lines Inc.",
            }
        self.assertEqual(actual, expected)
```

If the assert fails, it throws an exception with the unittest runner will report
as an error. Detailed unit testing can look for exceptions, true/false statements,
and more!  However, we just want you to start thinking about unit tests for this
assignment so you need at least two, but we highly recommend more.

> [!IMPORTANT]
> For the two unit tests you write, remember to create test .dat files!

> [!NOTE]
> You can also look at the larger program run. What that does is
> run the program and captures the output into a string, that can then be
> tested. You may consider using one of the smaller flights file to figure out
> a program run.

The autograder will have a variety of tests and files similar to the ones you create. I also encourage you to think about edge cases (e.g. what happens if files have spaces, or empty files, etc).

---

Start early, and ask questions!

## Report.md and README.md

:fire: **Task**: Answer the questions in the [Report.md](../Report.md) and [README.md](../README.md) files.

As always you are free to ask about the questions in MS Teams, including clarifications on the code.

## Coding Practice

Looking at the coding [practice problems](https://github.com/CS5001-khoury/Resources/blob/main/PracticeProblems.md) in the class resources, you should ideally do a few
others on your own to get more practice coding.  However, you need to submit at least ONE (1)
completed practice as its own python file (which means even if the coding practice had an online
form to fill out like codingbat, you need to copy your solution to a python file).

## 🤖 Use of LLMs
You should **not** use LLMs for writing your code. This is about learning the process, and without learning the process you may find it actually more difficult to generate code with LLMs. This is because the prompts for LLMs need to be exact, or they will make faulty assumptions about the code you are trying to generate (often generating incorrect test cases!). 

You are free to use LLMs to help you think of edge cases  **after** you have a working function. An example prompt could be:

> Please evaluate the following function focusing on these specific areas:
>
> 1. **Code correctness**: Does the implementation match the docstring description?
> 2. **Docstring completeness**: Are the parameters, return value, and examples clear and accurate?
> 3. **Edge cases**: What boundary conditions or unusual inputs could cause issues?
>
> Note that for this function, I am specifically required to use recursion. 
> 
> For any edge cases you identify:
> - Explain why they're problematic
> - Show what would happen with specific input examples
> - Suggest how to handle them (documentation or code changes)
>
> Focus your feedback on the most important issues first. Assume this is for a beginner programming course.
>
> [then paste in the single function you are looking at]

For this one, we are also going to help you generate unit tests. Here is a sample prompt that can help with unit tests. Note with most LLMs, you can copy and drag the files into the prompt area. 

**Unit Test Generation and Enhancement Prompt**
> I have a Python file with functions that I need to test more thoroughly. I'm providing you with the original code file and an existing test file that may have some tests already written. I need you to analyze the current test coverage and create a comprehensive, improved test file.
>
> **Files I'm providing:** 
> - **Main code file**: [filename.py] - Contains the functions that need testing
> - **Current test file**: [test_filename.py] - May have some existing tests or be mostly empty
> - **Data files** (if applicable): [data_file.dat] and [sample.dat] - Sample data that the functions might work with
>
> **What I need you to do:**
>
> 1. **Analyze the existing tests**: Review what's already covered and identify gaps in test coverage
>
> 2. **Create comprehensive unit tests** that include:
>    - **Happy path tests**: Normal, expected inputs and outputs
>    - **Edge case tests**: Empty inputs, boundary values, maximum/minimum values
>    - **Error handling tests**: Invalid inputs, wrong data types, missing files
>    - **Data validation tests**: If functions work with the provided data files, test various scenarios
>    - **Integration tests**: If functions work together, test their interactions
>
> 3. **Follow testing best practices**:
>    - Use descriptive test method names that explain what is being tested
>    - Include clear assertions with helpful error messages
>    - Set up proper test data and teardown if needed
>    - Group related tests logically
>    - Use appropriate the unittest testing frameworks
>
> **For each test you create, please:**
> - Add a brief comment explaining what the test is checking
> - Ensure tests are independent and can run in any order
> - Make sure test data doesn't interfere between tests
> - Include both positive and negative test cases
>
> **Output format:**
> - Provide the complete, updated test file
> - Include a brief summary of what new tests you added and why
> - Point out any functions that might be difficult to test and suggest improvements
> - Note any assumptions you made about expected behavior
>
> My goal is to have a robust test suite that gives me confidence in my code and helps me catch bugs early. Help me understand good testing practices through your examples.

You may actually find using the LLM will be more work than just writing additional tests. However, it is worth looking at both approaches. 

> [!CAUTION]
> LLMs are notorious about having invalid tests. The code is right, but the expected
> output is often wrong. You will want to validate all lines of code with your 
> own understanding of the files!

## 📝 Grading Rubric

1. Learning (AG)
   * `load_airlines` works correctly with a small airlines file
   * `load_airlines` works correctly with a larger sized file
2. Approaching  (AG)
   * Build counters works correctly with a small airlines file
   * Build counters works correct with medium sized files
   * Prints out flight info for a small data set, spacing is not counted, no commas
   * Prints out flight info for a large dataset including commas correct
   * Passes standard pycodestyle check
3. Meets  (MG)
   * Code has comments, well written, and easy to read
   * Report.md questions answered
   * Student answers questions in the README.md file
   * Added Coding Practice Problem
4. Exceeds  (MG)
   * Student provides additional tests in `tests_flight_counter.py`, along with any `test.dat` files they made.
   * Deeper Thinking question answered



AG - Auto-graded
MG - Manually graded


### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.


## 📚 Additional Resources
* [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
* [Python File Reading](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [Format String Syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
* [argparse](https://docs.python.org/3/library/argparse.html) - Python library for creating command line interfaces
* [Kaggle - Explore: Flights](https://www.kaggle.com/code/miquar/explore-flights-csv-airports-csv-airlines-csv/notebook) - This is a notebook that uses the flights dataset to explore flights. It provided the basis for the .dat files we provided.
* [Python Unit Testing Tutorial](https://realpython.com/python-unittest/) - Detailed tutorial on unit testing.

### String Formatting for Numbers

If you want to format a number to have commas, you can use the following code:

```python
>>> num = 123456789
>>> print(f'{num:,}')
123,456,789
```

If you want to have a number that is 12 characters wide, and right justified, you can use the following code:

```python
>>> num = 123456789
>>> print(f'|{num:12,}|')
|   123,456,789|
```

### String Padding to the Right

If you want to pad a string to the right, you can use the following code:

```python
>>> name = "Delta Air Lines Inc."
>>> print(f'|{name:30}|')
|Delta Air Lines Inc.         |
```

But what if you wanted to add an extra character? Then make sure to modify `name` *before* using the string formatting.  The bars are added just so you can see the spaces easier.

### Combining String Formatting and Padding

```python
>>> name = "Delta Air Lines Inc."
>>> num = 123456789
>>> print(f'|{name:30} {num:12,}|')
|Delta Air Lines Inc.         123,456,789|
```
