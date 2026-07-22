from abc import ABC, abstractmethod
from sqlite3.dbapi2 import SQLITE_ANALYZE
class InvalidInputError(Exception):
    pass
class DataNotFoundError(Exception):
    pass
class KoneksiDatabase(ABC):
    @abstractmethod
    def simpan_data(self, data):
        pass
    @abstractmethod
    def ambil_data(self):
        pass
class DataBaseInMemory(KoneksiDatabase):
    def __init__(self):
        self.__db = []
    def simpan_data(self, mahasiswa):
        self.__db[mahasiswa.nim] = mahasiswa
    def ambil_data(self):
        return self.__db
    def cari_by_nim(self, nim):
        return self.__db.get(nim)
class user:
    def __init__(self, nama_lengkap: str):
        self.nama_lengkap = nama_lengkap
    @property
    def nama_lengkap(self):
        return self.nama_lengkap
class Mahasiswa(user):
    def __init__(self, nama: str, nim: str, semester: int, prodi: str, tujuan:str, alasan: str, waktu_keluar:  str):
        super().__init__(nama)
        self.__nim = nim
        self.__semester = semester
        self.__prodi = prodi
        self.__tujuan = tujuan
        self.__alasan = alasan
        self.__waktu_keluar = waktu_keluar
        self.__keluar_count = 1
        self.__status_izin = "Pending"
    @property
    def nim(self):
        return self.__nim
    @property
    def semester(self):
        return self.__semester
    @property
    def prodi(self):
        return self.__prodi
    @property
    def tujuan(self):
        return self.__tujuan
    @tujuan.setter
    def tujuan(self, val):
        self.__tujuan = val
    @property
    def alasan(self):
        return self.__alasan
    @property
    def waktu_keluar(self):
        return self.__waktu_keluar
    @waktu_keluar.setter
    def waktu_keluar(self, val):
        self.__waktu_keluar = val
    @property
    def keluar_count(self):
        return self.__keluar_count
    @property
    def status_izin(self):
        return self.status_izin
    @status_izin.setter
    def status_izin(self, status):
        self.__status_izin = status
    def catat_keluar(self):
        self.__keluar_count += 1
    def __str__(self):
        return (
            f"\n========== DATA E-PERIZINAN MAHASISWA=========="
            f"Nama          : {self.nama_lengkap}"
            f"NIM           : {self.__nim}"
            f"Semester      : {self.__semester}"
            f"Prodi         : {self.__prodi}"
            f"Tujuan        : {self.__tujuan}"
            f"Alasan        : {self.__alasan}"
            f"Waktu Keluar  : {self.__waktu_keluar}"
            f"Keluar Count  : {self.__keluar_count}"
            f"Status Izin   : {self.__status_izin}"
        )
class StafDeKaPe(user):
    def __init__(self, nama: str, id_staf: str):
        super().__init__(nama)
        self.__id_staf = id_staf
    def proses_pesan_masuk(self, mhs: mahasiswa, setuju: bool):
        if setuju:
            mhs.status_izin = "Disetujui"
            print(f"[AKSES STAF] Izin Mahasiswa {mhs.nama_lengkap}(NIM:{mhs.__nim}) Telah Disetujui")
        else:
            mhs.status_izin = "Ditolak"
            print(f"[AKSES STAF] Izin Mahasiswa {mhs.nama_lengkap}(NIM:{mhs.__nim}) Telah Ditolak")
class SatpamGerbangKampus(user):
    def __init__(self, nama: str, id_satpam: str):
        super().__init__(nama)
        self.__id_satpam = id_satpam
    def verifikasi_kembali(self, mhs: mahasiswa):
        mhs.status_izin = "Sudah Kembali"
        print(f"[POS {self.__id_satpam}] Mahasiswa {mhs.nama_lengkap}(NIM:{mhs.__nim}) Terverifikasi dan Sudah Kembali")
class SistemPerizinan:
    @staticmethod
    def verifikasi_jam_malam(waktu_keluar: str)-> str:
        waktu = waktu_keluar.lower().strip()
        if waktu in ["pagi", "siang", "sore", "malam"]:
            return "Peringatan harus kembali paling lambat sebelum jam 22.00 PM"
        else:
            return "Peringatan: Anda Telah Melanggar Peraturan Kampus Silahkan Melapor Ke Pihak DKP"
    @staticmethod
    def parse_wa_command(command: str):
