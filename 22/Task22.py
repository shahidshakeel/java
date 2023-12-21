def calculate_expression(expression):
    #return expression  # Placeholder for return value
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

    """
    TODO: Implement the calculate_expression function.
    """
    # TODO: Add logic to evaluate the arithmetic expression

def main():
    # Tests for the calculate_expression function
    test_cases = [
        ("2 + 2", 4),
        ("3 * 4", 12),
        ("10 / 5", 2),
        ("5 - 3", 2),
        ("1 + 2 * 3", 7)  # Assuming standard order of operations
    ]
    passed = 0
    failed = 0

    for expression, expected in test_cases:
        result = calculate_expression(expression)
        if abs(result - expected) < 0.001:
            passed += 1
        else:
            failed += 1

    print(f"Test Cases Passed: {passed}")
    print(f"Test Cases Failed: {failed}")

if __name__ == "__main__":
    main()