class Pabrik_Mobil:
    def __init__(self, nama, tahun):
        self.nama = nama
        self.tahun = tahun

    def info(self):
        print(f"Nama Mobil: {self.nama}, Tahun: {self.tahun}")
mobil1 = Pabrik_Mobil("Toyota", 2020)
mobil2 = Pabrik_Mobil("Honda", 2021)
mobil3 = Pabrik_Mobil("Suzuki", 2019)
mobil1.info()
mobil2.info()
mobil3.info()