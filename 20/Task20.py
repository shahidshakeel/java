'''Description
Develop a Python function is_palindrome that checks if a given string is a palindrome (reads the same forward and backward).'''

def is_palindrome(text):

     # Remove spaces and convert text to lowercase
    text = text.replace(" ", "").lower()
    
    # Compare the text with its reverse
    return text == text[::-1]

def main():
    # Tests for the is_palindrome function
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("radar", True),
        ("python", False)
    ]
    passed = 0
    failed = 0

    for text, expected in test_cases:
        result = is_palindrome(text)
        if result == expected:
            passed += 1
        else:
            failed += 1

    print(f"Test Cases Passed: {passed}")
    print(f"Test Cases Failed: {failed}")

if __name__ == "__main__":
    main()