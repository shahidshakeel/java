def count_word_frequency(text):
    words = text.split(" ")
    word_freq = {}

    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq

def main():
    # Tests for the count_word_frequency function
    test_cases = [
        ("hello world hello", {"hello": 2, "world": 1}),
        ("repeat words repeat words words", {"repeat": 2, "words": 3}),
        ("", {}),
        ("one word", {"one": 1, "word": 1}),
        ("punctuation, and punctuation; again", {"punctuation": 2, "and": 1, "again": 1})
    ]
    passed = 0
    failed = 0

    for text, expected in test_cases:
        result = count_word_frequency(text)
        if result == expected:
            passed += 1
        else:
            failed += 1

    print(f"Test Cases Passed: {passed}")
    print(f"Test Cases Failed: {failed}")

if __name__ == "__main__":
    main()