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
        else:
            encrypted_text += char
    return encrypted_text

def text_to_binary(text):
    binary_string = ""
    for char in text:
        binary_char = format(ord(char), '08b')  # Mengonversi karakter ke biner dengan 8 bit
        binary_string += binary_char
    return binary_string

def get_key_from_cesar(shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    key = shifted_alphabet[0]
    for char in shifted_alphabet:
        if shifted_alphabet.count(char) > shifted_alphabet.count(key):
            key = char
    key_binary = format(ord(key), '08b')
    return key_binary

def most_frequent_bit(key):
    count_0 = 0
    count_1 = 0
    
    for bit in key:
        if bit == '0':
            count_0 += 1
        elif bit == '1':
            count_1 += 1
    
    if count_0 > count_1:
        return 0
    else:
        return 1

def encrypt_message(message, key):
    # Inisialisasi sirkuit kuantum dengan panjang pesan
    circuit = QuantumCircuit(len(message), len(message))

    # Menyiapkan qubit awal sesuai dengan pesan
    for i, bit in enumerate(message):
        if bit == '1':
            circuit.x(i)

    # Melewati kunci melalui qubit
    for i, bit in enumerate(key):
        if bit == '1':
            circuit.h(i)

    # Mengukur qubit
    circuit.measure(range(len(message)), range(len(message)))

    # Mengirim sirkuit ke simulator kuantum
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)

    # Mendapatkan hasil pengukuran
    result = job.result()
    counts = result.get_counts(circuit)
    encrypted_message = list(counts.keys())[0]  # Mengambil hasil pengukuran

    return encrypted_message

# Memasukkan teks dan pergeseran dari pengguna
text = input("Masukkan teks yang akan dienkripsi: ")
shift = int(input("Masukkan jumlah pergeseran: "))

# Enkripsi teks menggunakan cipher Caesar
encrypted_text = caesar_encrypt(text, shift)

# Konversi teks terenkripsi ke dalam bentuk biner
binary = text_to_binary(encrypted_text)

# Mendapatkan kunci dari cipher Caesar
key = get_key_from_cesar(shift)

# Mendapatkan bit yang paling sering muncul pada kunci
key_qubit = most_frequent_bit(key)

# Enkripsi pesan menggunakan kunci dan sirkuit kuantum
encrypted_message = encrypt_message(binary, key)

print("Pesan terenkripsi:", encrypted_message)