def is_odd_count_even(numbers):
    """
    Determine if the count of odd numbers in the list is even.

    Parameters:
    - numbers: List of integers

    Returns:
    - True if the count of odd numbers is even, False otherwise.
    """
    odd_count = sum(1 for num in numbers if num % 2 != 0)  # Count odd numbers
    return odd_count % 2 == 0  # Check if the count is even


# Example usage
input_numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
if is_odd_count_even(input_numbers):
    print("The count of odd numbers is even.")
else:
    print("The count of odd numbers is odd.")
