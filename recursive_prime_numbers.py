def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_desc(num):
    """Recursively print prime numbers from num to 0 in descending order."""
    if num < 2:
        return
    if is_prime(num):
        print(num)
    print_primes_desc(num - 1)

# Input from user
n = int(input("Enter an integer: "))
print_primes_desc(n)
