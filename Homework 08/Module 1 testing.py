def print_even(number: int):
    """Name: print_even
    Arguments: number
    returns: Even numbers
    
    Example intake number of 8 and this function will only print the even numbers from 8-0
    
    >>> 8
        0, 2, 4, 6, 8
    
        Edge cases: Testing numbers at the edges of the bounds we define. (0) (10)
    >>> 0
        0
    >>> 7
        0, 2, 4, 6
    
    """


    even_print = 0
    while even_print <= number:
        print(even_print)
        even_print += 2


print_even(23)

