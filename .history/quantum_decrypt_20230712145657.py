from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
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
        binary_char = binary[i:i+8]
        decimal_char = int(binary_char, 2)
        char = chr(decimal_char)
        text += char
    return text

def decrypt_message(encrypted_message, key):
    circuit = QuantumCircuit(len(encrypted_message), len(encrypted_message))

    for i, bit in enumerate(key):
        if bit == '1':
            circuit.h(i)

    circuit.measure(range(len(encrypted_message)), range(len(encrypted_message)))

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)

    result = job.result()
    counts = result.get_counts(circuit)
    binary_text = list(counts.keys())[0]

    decrypted_text = binary_to_text(binary_text)

    return decrypted_text

# Memasukkan pesan terenkripsi dan pergeseran dari pengguna
encrypted_message = input("Masukkan pesan terenkripsi: ")
shift = int(input("Masukkan jumlah pergeseran untuk Caesar Cipher: "))

# Deskripsi menggunakan Quantum
binary_text = decrypt_message(encrypted_message, get_key_from_cesar(shift))

# Konversi binary ke teks
decrypted_text = binary_to_text(binary_text)

# Deskripsi menggunakan Caesar Cipher
decrypted_message = caesar_decrypt(decrypted_text, shift)

# Menampilkan hasil deskripsi
print("Pesan terdeskripsi:", decrypted_message)