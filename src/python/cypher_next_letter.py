import cypher

message = input('Enter message: ')
words = message.split(' ')
print(words)
encrypted_message_word = []
for word in words:
    if len(word.strip()) > 0:
        encrypted_message_word.append(Cypher.next_letter_cipher(word.upper()))
print("Original Message:", message)
print("Encrypted Message:", encrypted_message_word)

