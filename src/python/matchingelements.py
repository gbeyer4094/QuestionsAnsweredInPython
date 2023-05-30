def find_matching_elements(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    matching_elements = set1.intersection(set2)
    return list(matching_elements)

# Example usage
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
matching_elements = find_matching_elements(array1, array2)
print(f"Matching elements: {matching_elements}")