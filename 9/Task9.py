def contains_element(list, element):
    if element in list:
        return True
    else:
        return False
    
    
    
result = contains_element([1, 2, 3, 4, 5], 6)
print(result)  # Should output True