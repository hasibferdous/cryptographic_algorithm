import matplotlib.pyplot as plt

# Data for plotting
file_sizes = ["1 MB", "100 MB", "1 GB"]
rsa_encryption_times = [0.000998, 0.000365, 0.000424]
rsa_decryption_times = [0.001751, 0.001449, 0.001419]
elgamal_encryption_times = [0.001837, 0.001691, 0.001789]
elgamal_decryption_times = [0.001061, 0.001044, 0.001055]

# Plotting encryption times
plt.figure(figsize=(10, 6))
plt.plot(file_sizes, rsa_encryption_times, label="RSA Encryption", marker="o")
plt.plot(file_sizes, elgamal_encryption_times, label="ElGamal Encryption", marker="o")
plt.title("Encryption Time Comparison")
plt.xlabel("File Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()
plt.show()

# Plotting decryption times
plt.figure(figsize=(10, 6))
plt.plot(file_sizes, rsa_decryption_times, label="RSA Decryption", marker="o")
plt.plot(file_sizes, elgamal_decryption_times, label="ElGamal Decryption", marker="o")
plt.title("Decryption Time Comparison")
plt.xlabel("File Size")
plt.ylabel("Time (seconds)")
plt.legend()
plt.grid()
plt.show()
