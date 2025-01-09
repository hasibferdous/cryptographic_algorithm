import os
import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from sympy import mod_inverse, isprime, randprime
from random import randint

# Define the 10-digit key (0424313011) as bytes
KEY = b"0424313011"

# Function to generate test files of specified sizes
def generate_test_files():
    sizes = [1 * 1024 * 1024, 100 * 1024 * 1024, 1 * 1024 * 1024 * 1024]  # 1MB, 100MB, 1GB
    filenames = []
    for size in sizes:
        filename = f"test_{size // (1024 * 1024)}MB.txt"
        with open(filename, "wb") as f:
            f.write(os.urandom(size))  # Write random bytes
        filenames.append(filename)
    return filenames

# RSA Implementation
def rsa_cryptography(file_path):
    print(f"\nProcessing {file_path} with RSA...")
    with open(file_path, "rb") as f:
        data = f.read()
    
    # RSA key generation
    rsa_key = RSA.generate(1024)
    private_key = rsa_key
    public_key = rsa_key.publickey()

    # Encryption
    cipher = PKCS1_OAEP.new(public_key)
    start_time = time.time()
    ciphertext = cipher.encrypt(KEY)
    encryption_time = time.time() - start_time

    # Decryption
    cipher = PKCS1_OAEP.new(private_key)
    start_time = time.time()
    decrypted_key = cipher.decrypt(ciphertext)
    decryption_time = time.time() - start_time

    print(f"RSA Encryption Time: {encryption_time:.6f} seconds")
    print(f"RSA Decryption Time: {decryption_time:.6f} seconds")
    return encryption_time, decryption_time

# ElGamal Manual Implementation
def elgamal_generate_keys(bits=512):
    """Generate ElGamal keys."""
    p = randprime(2**(bits - 1), 2**bits)
    g = randint(2, p - 1)
    x = randint(1, p - 2)
    h = pow(g, x, p)
    public_key = (p, g, h)
    private_key = x
    return public_key, private_key

def elgamal_encrypt(public_key, message):
    """Encrypt a message using ElGamal."""
    p, g, h = public_key
    y = randint(1, p - 2)
    c1 = pow(g, y, p)
    s = pow(h, y, p)
    c2 = (int.from_bytes(message, 'big') * s) % p
    return (c1, c2)

def elgamal_decrypt(private_key, public_key, ciphertext):
    """Decrypt a ciphertext using ElGamal."""
    p, _, _ = public_key
    c1, c2 = ciphertext
    s = pow(c1, private_key, p)
    s_inv = mod_inverse(s, p)
    decrypted = (c2 * s_inv) % p
    decrypted_bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return decrypted_bytes

def elgamal_cryptography(file_path):
    print(f"\nProcessing {file_path} with ElGamal...")
    with open(file_path, "rb") as f:
        data = f.read()

    # Key generation
    public_key, private_key = elgamal_generate_keys()

    # Encryption
    start_time = time.time()
    ciphertext = elgamal_encrypt(public_key, KEY)
    encryption_time = time.time() - start_time

    # Decryption
    start_time = time.time()
    decrypted_key = elgamal_decrypt(private_key, public_key, ciphertext)
    decryption_time = time.time() - start_time

    print(f"ElGamal Encryption Time: {encryption_time:.6f} seconds")
    print(f"ElGamal Decryption Time: {decryption_time:.6f} seconds")
    return encryption_time, decryption_time

# Main function to run the performance analysis
def main():
    print("Generating test files...")
    test_files = generate_test_files()  # Create files of 1MB, 100MB, 1GB

    results = {"RSA": [], "ElGamal": []}

    for file_path in test_files:
        rsa_result = rsa_cryptography(file_path)
        results["RSA"].append(rsa_result)

        elgamal_result = elgamal_cryptography(file_path)
        results["ElGamal"].append(elgamal_result)

        # Clean up the test files to save space
        os.remove(file_path)

    print("\nFinal Results:")
    for algo, times in results.items():
        print(f"\n{algo} Performance:")
        for i, (enc_time, dec_time) in enumerate(times):
            file_size = ["1 MB", "100 MB", "1 GB"][i]
            print(f"  File Size: {file_size} - Encryption: {enc_time:.6f}s, Decryption: {dec_time:.6f}s")

if __name__ == "__main__":
    main()
