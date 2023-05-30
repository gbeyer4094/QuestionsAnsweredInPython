def count_vowels_and_consonants(input_string):
    vowels = 0
    consonants = 0
    for char in input_string:
        if char.lower() in 'aeiou':
            vowels += 1
        elif char.isalpha():
            consonants += 1
    return vowels, consonants


# Example usage
my_string = "Hello World!"
vowel_count, consonant_count = count_vowels_and_consonants(my_string)
print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
