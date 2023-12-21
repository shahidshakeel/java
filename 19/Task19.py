
'''
    Create two Python functions:
      celsius_to_fahrenheit and fahrenheit_to_celsius
 for converting temperatures between Celsius and Fahrenheit.
'''

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5)+32  # Placeholder for return value
    """
    TODO: Implement the celsius_to_fahrenheit function.
    """
    # TODO: Add conversion logic
    

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9  # Placeholder for return value

    """
    TODO: Implement the fahrenheit_to_celsius function.
    """
    # TODO: Add conversion logic

def main():
    # Tests for the temperature conversion functions
    celsius_test_cases = [
        (0, 32),
        (100, 212),
        (-40, -40),
        (30, 86),
        (20, 68)
    ]
    fahrenheit_test_cases = [
        (32, 0),
        (212, 100),
        (-40, -40),
        (86, 30),
        (68, 20)
    ]
    passed = 0
    failed = 0

    for celsius, expected_fahrenheit in celsius_test_cases:
        result_fahrenheit = celsius_to_fahrenheit(celsius)
        if abs(result_fahrenheit - expected_fahrenheit) < 0.001:
            passed += 1
        else:
            failed += 1

    for fahrenheit, expected_celsius in fahrenheit_test_cases:
        result_celsius = fahrenheit_to_celsius(fahrenheit)
        if abs(result_celsius - expected_celsius) < 0.001:
            passed += 1
        else:
            failed += 1

    print(f"Test Cases Passed: {passed}")
    print(f"Test Cases Failed: {failed}")

if __name__ == "__main__":
    main()