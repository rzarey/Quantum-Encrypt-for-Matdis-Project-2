#include <iostream>
#include <string>

std::string caesar_encrypt(std::string text, int shift) {
    std::string encrypted_text = "";
    for (char& c : text) {
        if (std::isalpha(c)) {
            if (std::islower(c)) {
                char encrypted_char = ((c - 'a' + shift) % 26) + 'a';
                encrypted_text += encrypted_char;
            } else {
                char encrypted_char = ((c - 'A' + shift) % 26) + 'A';
                encrypted_text += encrypted_char;
            }
        } else {
            encrypted_text += c;
        }
    }
    return encrypted_text;
}

std::string text_to_binary(std::string text) {
    std::string binary_string = "";
    for (char& c : text) {
        std::string binary_char = "";
        for (int i = 7; i >= 0; i--) {
            binary_char += ((c >> i) & 1) ? '1' : '0';
        }
        binary_string += binary_char;
    }
    return binary_string;
}

std::string encrypt_message(std::string message, std::string key) {
    std::string encrypted_message = "";
    for (int i = 0; i < message.length(); i++) {
        if (message[i] == '1') {
            encrypted_message += key[i];
        } else {
            encrypted_message += '0';
        }
    }
    return encrypted_message;
}

std::string get_key_from_cesar(int shift) {
    std::string alphabet = "abcdefghijklmnopqrstuvwxyz";
    std::string shifted_alphabet = alphabet.substr(shift) + alphabet.substr(0, shift);
    char key = shifted_alphabet[0];
    for (char& c : shifted_alphabet) {
        if (std::count(shifted_alphabet.begin(), shifted_alphabet.end(), c) > std::count(shifted_alphabet.begin(), shifted_alphabet.end(), key)) {
            key = c;
        }
    }
    std::string key_binary = "";
    for (int i = 7; i >= 0; i--) {
        key_binary += ((key >> i) & 1) ? '1' : '0';
    }
    return key_binary;
}

int main() {
    std::string message;
    int shift;

    std::cout << "Masukkan pesan yang akan dikirimkan: ";
    std::getline(std::cin, message);
    std::cout << "Masukkan jumlah pergeseran untuk Caesar Cipher: ";
    std::cin >> shift;

    // Enkripsi menggunakan Caesar Cipher
    std::string encrypted_text = caesar_encrypt(message, shift);

    // Konversi teks menjadi binary
    std::string binary_text = text_to_binary(encrypted_text);

    // Mendapatkan key untuk enkripsi kuantum dari Caesar Cipher
    std::string key_quantum = get_key_from_cesar(shift);

    // Enkripsi menggunakan Quantum
    std::string encrypted_message = encrypt_message(binary_text, key_quantum);

    // Menampilkan hasil enkripsi
    std::cout << "Pesan terenkripsi: " << encrypted_message << std::endl;

    return 0;
}
