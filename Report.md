# Report 

Brad Wing
Fall 2025

1. When you fail to add a base case in recursion, you will return a error value (crashing your program). What is the error value? If you don't know, try running the following code...
```python
def factorial(n):
    return n * factorial(n-1)
```
The error you receive is: RecursionError: maximum recursion depth exceeded. This is likely similar to a nevernding loop that was not given a return statement.

2. Describe a base case in your own words. What is the base case needed for the code above?
A base case is a value of the function where we know it is true. This is done by calculating the lowest case that isd trivial to solve and calculate where we know it is true. It acts as our anchor and lets the recursion know where to end, similar to a break in a loop. 

The base case missing for the above code is:
if n == 0 or n == 1:
    return 1

3. Thinking about for-in loops, they all work on sequential data, so based on that, what is each "item" for each of these sequential data types. Separate each item by a comma after the => symbol. 
    * Example: range(1, 3) => 1, 2
    * ('aloha', 'world') => 'aloha', 'world'
    * ['aloha', 'world'] => 'aloha', 'world'
    * 'aloha world' => 'a', 'l', 'o', 'h', 'a', ' ', 'w', 'o', 'r', 'l', 'd'

4. For this for-in loop, write an equivalent while loop. 
```python
for i in range(1, 10, 2):
    print(i)
```
```python
# your code here
i = 1
while i < 10:
    print(i)
    i += 2
```


## Deeper Thinking

The fibonacci sequence is a very famous sequence found in nature. It is defined as the sum of the previous two numbers in the sequence. The first two numbers are 0 and 1. So the sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc. If you do a quick search online, you will find that it can be written both recursively and iteratively.

For this deeper thinking, you will work on an experiment. Write a recursive fibonacci function and an iterative fibonacci function. Then, time how long it takes to run each function for the first 30 fibonacci numbers. You can use the following code to time your functions. 


```python

import time

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def time_function(func, *args):
  # Get the start time
  start = time.time()
  # Call the function with the given arguments
  result = func(*args)
  # Get the end time
  end = time.time()
  # Calculate the elapsed time
  elapsed = end - start
  # Return the result and the elapsed time
  return result, elapsed

def main():

    print("Fibonacci(10) =", time_function(fibonacci_iterative, 10))
    print("Fibonacci(20) =", time_function(fibonacci_iterative, 20))
    print("Fibonacci(30) =", time_function(fibonacci_iterative, 30))

    print("Fibonacci(10) =", time_function(fibonacci_recursive, 10))
    print("Fibonacci(20) =", time_function(fibonacci_recursive, 20))
    print("Fibonacci(30) =", time_function(fibonacci_recursive, 30))

if __name__ == "__main__":
    main()

```

Report on your results here:

Fibonacci(10) = (55, 2.6226043701171875e-06)
Fibonacci(20) = (6765, 3.337860107421875e-06)
Fibonacci(30) = (832040, 2.86102294921875e-06)
Fibonacci(10) = (55, 8.821487426757812e-06)
Fibonacci(20) = (6765, 0.0007622241973876953)
Fibonacci(30) = (832040, 0.08736371994018555)

Which one takes longer? Why do you think that is? 

The recursive function takes 29,000 times longer at a value of 30 compared to the iterative function. That is because the iterative function is calculated from the ground up and run only once. The recursive function is calculated from the top down and goes through a exponentially larger set of function calls with each larger value passed through the function. 