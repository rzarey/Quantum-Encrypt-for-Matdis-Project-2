#include <iostream>
#include <string>
#include <cmath>

using namespace std;

// Fungsi untuk mengenkripsi pesan
string encrypt(string message, int key) {
    string encrypted_message = "";
    for (int i = 0; i < message.length(); i++) {
        char c = message[i];
        // Geser karakter sebanyak kunci
        c = c + key;
        // Tambahkan karakter yang sudah digeser ke pesan terenkripsi
        encrypted_message += c;
    }
    return encrypted_message;
}

// Fungsi untuk mendekripsi pesan
string decrypt(string encrypted_message, int key) {
    string decrypted_message = "";
    for (int i = 0; i < encrypted_message.length(); i++) {
        char c = encrypted_message[i];
        // Geser karakter sebanyak kunci
        c = c - key;
        // Tambahkan karakter yang sudah digeser ke pesan terdekripsi
        decrypted_message += c;
    }
    return decrypted_message;
}

int main() {
    string message = "Ini adalah pesan rahasia";
    int key = 5;

    // Enkripsi pesan
    string encrypted_message = encrypt(message, key);
    cout << "Pesan terenkripsi: " << encrypted_message << endl;

    // Dekripsi pesan
    string decrypted_message = decrypt(encrypted_message, key);
    cout << "Pesan terdekripsi: " << decrypted_message << endl;

    return 0;
}
