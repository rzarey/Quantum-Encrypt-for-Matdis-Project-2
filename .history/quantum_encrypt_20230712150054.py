from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:a
            encrypted_text += char
    return encrypted_text

def text_to_binary(text):
    binary_string = ""
    for char in text:
        binary_char = format(ord(char), '08b')  # Mengonversi karakter ke biner dengan 8 bit
        binary_string += binary_char
    return binary_string

def encrypt_message(message, key):
    circuit = QuantumCircuit(len(message), len(message))

    for i, bit in enumerate(message):
        if bit == '1':
            circuit.x(i)

    for i, bit in enumerate(key):
        if bit == '1':
            circuit.h(i)

    circuit.measure(range(len(message)), range(len(message)))

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)

    result = job.result()
    counts = result.get_counts(circuit)
    encrypted_message = list(counts.keys())[0]

    return encrypted_message

def get_key_from_cesar(shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    key = shifted_alphabet[0]
    for char in shifted_alphabet:
        if shifted_alphabet.count(char) > shifted_alphabet.count(key):
            key = char
    key_binary = format(ord(key), '08b')
    return key_binary

# Memasukkan pesan dan pergeseran dari pengguna
message = input("Masukkan pesan yang akan dikirimkan: ")
shift = int(input("Masukkan Key (berupa angka): "))

# Enkripsi menggunakan Caesar Cipher
encrypted_text = caesar_encrypt(message, shift)

# Konversi teks menjadi binary
binary_text = text_to_binary(encrypted_text)

# Mendapatkan key untuk enkripsi kuantum dari Caesar Cipher
key_quantum = get_key_from_cesar(shift)

# Enkripsi menggunakan Quantum
encrypted_message = encrypt_message(binary_text, key_quantum)

# Menampilkan hasil enkripsi
print("Pesan terenkripsi:", encrypted_message)