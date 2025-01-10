# Re-importing the necessary library
import matplotlib.pyplot as plt

# Data for plotting
file_sizes = ["1 MB", "100 MB", "1 GB"]
three_des_encryption = [0.0531, 5.3715, 56.8452]
three_des_decryption = [0.0531, 5.7601, 55.4279]
aes_encryption = [0.0036, 0.3377, 3.8634]
aes_decryption = [0.0034, 0.3190, 3.2960]

# Plot encryption times
plt.figure(figsize=(10, 6))
plt.plot(file_sizes, three_des_encryption, label="3DES Encryption", marker="o")
plt.plot(file_sizes, aes_encryption, label="AES Encryption", marker="o")
plt.title("Encryption Time Comparison")
plt.xlabel("File Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()
plt.show()

# Plot decryption times
plt.figure(figsize=(10, 6))
plt.plot(file_sizes, three_des_decryption, label="3DES Decryption", marker="o")
plt.plot(file_sizes, aes_decryption, label="AES Decryption", marker="o")
plt.title("Decryption Time Comparison")
plt.xlabel("File Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()
plt.show()
