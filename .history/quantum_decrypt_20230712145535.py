def decrypt_message(encrypted_message, key):
    circuit = QuantumCircuit(len(encrypted_message), len(encrypted_message))

    for i, bit in enumerate(key):
        if bit == '1':
            circuit.h(i)

    circuit.barrier()

    for i, bit in enumerate(encrypted_message):
        if bit == '1':
            circuit.x(i)
    
    circuit.barrier()

    for i in range(len(encrypted_message)):
        circuit.measure(i, i)

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)

    result = job.result()
    counts = result.get_counts(circuit)
    decrypted_message = list(counts.keys())[0]

    return decrypted_message

# Memasukkan pesan terenkripsi dan pergeseran dari pengguna
encrypted_message = input("Masukkan pesan terenkripsi: ")
shift = int(input("Masukkan jumlah pergeseran untuk Caesar Cipher: "))

# Mendapatkan key untuk dekripsi kuantum dari Caesar Cipher
key_quantum = get_key_from_cesar(shift)

# Dekripsi menggunakan Quantum
decrypted_message = decrypt_message(encrypted_message, key_quantum)

# Konversi binary ke teks
text = ""
for i in range(0, len(decrypted_message), 8):
    byte = decrypted_message[i:i+8]
    text += chr(int(byte, 2))

# Mendekripsi menggunakan Caesar Cipher
decrypted_text = caesar_encrypt(text, -shift)

# Menampilkan hasil dekripsi
print("Pesan terdekripsi:", decrypted_text)