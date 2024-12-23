# -*- coding: utf-8 -*-
"""TubesAKA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Wnda6ww3qcTkcP3NjRoklq2mzt86c6DX
"""

import random
import time
import matplotlib.pyplot as plt

#Membuat string binary 16 angka secara random
#Contoh data "0110010101101001"
#Tiap nilai fingerprints unik dan tidak mempunyai duplikasi data
def generate_random_fingerprints(n, length=16):
    fingerprints = set()
    while len(fingerprints) < n:
        fingerprint = "".join(random.choice("01") for _ in range(length))
        fingerprints.add(fingerprint)
    return list(fingerprints)

#Membuat string nama suspect secara simpel
#Contoh data "Suspect_i" dimana i adalah ukuran data yang secara otomatis bertambah sesuai ukuran input
def generate_random_suspects(n):
    return [f"Suspect_{i}" for i in range(1, n + 1)]

#Sequential Search
def sequential_search(data, target):
    for index in range(len(data)):
        if data[index] == target:
            return index
    return -1

#Binary search untuk perbandingan DNA/Sidik Jari secara rekursif dengan syarat data telah terurut
def binary_search(data, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if data[mid][1] == target:
        return mid
    elif data[mid][1] > target:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)

#Mendefinisikan ukuran data yang dipakai untuk perbandingan
sizes = range(300, 3001, 300)  #Minimal 300 dan maksimal 3000 dengan langkah sebanyak 300
seq_times = []
bin_times = []
for size in sizes:
    fingerprints = generate_random_fingerprints(size)
    suspects = generate_random_suspects(size)
    suspect_data = list(zip(suspects, fingerprints))  #Mengassign suspect ke sebuah sidik jari dengan contoh data: Suspect_i
    suspect_data_sorted = sorted(suspect_data, key=lambda x: x[1])  #Sorting data untuk preprocessing pada binary search
    fingerprint_to_find = '111010110101001' #Median data (suspect_data_sorted[size // 2][1]) atau bisa menggunakan value sendiri contoh '001010110101001'

    #Menghitung waktu untuk sequential search
    start_time = time.time()
    sequential_search([item[1] for item in suspect_data], fingerprint_to_find)
    seq_times.append(time.time() - start_time)

   #Menghitung waktu untuk binary search
    start_time = time.time()
    binary_search(suspect_data_sorted, fingerprint_to_find, 0, len(suspect_data_sorted) - 1)
    bin_times.append(time.time() - start_time)

#Graph perbandingan
plt.figure(figsize=(10, 6))

#PLot waktunya
plt.plot(sizes, seq_times, marker='o', label="Sequential Search")
plt.plot(sizes, bin_times, marker='s', label="Binary Search")

#Penambahan deskripsi graph
plt.title("Perbandingan Waktu Komputasi")
plt.xlabel("Ukuran Dataset")
plt.ylabel("Waktu dalam Sekon")
plt.legend()
plt.grid(True)
plt.tight_layout()

#Panggil fungsi graph
plt.show()

#Contoh output hasil searching
print("Ukuran Dataset | Waktu Sequential Search | Waktu Binary Search")
print("------------------------------------------------------")
for size, seq_time, bin_time in zip(sizes, seq_times, bin_times):
    print(f"{size:<12}   | {seq_time:.6f} s              | {bin_time:.6f} s")

#Contoh dataset yang dipakai
print("\nKolom Dataset: ['Nama Suspect', 'Fingerprint dalam Binary String']")
sample_suspect_data = list(zip(generate_random_suspects(5), generate_random_fingerprints(5)))
print("Nilai Sampel:")
for suspect, fingerprint in sample_suspect_data:
    print(f"Nama: {suspect}, DNA: {fingerprint}")