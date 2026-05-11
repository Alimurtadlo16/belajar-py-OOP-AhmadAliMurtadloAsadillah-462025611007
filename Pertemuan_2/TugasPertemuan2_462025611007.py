#Pertemuan 2
class SepedaMotor:
    """
    Class untuk merepresentasikan objek dunia nyata: Sepeda Motor.
    Memenuhi kriteria Struktur Class dengan atribut dan metode yang benar.
    """
    def __init__(self, merk, model, kapasitas_mesin, warna):
        # Atribut instance
        self.merk = merk
        self.model = model
        self.kapasitas_mesin = kapasitas_mesin
        self.warna = warna
        self.is_mesin_menyala = False

    def nyalakan_mesin(self):
        self.is_mesin_menyala = True
        print(f"Mesin {self.merk} {self.model} sekarang menyala. Brumm!")

    def tampilkan_info(self):
        """
        Memenuhi kriteria Objek & Instansiasi: memanggil print attributes tanpa error.
        """
        status = "Menyala" if self.is_mesin_menyala else "Mati"
        print("="*30)
        print(f"Informasi Kendaraan:")
        print(f"Merk            : {self.merk}")
        print(f"Model           : {self.model}")
        print(f"Kapasitas Mesin : {self.kapasitas_mesin}cc")
        print(f"Warna           : {self.warna}")
        print(f"Status Mesin    : {status}")
        print("="*30)

def main():
    # Instansiasi Objek 1: Supra X 125 (Objek Unik 1)
    motor_harian = SepedaMotor("Honda", "Supra X 125", 125, "Hitam Merah")
    
    # Instansiasi Objek 2: Hasil Bore Up (Objek Unik 2 - Orisinalitas)
    motor_touring = SepedaMotor("Honda", "Supra X Modifikasi", 150, "Silver")

    # Memanggil metode untuk menampilkan atribut (Poin: Objek & Instansiasi)
    motor_harian.tampilkan_info()
    
    motor_touring.nyalakan_mesin()
    motor_touring.tampilkan_info()

if __name__ == "__main__":
    main()