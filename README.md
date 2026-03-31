# Caesar Cipher Implementation

## PRODIGY_CS_01

A simple Python implementation of the Caesar Cipher encryption technique for text encryption and decryption.

### Features

- **Text Encryption**: Encrypt plaintext messages using a shift value
- **Text Decryption**: Decrypt ciphertext back to original text
- **Case Preservation**: Maintains uppercase and lowercase letters
- **Non-Alphabetic Handling**: Preserves numbers, symbols, and spaces
- **Interactive Interface**: User-friendly command-line interface

### How It Works

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions down the alphabet. For example, with a shift of 3:
- A → D
- B → E
- C → F
- ...
- X → A
- Y → B
- Z → C

Decryption works by shifting in the opposite direction (negative shift).

### Installation

1. Ensure Python 3.x is installed on your system
2. Clone or download the repository
3. Navigate to the PRODIGY_CS_01 directory

### Usage

Run the script:

```bash
python text-encryption.py
```

Follow the prompts:
1. Enter the text to encrypt/decrypt
2. Choose 1 for encryption or 2 for decryption
3. Enter the shift value (1-25 recommended)

### Example

```
Enter the text: Hello World!
1. Encrypt
2. Decrypt
choice: 1
Enter the shift value: 3
The encrypted text is: Khoor Zruog!
```

### Knowledge Gained

- Understanding of basic encryption algorithms
- Character manipulation using ASCII values
- Modular arithmetic for alphabet wrapping
- Input validation and user interaction in Python