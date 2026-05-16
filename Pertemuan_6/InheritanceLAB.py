"""
Nama    : Ahmad Ali Murtadlo Asadillah
NIM     : 462025611007
Matkul  : OOP
"""
class Civitas:
    def __init__(self, nama):
        self.nama   = nama
        print(class_nama    := f"[{self.__class__.__name__}]", f"Inisialisasi Civitas untuk {self.nama}")
    
    def info(self):
        print(f"Nama Civitas    : {self.nama}")

class Pengajar(Civitas):
    def __init__(self, nama, bidang_ilmu, **kwarg):
        super().__init__(nama   = nama, **kwarg)
        self.bidang_ilmu    = bidang_ilmu
        print(f"[{self.__class__.__name__}] Inisialisasi pengajar bidang {self.bidang_ilmu}")
    
    def info(self):
        super().info()
        print(f"Bidang ilmu :{self.bidang_ilmu}")

class Organisator(Civitas):
    def __init__(self, nama, lembaga, **kwargs):
        super().__init__(nama=nama, **kwargs)
        self.lembaga = lembaga
        print(f"[{self.__class__.__name__}] Inisialisasi Organisator di {self.lembaga}")

    def info(self):
        super().info()
        print(f"Lembaga/Unit : {self.lembaga}")

class DosenMasyarakat(Pengajar, Organisator):
    def __init__(self, nama, bidang_ilmu, lembaga, tugas_khusus):
        print("\n--- Memulai Inisialisasi Objek DosenMasyarakat (Diamond Problem) ---")
        super().__init__(nama=nama, bidang_ilmu=bidang_ilmu, lembaga=lembaga)
        self.tugas_khusus = tugas_khusus
        print(f"[{self.__class__.__name__}] Inisialisasi DosenMasyarakat dengan tugas: {self.tugas_khusus}")

    def info(self):
        print("\n--- Menampilkan Informasi Lengkap (Resolusi Diamond Problem) ---")
        super().info()
        print(f"Tugas Khusus : {self.tugas_khusus}")

if __name__ == "__main__":
    dosen_abdi = DosenMasyarakat(
        nama="Ust. Wahid Alfaridsi", 
        bidang_ilmu="OOP", 
        lembaga="TI UNIDA Gontor",
        tugas_khusus="Pengabdian Masyarakat Berbasis Teknologi"
    )
    dosen_abdi.info()
    print("\n--- Urutan Method Resolution Order (MRO) ---")
    for i, urutan in enumerate(DosenMasyarakat.__mro__, 1):
        print(f"{i}. {urutan}")