def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_recursive(num):
    """Recursively count the number of prime numbers less than or equal to num."""
    if num < 2:
        return 0  # No primes below 2
    # Check if the current number is prime and add 1 if it is
    return (1 if is_prime(num) else 0) + count_primes_recursive(num - 1)

# Input from the user
n = int(input("Enter an integer: "))
count = count_primes_recursive(n)
print(f"The number of prime numbers less than or equal to {n} is: {count}")
