# What This Script Does:
# This tool lets you play with Bitcoin seed phrase creation for learning using Windows Command Promt! You can:
# You can paste the hex or 128 or 256 bits of binary from the associated spreadsheets in my other repositories into the terminal it will output seed phrase and other details. 
# - Enter your own 128-bit (12 words) or 256-bit (24 words) binary (0s and 1s) or hex values.
# - See your entropy as binary, hex, and a big decimal number (e.g., 36726352627182736464736453536573854339).
# - Generate random 128-bit or 256-bit entropy using simulated dice rolls (even = 0, odd = 1).
# - Get the SHA-256 hash, a checksum, a 12-word or 24-word seed phrase, and word indices (1-2048).
# - Important: This is for education only—don’t use for real wallets unless offline on a secure system like Tails OS!

# How to Use It:
# 1. Run the script in Python (e.g., "py entropy_hash_checksum.py" in Command Prompt).
# 2. At the first prompt:
#    - Type a binary string (over 128 bits for 12 words, over 256 bits for 24 words) or hex (32 chars for 12 words, 64 chars for 24 words).
#    - Or press Enter for random entropy.
# 3. If you press Enter:
#    - Type 0 for 128 dice rolls (12 words) or 1 for 256 dice rolls (24 words).
#    - Then enter your own binary entropy, or press Enter again for dice roll generation.
# 4. Watch the output: binary, hex, decimal, SHA-256, checksum, checksum word, word indices, seed phrase, and safety notes!

import hashlib
import os
import random

# Load BIP-39 wordlist
try:
    with open("wordlist.txt", "r") as f:
        wordlist = [line.strip() for line in f.readlines()]
    if len(wordlist) != 2048:
        raise ValueError("Wordlist must contain 2048 words!")
except FileNotFoundError:
    print("Error: wordlist.txt not found! Download from https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt")
    exit(1)

# Function to simulate a dice roll and return a bit (even = 0, odd = 1)
def generate_bit_from_dice():
    roll = random.randint(1, 6)  # Simulate a dice roll (1-6)
    return '0' if roll % 2 == 0 else '1'  # Even = 0, Odd = 1

# Function to generate entropy from dice rolls
def generate_entropy_from_dice(num_bits):
    return ''.join(generate_bit_from_dice() for _ in range(num_bits))

# Seed random with secure entropy for dice rolls and passphrase
random.seed(os.urandom(32))

# Input: Binary (over 128-bit/256-bit) or hex (32-char/64-char), or random
user_input = input("Enter binary (over 128 bits for 12 words, over 256 bits for 24 words) or hex (32-char for 12 words, 64-char for 24 words), or Enter for random: ").strip()
if user_input:
    if set(user_input).issubset({'0', '1'}):
        # Binary input
        input_length = len(user_input)
        if input_length < 128:
            raise ValueError("Not enough entropy! Needs at least 128 bits for 12 words.")
        elif 128 <= input_length < 256:
            custom_binary = user_input[:128]  # Trim to 128 bits
            byte_length = 16
        elif input_length >= 256:
            custom_binary = user_input[:256]  # Trim to 256 bits
            byte_length = 32
        entropy_bytes = int(custom_binary, 2).to_bytes(byte_length, 'big')
    elif all(c in '0123456789abcdefABCDEF' for c in user_input):
        # Hex input
        if len(user_input) == 32:
            byte_length = 16
            entropy_bytes = bytes.fromhex(user_input)
            custom_binary = bin(int.from_bytes(entropy_bytes, 'big'))[2:].zfill(128)
        elif len(user_input) == 64:
            byte_length = 32
            entropy_bytes = bytes.fromhex(user_input)
            custom_binary = bin(int.from_bytes(entropy_bytes, 'big'))[2:].zfill(256)
        else:
            raise ValueError("Hex must be 32 chars (128-bit) or 64 chars (256-bit)!")
    else:
        raise ValueError("Input must be binary (0s and 1s) or hex (0-9, a-f, A-F)!")
