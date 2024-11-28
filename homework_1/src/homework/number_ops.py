def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n<=1:
        return n
    return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)


def sum_of_digits_recursive(num: int) -> int:
    num = abs(num) # to handle negative numbers
    if num < 10:
        return num # if the number has only one digit
    else:
        return num % 10 + sum_of_digits_recursive(num // 10) # %10 give the last digit, //10 give all other digits


def is_palindrome_number(num: int) -> bool:
    if not isinstance(num, int):
        raise ValueError("Input must be an integer.")
    if num < 0:
        raise ValueError("Input must be positive.")
    num_str = str(num)
    return num_str == num_str[::-1] # num_str[::-1] is the flipped string
