from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

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
        binary_char = format(ord(char), '08b')
        binary_string += binary_char
    return binary_string

def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        binary_char = binary[i:i+8]
        decimal_char = int(binary_char, 2)
        char = chr(decimal_char)
        text += char
    return text

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
        return '0'
    else:
        return '1'

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

def decrypt_message(encrypted_message, key_qubit):
    circuit = QuantumCircuit(len(encrypted_message), len(encrypted_message))
    for i, bit in enumerate(key_qubit):
        if bit == '1':
            circuit.h(i)
    for i, bit in enumerate(encrypted_message):
        if bit == '1':
            circuit.x(i)
    circuit.measure(range(len(encrypted_message)), range(len(encrypted_message)))
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1)
    result = job.result()
    counts = result.get_counts(circuit)
    decrypted_message = list(counts.keys())[0]
    return decrypted_message

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet("background-color: #F0F0F0; color: #333333;")
        self.setWindowTitle('Program Enkripsi dan Dekripsi Kuantum Caesar Cipher (QCC) v1.0')
        self.setWindowIcon(QIcon('decryption.png'))

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        self.label = QLabel('Masukkan teks:')
        vbox.addWidget(self.label)

        self.textEdit = QTextEdit()
        vbox.addWidget(self.textEdit)

        self.labelShift = QLabel('Masukkan jumlah pergeseran:')
        vbox.addWidget(self.labelShift)

        self.lineEditShift = QLineEdit()
        vbox.addWidget(self.lineEditShift)

        self.btnEncrypt = QPushButton(' Enkripsi', self)
        self.btnEncrypt.setIcon(QIcon('encrypt.png'))
        self.btnEncrypt.setStyleSheet("background-color: #4CAF50; color: black;")
        self.btnEncrypt.clicked.connect(self.encrypt)
        vbox.addWidget(self.btnEncrypt)

        self.btnDecrypt = QPushButton(' Dekripsi', self)
        self.btnDecrypt.setIcon(QIcon('decrypt.png'))
        self.btnDecrypt.setStyleSheet("background-color: #2196F3; color: black;")
        self.btnDecrypt.clicked.connect(self.decrypt)
        vbox.addWidget(self.btnDecrypt)
        vbox.addWidget(self.btnDecrypt)

        self.labelResult = QLabel('Hasil:')
        vbox.addWidget(self.labelResult)

        self.textEditResult = QTextEdit()
        vbox.addWidget(self.textEditResult)

        self.labelCreator = QLabel('Created by Reyhansssan Islamey - 2200018411')
        self.labelCreator.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.labelCreator)

        self.setGeometry(300, 300, 300, 200)
        self.show()

    def encrypt(self):
        text = self.textEdit.toPlainText()
        shift = int(self.lineEditShift.text())
        encrypted_text = caesar_encrypt(text, shift)
        binary = text_to_binary(encrypted_text)
        key = get_key_from_cesar(shift)
        key_qubit = most_frequent_bit(key)
        encrypted_message = encrypt_message(binary, key)
        self.textEditResult.setText(encrypted_message)

    def decrypt(self):
        encrypted_message = self.textEdit.toPlainText()
        shift = int(self.lineEditShift.text())
        key = get_key_from_cesar(shift)
        key_qubit = most_frequent_bit(key)
        decrypted_message = decrypt_message(encrypted_message, key_qubit)
        text = binary_to_text(decrypted_message)
        decrypted_text = caesar_encrypt(text, -shift)
        self.textEditResult.setText(decrypted_text)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())