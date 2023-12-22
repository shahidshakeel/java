'''Description
Create a Python script that sorts a list of mixed data types into separate lists for integers, strings, and other types.'''
def sort_and_filter_list(mixed_list):
    integers = []
    strings = []
    others = []

    for item in mixed_list:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, str):
            strings.append(item)
        else:
            others.append(item)

    return {"integers": integers, "strings": strings, "others": others}
   
    #return {"integers": [], "strings": [], "others": []}

def main():
    # Tests for the sort_and_filter_list function
    test_cases = [
        ([1, "apple", 2, "banana", 3.5, None], {"integers": [1, 2], "strings": ["apple", "banana"], "others": [3.5, None]}),
        (["hello", 123, 45.6, "world"], {"integers": [123], "strings": ["hello", "world"], "others": [45.6]}),
        ([], {"integers": [], "strings": [], "others": []}),
        ([True, False, "True", "False"], {"integers": [], "strings": ["True", "False"], "others": [True, False]}),
        ([10, 20, "thirty", 40, "fifty"], {"integers": [10, 20, 40], "strings": ["thirty", "fifty"], "others": []})
    ]
    passed = 0
    failed = 0

    for mixed_list, expected in test_cases:
        result = sort_and_filter_list(mixed_list)
        if result == expected:
            passed += 1
        else:
            failed += 1

    print(f"Test Cases Passed: {passed}")
    print(f"Test Cases Failed: {failed}")

if __name__ == "__main__":
    main()