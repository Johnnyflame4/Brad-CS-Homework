def sum_of_numbers(n: int) -> int:
    """Returns the sum of all numbers from 1 to n (inclusive).

    Args:
        n (int): The upper limit number.

    Returns:
        int: The sum of all numbers from 1 to n.
    """
    if n <= 0:
        return 0
    return n + sum_of_numbers(n - 1)


print(sum_of_numbers(5))