else:
    # Random: Choose 128-bit or 256-bit with dice rolls
    choice = input("Generate random entropy with dice rolls: key in 0 for 128 dice rolls (12 words) or 1 for 256 dice rolls (24 words): ").strip()
    if choice == "0":
        byte_length = 16
        custom_input = input("Enter your own 128-bit binary entropy (or Enter for random dice rolls): ").strip()
        if custom_input:
            if len(custom_input) < 128:
                raise ValueError("Not enough entropy! Needs 128 bits for 12 words.")
            custom_binary = custom_input[:128]
            entropy_bytes = int(custom_binary, 2).to_bytes(16, 'big')
        else:
            custom_binary = generate_entropy_from_dice(128)
            entropy_bytes = int(custom_binary, 2).to_bytes(16, 'big')
            print("Entropy generated using 128 simulated dice rolls (even = 0, odd = 1).")
    elif choice == "1":
        byte_length = 32
        custom_input = input("Enter your own 256-bit binary entropy (or Enter for random dice rolls): ").strip()
        if custom_input:
            if len(custom_input) < 256:
                raise ValueError("Not enough entropy! Needs 256 bits for 24 words.")
            custom_binary = custom_input[:256]
            entropy_bytes = int(custom_binary, 2).to_bytes(32, 'big')
        else:
            custom_binary = generate_entropy_from_dice(256)
            entropy_bytes = int(custom_binary, 2).to_bytes(32, 'big')
            print("Entropy generated using 256 simulated dice rolls (even = 0, odd = 1).")
    else:
        raise ValueError("Enter 0 for 128 dice rolls or 1 for 256 dice rolls!")

# Convert binary entropy to decimal
entropy_decimal = int(custom_binary, 2)

# Entropy hex
entropy_hex = entropy_bytes.hex()

# SHA-256 of hex string as raw hex bytes
sha256_hash = hashlib.sha256(bytes.fromhex(entropy_hex)).hexdigest()

# Checksum: 4 bits (128-bit) or 8 bits (256-bit) from SHA-256
checksum_bits = 4 if byte_length == 16 else 8
checksum_hex = sha256_hash[0] if byte_length == 16 else sha256_hash[0:2]
checksum_binary = bin(int(checksum_hex, 16))[2:].zfill(checksum_bits)

# Full binary
full_binary = custom_binary + checksum_binary

# Seed phrase (132 or 264 bits, 11-bit chunks)
total_bits = 132 if byte_length == 16 else 264
word_count = 12 if byte_length == 16 else 24
words = []
for i in range(0, total_bits, 11):
    chunk = full_binary[i:i+11]
    if len(chunk) == 11:
        index = int(chunk, 2)
        words.append(wordlist[index])

# Last checksum word and its index (1-2048)
last_word = words[-1]
last_word_index = wordlist.index(last_word) + 1  # BIP-39 uses 1-based indexing

# Word indices (1-2048) for all words
word_indices = [wordlist.index(word) + 1 for word in words]

# Generate random passphrase example (6 words, lowercase, no spaces)
passphrase_example = ''.join(random.sample(wordlist, 6))

# Output
print(f"Entropy (binary, {byte_length * 8} bits): {custom_binary}")
print(f"Entropy (hex, {byte_length * 2} chars): {entropy_hex}")
print(f"Entropy (decimal): {entropy_decimal}")
print(f"SHA-256 (Hex Bytes): {sha256_hash}")
print(f"Checksum (binary, {checksum_bits} bits): {checksum_binary}")
print(f"Checksum (hex, {len(checksum_hex)} char{'s' if len(checksum_hex) > 1 else ''}): {checksum_hex}")
print(f"Last Checksum Word: {last_word} ({last_word_index})")
print(f"Full Entropy+Checksum (binary, {total_bits} bits): {full_binary}")
print(f"Word Numbers (indices 1-2048): {' '.join(map(str, word_indices))}")
print(f"Seed Phrase ({word_count} words): {' '.join(words)}")
print("\n=== IMPORTANT NOTES ===")
print("1. LEARNING EXERCISE: This script is for educational purposes only. Do not use these seed phrases for real cryptocurrency wallets unless you fully understand the risks.")
print("2. SECURITY WARNING: Only generate seed phrases on a secure, offline computer (e.g., running Tails OS) to prevent exposure to malware or network attacks.")
print("3. DATA SENSITIVITY: Seed phrases and entropy are highly sensitive. Never store them on an online device or share them. Wipe this data after use.")
print("4. VERIFICATION: Always verify seed phrases with trusted tools before use in a real wallet.")
print(f"5. EXTRA SECURITY: For added protection, consider a passphrase. Use 6 random words from the BIP-39 wordlist, all lowercase, no spaces (e.g., '{passphrase_example}'). This makes your wallet harder to crack while keeping it memorable.")
print("6. SECURE SETUP: For real-world use, consider a computer running Linux Ubuntu or Mint (Cinnamon is a great choice) for security and running Sparrow wallet. Alternatively, download the iancoleman.io webpage and run it offline to generate xPubs, zPubs, Bitcoin addresses, 12-24 word seed phrases, and passphrases.")
