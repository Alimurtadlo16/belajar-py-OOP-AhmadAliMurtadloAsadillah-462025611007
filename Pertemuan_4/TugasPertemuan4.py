#Pertemuan 4
class Produk:
    def __init__(self, nama, harga):
        """Metode inisialisasi untuk atribut objek."""
        self.nama = nama
        self.harga = harga

    def __str__(self):
        """Representasi teks yang informatif saat objek di-print."""
        return f"Produk: {self.nama} | Harga: Rp{self.harga:,}"

    # Implementasi 3 Metode Perbandingan
    def __eq__(self, other):
        """Memeriksa apakah harga dua produk sama (==)."""
        if isinstance(other, Produk):
            return self.harga == other.harga
        return False

    def __lt__(self, other):
        """Memeriksa apakah harga produk lebih murah (<)."""
        if isinstance(other, Produk):
            return self.harga < other.harga
        return NotImplemented

    def __gt__(self, other):
        """Memeriksa apakah harga produk lebih mahal (>)."""
        if isinstance(other, Produk):
            return self.harga > other.harga
        return NotImplemented

# --- Instansiasi dan Pengujian ---

# 1. Membuat 3 Object dengan data berbeda
produk1 = Produk("Smartphone A", 3500000)
produk2 = Produk("Laptop B", 8500000)
produk3 = Produk("Earbuds C", 1200000)
produk4 = Produk("Smartphone X (Promo)", 3500000) # Untuk tes __eq__

print("=== Daftar Produk ===")
print(produk1)
print(produk2)
print(produk3)
print("-" * 30)

# 2. Pengujian Perbandingan
print("=== Hasil Pengujian Perbandingan ===")

# Uji Lebih Mahal (__gt__)
print(f"Apakah {produk2.nama} lebih mahal dari {produk1.nama}? -> {produk2 > produk1}")

# Uji Lebih Murah (__lt__)
print(f"Apakah {produk3.nama} lebih murah dari {produk1.nama}? -> {produk3 < produk1}")

# Uji Sama Dengan (__eq__)
print(f"Apakah harga {produk1.nama} sama dengan {produk4.nama}? -> {produk1 == produk4}")

# Uji Tambahan
print(f"Apakah {produk3.nama} lebih mahal dari {produk2.nama}? -> {produk3 > produk2}")