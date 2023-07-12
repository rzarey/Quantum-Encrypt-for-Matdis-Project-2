def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


# Memasukkan teks dan pergeseran dari pengguna
text = input("Masukkan teks yang akan dienkripsi: ")
shift = int(input("Masukkan jumlah pergeseran: "))



encrypted_text = caesar_encrypt(text, shift)
print("Teks terenkripsi:", encrypted_text)