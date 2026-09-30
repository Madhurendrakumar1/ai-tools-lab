"""utils.py - a small collection of beginner-friendly helper functions."""


def is_palindrome(s):
    """Return True if the string reads the same forwards and backwards.

    Spaces, punctuation, and capital letters are ignored, so
    "A man, a plan, a canal: Panama" counts as a palindrome.

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("Hello")
        False
    """
    # Keep only letters and digits, and make them lowercase
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    # A palindrome is equal to its own reverse
    return cleaned == cleaned[::-1]


def count_words(text):
    """Return the number of words in the text.

    Words are separated by whitespace (spaces, tabs, or new lines).

    Examples:
        >>> count_words("Hello world")
        2
        >>> count_words("   ")
        0
    """
    # split() with no arguments splits on any whitespace
    # and ignores extra spaces at the start, middle, or end
    words = text.split()
    return len(words)


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    Formula: F = C * 9/5 + 32

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return c * 9 / 5 + 32


# This block only runs when you execute the file directly
# (python utils.py), not when you import it from another file.
if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("Hello"))                            # False
    print(count_words("The quick brown fox"))                # 4
    print(celsius_to_fahrenheit(37))                         # 98.6