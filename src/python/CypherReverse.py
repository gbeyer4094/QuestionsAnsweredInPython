import Cypher

message = input('Enter message: ')
words = message.split(' ')

encrypted_message_word = []
for word in words:
    if len(word.strip()) > 0:
        encrypted_message_word.append(Cypher.reverse_letter_cipher(word.upper()))
print("Original Message:", message)
print("Encrypted Message:", encrypted_message_word)

