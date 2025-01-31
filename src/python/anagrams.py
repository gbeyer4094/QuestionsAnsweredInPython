def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)


# Example usage
string1 = "listen"
string2 = "silent"
if is_anagram(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

string3 = "listens"
string4 = "silent"
if is_anagram(string3, string4):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")