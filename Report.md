# Report


1. What is the difference between a file and a directory?
   A file is something that holds data in a specific file type, such as .txt, .xls, .pdf, etc. 
   A directory is a place in the computer that stores files. A file path is considered the directory where the file is stored in the storage structure of the drive it is stored on. 

2. What is the difference between a relative and absolute path?
   A relative path is only part of the full file path. It usually uses dots (.) (...) to shorten the parent directory. For example it can be "... > Python > Homework 08, instead of the full file path that would include the folder structure above it going back to C drive. 
   An absolute path goes all the way back to the root. An absolute path works wherever you start from, as opposed to a relative path. For example it could be C:\Users\Brad\Documents\VS Code Projects\Python Projects\Homework 08, which is which is the full file path on my local machine. 

3. What is the difference between a text file and a binary file?
    A text file contains characters that are meant to be read by a human. These are things like .txt, .csv, etc. 
    A binary file contains 0's and 1's that are meant to be interpreted by a computer. These are things like .exe, .jpg, .pdf, etc. 

4. When looking at program arguments, which is the first argument (sys.argv[0]) in the list for all python files?
    This is always the name of the python script that is being executed. (sys.argv) is a list that contains the command line arguments passed to the python script. (sys.argv(0)) contains the script name (for example, my_script.py). 
   
5. List three python exceptions or errors, and what their purpose. For example, a ValueError represents an error when a value has the right type but inappropriate value. You can find a list here: https://docs.python.org/3/library/exceptions.html. Ideally, pick ones you have seen before! 
 
    1.. exception SyntaxError(message, details)

    Raised when the parser encounters a syntax error. This may occur in an import statement, in a call to the built-in functions compile(), exec(), or eval(), or when reading the initial script or standard input (also interactively).

    2.. exception IndentationError

    Base class for syntax errors related to incorrect indentation. This is a subclass of SyntaxError.

    3.. exception TypeError

    Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.

    This exception may be raised by user code to indicate that an attempted operation on an object is not supported, and is not meant to be. If an object is meant to support a given operation but has not yet provided an implementation, NotImplementedError is the proper exception to raise.

    Passing arguments of the wrong type (e.g. passing a list when an int is expected) should result in a TypeError, but passing arguments with the wrong value (e.g. a number outside expected boundaries) should result in a ValueError.


## Deeper Thinking

In this assignment, your capability to analyze and represent data greatly increased
because you are now able to handle files. Files hold the "state" of information (data)
in a computer, and because of them, we can save our state and return to a certain state between computer runs. 

However, for file types to make sense, there needs to be specifications. A specification
is an agreed upon format for how to represent data. For example, the .csv file format
is a specification for how to represent data in a comma separated value file. Many groups are formed to create specifications, and they are often open source. One  well known one is the [W3C](https://www.w3.org/), which creates specifications for the web with the [HTML](https://html.spec.whatwg.org/) standard being the most well known.

Task: Write a three short paragraphs about how you think specifications are created, and why they are important. You can use the W3C and HTML as an example, or any other specification you find interesting. If you look at HTML bonus if you create small webpage in HTML to show off your knowledge! (You can upload the .html repo with your submission)

Response:

Specifications are created through collaboration between experts, organizations, and community members who share a common goal of establishing consistent ways to represent or process information. Typically, a group such as the W3C (World Wide Web Consortium) will form working groups made up of engineers, developers, and stakeholders who propose ideas, discuss challenges, and refine drafts over time. These drafts are reviewed publicly, allowing others in the industry to provide feedback before they become official recommendations or standards. This open and iterative process helps ensure that specifications are both technically sound and widely accepted.

Specifications are important because they enable compatibility, consistency, and communication between systems. Without them, every developer or company might represent data differently, leading to confusion and incompatibility. For example, the HTML specification defines how web browsers should interpret and display web pages, ensuring that a website looks and behaves similarly across Chrome, Firefox, Safari, and other browsers. Specifications also make it possible for different technologies to work together, like how CSS and JavaScript integrate seamlessly with HTML due to shared standards.

A great example of this in action is the HTML specification, which provides a common language for structuring web content. Below is a simple HTML webpage that follows W3C standards. It demonstrates how specifications help developers create universally understood web content:

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Specification Example</title>
</head>
<body>
  <h1>Understanding Specifications</h1>
  <p>Specifications like HTML ensure that web pages display consistently across all browsers and devices.</p>
  <p>Thanks to groups like the W3C, the web remains open, accessible, and standardized for everyone.</p>
</body>
</html>
