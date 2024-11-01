import random

# Menghasilkan array x dengan 20 nilai random dari 0 sampai 10
x = [random.randint(0, 10) for _ in range(20)]

# Mencetak array x
print("Array x:", x)

# Mengambil inputan bilangan
y1 = int(input("Masukkan bilangan (genap/ganjil): "))

# Memeriksa apakah bilangan yang dimasukkan genap atau ganjil
if y1 % 2 == 0:  # Bilangan genap
    # Mencari indeks dari bilangan genap y1 dalam array x
    indices = [i for i, value in enumerate(x) if value == y1]
    if indices:
        print(f"Bilangan {y1} ada di index: {', '.join(map(str, indices))}")
    else:
        print(f"Bilangan {y1} tidak ditemukan dalam array.")
else:  # Bilangan ganjil
    raise ValueError("Error: Bilangan yang dimasukkan adalah ganjil.")
