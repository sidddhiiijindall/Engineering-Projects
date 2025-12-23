#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

/**
 * IronFolder: A Cryptographic File Utility
 * Logic: Symmetric XOR Cipher
 * This project demonstrates File I/O, Binary Streams, and Bitwise logic.
 */

void processFile(string inputPath, string outputPath, string key) {
    // Open files in binary mode to support all file types (PDF, JPG, TXT)
    ifstream inFile(inputPath, ios::binary);
    ofstream outFile(outputPath, ios::binary);

    if (!inFile || !outFile) {
        cout << "[ERROR] Could not access files. Ensure the filename is correct." << endl;
        return;
    }

    char currentByte;
    int index = 0;
    int keyLength = key.length();

    // Process file byte-by-byte
    while (inFile.get(currentByte)) {
        // XOR bitwise operation for encryption/decryption
        // The modulo (%) operator wraps the key around the file data
        char processedByte = currentByte ^ key[index % keyLength];
        outFile.put(processedByte);
        index++;
    }

    inFile.close();
    outFile.close();
    
    cout << "-----------------------------------------------" << endl;
    cout << "[SUCCESS] File processed saved as: " << outputPath << endl;
    cout << "-----------------------------------------------" << endl;
}

int main() {
    int mode;
    string filename, secretKey;

    cout << "========================================" << endl;
    cout << "       IRONFOLDER SECURITY SYSTEM       " << endl;
    cout << "========================================" << endl;
    cout << "1. Encrypt File\n2. Decrypt File\n3. Exit\nSelection: ";
    cin >> mode;

    if (mode == 3) return 0;

    cout << "Enter target filename: ";
    cin >> filename;
    cout << "Enter your Secret Key: ";
    cin >> secretKey;

    if (mode == 1) {
        processFile(filename, "encrypted_" + filename, secretKey);
    } else if (mode == 2) {
        processFile(filename, "decrypted_" + filename, secretKey);
    } else {
        cout << "Invalid selection." << endl;
    }

    return 0;
}