class Karyawan:
    def __init__(self, nama, jabatan, gaji_pokok):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji_pokok = gaji_pokok

    # Instance Method 1: Menampilkan profil karyawan
    def tampilkan_profil(self):
        print(f"Nama: {self.nama} | Jabatan: {self.jabatan}")

    # Instance Method 2: Menghitung total gaji setelah bonus (mengolah atribut)
    def hitung_total_gaji(self, bonus):
        total = self.gaji_pokok + bonus
        print(f"Total Gaji {self.nama}: Rp{total}")

    # Static Method: Fungsi pendukung yang independen dari data objek
    @staticmethod
    def info_perusahaan():
        print("--- PT. Teknologi Masa Depan - Jakarta ---")

# --- Instansiasi dan Pengujian ---

# Memanggil Static Method melalui Class
Karyawan.info_perusahaan()

# Membuat 2 Object berbeda
karyawan1 = Karyawan("Andi", "Developer", 8000000)
karyawan2 = Karyawan("Budi", "Designer", 7000000)

# Menguji Objek 1 (Instance Methods)
karyawan1.tampilkan_profil()
karyawan1.hitung_total_gaji(500000)

print("-" * 30)

# Menguji Objek 2 (Instance Methods)
karyawan2.tampilkan_profil()
karyawan2.hitung_total_gaji(400000)

print("-" * 30)

# Memanggil Static Method melalui salah satu objek
karyawan2.info_perusahaan()