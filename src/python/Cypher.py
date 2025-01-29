def next_letter_cipher(message):
    """ Input is a hidden message that can be deciphered using the next letter in the alphabet.
    >>> next_letter_cipher('ABC')
    'BCD'
    """
    # Define the normal and next letter set alphabets
    normal_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reversed_alphabet = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'

    # Create a translation table using maketrans
    translation_table = str.maketrans(normal_alphabet, reversed_alphabet)

    # Translate the message using the translation table
    translated_message = message.translate(translation_table)

    return translated_message


def reverse_letter_cipher(message):
    """ Input is a hidden message that can be deciphered using the opposite letter in the alphabet.
    >>> reverse_letter_cipher('ABC')
    'ZYX'
    """
    # Define the normal and reversed alphabets
    normal_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reversed_alphabet = normal_alphabet[::-1]

    # Create a translation table using maketrans
    translation_table = str.maketrans(normal_alphabet, reversed_alphabet)

    # Translate the message using the translation table
    translated_message = message.translate(translation_table)

    return translated_message


if __name__ == "__main__":
    import doctest
    doctest.testmod()