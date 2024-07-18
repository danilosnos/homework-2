def caesar_cipher(text, shift):
    """Реализует шифр Цезаря."""
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            shifted_char = char
        result += shifted_char
    return result

shift = int(input("Введите смещение: "))
message = input("Введите сообщение: ")

encrypted_message = caesar_cipher(message, shift)
decrypted_message = caesar_cipher(encrypted_message, -shift)

print(f"Шифрованное сообщение: {encrypted_message}")
print(f"Расшифрованное сообщение: {decrypted_message}")
