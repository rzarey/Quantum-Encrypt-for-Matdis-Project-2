// #include <iostream>
// #include <string>
// #include <bitset>
// #include <bits/stdc++.h>

// using namespace std;

// string caesar_encrypt(string text, int shift) {
//     string encrypted_text = "";
//     for (char& c : text) {
//         if (isalpha(c)) {
//             if (islower(c)) {
//                 char encrypted_char = ((c - 'a' + shift) % 26 + 'a');
//                 encrypted_text += encrypted_char;
//             }
//             else {
//                 char encrypted_char = ((c - 'A' + shift) % 26 + 'A');
//                 encrypted_text += encrypted_char;
//             }
//         }
//         else {
//             encrypted_text += c;
//         }
//     }
//     return encrypted_text;
// }

// string text_to_binary(string text) {
//     string binary_string = "";
//     for (char& c : text) {
//         string binary_char = bitset<8>(c).to_string();
//         binary_string += binary_char;
//     }
//     return binary_string;
// }

// string get_key_from_cesar(int shift) {
//     string alphabet = "abcdefghijklmnopqrstuvwxyz";
//     string shifted_alphabet = alphabet.substr(shift) + alphabet.substr(0, shift);
//     char key = shifted_alphabet[0];
//     for (char& c : shifted_alphabet) {
//         if (count(shifted_alphabet.begin(), shifted_alphabet.end(), c) > count(shifted_alphabet.begin(), shifted_alphabet.end(), key)) {
//             key = c;
//         }
//     }
//     string key_binary = bitset<8>(key).to_string();
//     return key_binary;
// }

// string encrypt_message(string message, string key) {
//     string encrypted_message = "";
//     for (int i = 0; i < message.size(); i += 8) {
//         string binary_char = message.substr(i, 8);
//         bitset<8> binary(binary_char);
//         char c = binary.to_ulong();
//         encrypted_message += c;
//     }
//     return caesar_encrypt(encrypted_message, stoi(key, nullptr, 2));
// }

// int main() {
//     string text, encrypted_text, binary, key, encrypted_message;
//     int shift;

//     cout << "Masukkan teks yang akan dienkripsi: ";
//     getline(cin, text);
//     cout << "Masukkan jumlah pergeseran: ";
//     cin >> shift;

//     encrypted_text = caesar_encrypt(text, shift);
//     cout << "Teks terenkripsi: " << encrypted_text << endl;

//     binary = text_to_binary(text);
//     cout << "Hasil Konversi ke Biner: " << binary << endl;

//     key = get_key_from_cesar(shift);
//     cout << "Kunci: " << key << endl;

//     encrypted_message = encrypt_message(binary, key);
//     cout << "Pesan terenkripsi: " << encrypted_message << endl;

//     return 0;
// }



#include <iostream>
#include <bitset>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <complex>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>
#include <iomanip>
#include <random>
#include <chrono>
#include <omp.h>
#include <Eigen/Dense>
#include <Eigen/Eigenvalues>
#include <unsupported/Eigen/MatrixFunctions>

using namespace std;
using namespace Eigen;

// Fungsi untuk mengubah teks menjadi representasi biner
string textToBinary(string text) {
    string binary = "";
    for (char& c : text) {
        binary += bitset<8>(c).to_string();
    }
    return binary;
}

// Fungsi untuk mengubah representasi biner menjadi teks
string binaryToText(string binary) {
    string text = "";
    for (size_t i = 0; i < binary.size(); i += 8) {
        string byte = binary.substr(i, 8);
        text += bitset<8>(byte).to_ulong();
    }
    return text;
}

// Fungsi untuk mengenkripsi pesan biner menggunakan sirkuit kuantum
string quantumEncryption(string message) {
    // Inisialisasi sirkuit kuantum dengan 2 qubit
    MatrixXd state = MatrixXd::Zero(4, 1);
    state(0, 0) = 1.0;
    MatrixXd H = MatrixXd::Zero(4, 4);
    H << 1, 1, 1, 1,
         1, -1, 1, -1,
         1, 1, -1, -1,
         1, -1, -1, 1;
    MatrixXd CX = MatrixXd::Zero(4, 4);
    CX << 1, 0, 0, 0,
          0, 1, 0, 0,
          0, 0, 0, 1,
          0, 0, 1, 0;

    // Mengenkripsi pesan dengan operasi XOR
    if (message[0] == '1') {
        state.row(1).swap(state.row(2));
    }
    if (message[1] == '1') {
        state.row(0).swap(state.row(3));
    }

    // Mengenkripsi pesan dengan operasi Hadamard dan CNOT
    state = H * state;
    state = CX * state;

    // Mengukur qubit dan menyimpan hasilnya ke bit klasik
    int q1 = rand() % 2;
    int q2 = rand() % 2;

    // Mengembalikan hasil enkripsi
    return to_string(q1) + to_string(q2);
}

// Fungsi untuk mendekripsi ciphertext menggunakan sirkuit kuantum
string quantumDecryption(string ciphertext) {
    // Inisialisasi sirkuit kuantum dengan 2 qubit
    MatrixXd state = MatrixXd::Zero(4, 1);
    state(0, 0) = 1.0;
    MatrixXd H = MatrixXd::Zero(4, 4);
    H << 1, 1, 1, 1,
         1, -1, 1, -1,
         1, 1, -1, -1,
         1, -1, -1, 1;
    MatrixXd CX = MatrixXd::Zero(4, 4);
    CX << 1, 0, 0, 0,
          0, 1, 0, 0,
          0, 0, 0, 1,
          0, 0, 1, 0;

    // Mengubah ciphertext menjadi pesan biner
    string message = "";
    if (ciphertext[0] == '1') {
        message += '1';
    } else {
        message += '0';
    }
    if (ciphertext[1] == '1') {
        message += '1';
    } else {
        message += '0';
    }

    // Mengenkripsi pesan dengan operasi Hadamard terbalik
    state = CX * state;
    state = H * state;

    // Mengenkripsi pesan dengan operasi XOR terbalik
    if (message[1] == '1') {
        state.row(0).swap(state.row(3));
    }
    if (message[0] == '1') {
        state.row(1).swap(state.row(2));
    }

    // Mengukur qubit dan menyimpan hasilnya ke bit klasik
    int q1 = rand() % 2;
    int q2 = rand() % 2;

    // Mengembalikan hasil dekripsi
    return binaryToText(to_string(q1) + to_string(q2));
}

int main() {
    // Meminta input pesan dari pengguna
    string plaintext;
    cout << "Masukkan teks yang akan dienkripsi: ";
    getline(cin, plaintext);

    // Mengenkripsi teks
    string ciphertext = quantumEncryption(textToBinary(plaintext));
    cout << "Hasil enkripsi: " << ciphertext << endl;

    // Mendekripsi teks
    string decryptedText = quantumDecryption(ciphertext);
    cout << "Hasil dekripsi: " << decryptedText << endl;

    return 0;
}