def calculate_factorial(n):
    """Executes code based on conditions.

    Args:
        n (Any): Parameter for controlling n behavior.

    Returns:
        Any: The result of the computation.
    """

    if n == 0:
        return 1
    return n * calculate_factorial(n-1)