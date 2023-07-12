#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Fungsi Caesar Cipher
string caesarCipher(string text, int shift) {
    string result = "";
    for (int i = 0; i < text.length(); i++) {
        if (isupper(text[i]))
            result += char(int(text[i] + shift - 65) % 26 + 65);
        else
            result += char(int(text[i] + shift - 97) % 26 + 97);
    }
    return result;
}

// Fungsi Transposisi
string transpositionCipher(string text) {
    reverse(text.begin(), text.end());
    return text;
}

// Fungsi XOR Cipher
string xorCipher(string text, char key) {
    string result = "";
    for (int i = 0; i < text.length(); i++) {
        result += text[i] ^ key;
    }
    return result;
}

// Fungsi Enkripsi
string encrypt(string text, int shift, char key) {
    string result = caesarCipher(text, shift);
    result = transpositionCipher(result);
    result = xorCipher(result, key);
    return result;
}

// Fungsi Dekripsi
string decrypt(string text, int shift, char key) {
    string result = xorCipher(text, key);
    result = transpositionCipher(result);
    result = caesarCipher(result, 26 - shift);
    return result;
}

int main() {
    string text;
    int shift;
    char key;

    cout << "Masukkan pesan: ";
    getline(cin, text);

    cout << "Masukkan nilai shift (berupa angka) : ";
    cin >> shift;

    cout << "Masukkan kunci (berupa huruf ): ";
    cin >> key;

    cin.ignore(); // Membersihkan newline character dari input sebelumnya

    string encrypted = encrypt(text, shift, key);
    cout << "Pesan terenkripsi: " << encrypted << endl;

    string decrypted = decrypt(encrypted, shift, key);
    cout << "Pesan terdekripsi: " << decrypted << endl;

    return 0;
}
