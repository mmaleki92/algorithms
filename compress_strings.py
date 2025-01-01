def compress_string_recursive(s, count=1, result=""):
    if len(s) == 1:  # Base case: only one character left in the substring
        return result + s[0] + (str(count) if count > 1 else "")
    
    if s[0] == s[1]:  # Current character matches the next one
        count += 1
    else:
        result += s[0] + (str(count) if count > 1 else "")
        count = 1  # Reset count for the next sequence
    
    # Recursive call with the remaining substring
    return compress_string_recursive(s[1:], count, result)

# Example usage
input_string = input("Enter a string: ")
compressed = compress_string_recursive(input_string)
print(f"Compressed string: {compressed}")
