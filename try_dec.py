from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        binary_char = binary[i:i+8]  # Mengambil 8 bit biner untuk setiap karakter
        decimal_char = int(binary_char, 2)  # Mengonversi biner menjadi bilangan desimal
        char = chr(decimal_char)  # Mengonversi bilangan desimal ke karakter
        text += char
    return text

def decrypt_message(encrypted_message, key):
    # Inisialisasi sirkuit kuantum dengan panjang pesan terenkripsi
    circuit = QuantumCircuit(len(encrypted_message), len(encrypted_message))

    # Melewati kunci melalui qubit
    for i, bit in enumerate(key):
        if bit == '1':
            circuit.h(i)

    # Menyiapkan qubit awal dengan pesan terenkripsi
    for i, bit in enumerate(encrypted_message):
        if bit == '1':
            circuit.x(i)

    # Mengukur qubit
    circuit.measure(range(len(encrypted_message)), range(len(encrypted_message)))

    # Mengirim sirkuit ke simulator kuantum
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)

    # Mendapatkan hasil pengukuran
    result = job.result()
    counts = result.get_counts(circuit)
    decrypted_message = list(counts.keys())[0]  # Mengambil hasil pengukuran

    return decrypted_message

# Memasukkan pesan terenkripsi dan pergeseran yang digunakan saat enkripsi
encrypted_message = input("Masukkan pesan terenkripsi: ")
shift = int(input("Masukkan jumlah pergeseran yang digunakan saat enkripsi: "))

# Mendapatkan kunci dari pergeseran Caesar
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
key = shifted_alphabet[0]
for char in shifted_alphabet:
    if shifted_alphabet.count(char) > shifted_alphabet.count(key):
        key = char
key_binary = format(ord(key), '08b')

# Mendekripsi pesan menggunakan kunci dan sirkuit kuantum
decrypted_message = decrypt_message(encrypted_message, key_binary)

# Mengonversi representasi biner ke dalam teks
text = binary_to_text(decrypted_message)

# Mendekripsi teks menggunakan Caesar Cipher
decrypted_text = caesar_decrypt(text, shift)

print("Teks terdekripsi:", decrypted_text)