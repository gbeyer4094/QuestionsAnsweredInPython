def count_occurrences(input_string, character):
    return input_string.count(character)


# Example usage
base = "Hello, World!"
character_to_count = "l"
occurrences = count_occurrences(base, character_to_count)
print(f"The character '{character_to_count}' appears {occurrences} times.")
