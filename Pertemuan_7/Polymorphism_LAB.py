class AlatPembayaran:
    def prosesBayar(self, nominal):
        print(f"Pembayaran sebesar {nominal} berhasil diproses.")

class KartuKredit(AlatPembayaran):
    def prosesBayar(self, nominal):
        biayaAdmin = nominal * 0.02
        totalBayar = nominal + biayaAdmin
        print(f"Pembayaran dengan Kartu Kredit sebesar {nominal} berhasil diproses.")
        print(f"Biaya admin: {biayaAdmin}, Total bayar: {totalBayar}")
        print("Transaksi Kartu Kredit berhasil.")

class EWallet(AlatPembayaran):
    def prosesBayar(self, nominal):
        diskon = nominal * 0.05
        totalBayar = nominal - diskon
        print(f"Pembayaran dengan E-Wallet sebesar {nominal} berhasil diproses.")
        print(f"Diskon: {diskon}, Total bayar: {totalBayar}")
        print("Transaksi E-Wallet berhasil.")

class QrisTanpaInheritance:
    def prosesBayar(self, nominal):
        print(f"Pembayaran dengan QRIS sebesar {nominal} berhasil diproses.")
        print("Transaksi QRIS berhasil.")
    
def jalankanTransaksi(objekPembayaran, nominal):
    objekPembayaran.prosesBayar(nominal)

if __name__ =="__main__":
    print("=== Polymorphism dengan Inheritance ===")
    dompetDigital = EWallet()
    kartuBCA = KartuKredit()
    qrisGojek = QrisTanpaInheritance()
    nominalTransaksi = 1000000
    print("\nTransaksi dengan Kartu Kredit:")
    print("1. Menguji objek Ewallet (child class): ")
    jalankanTransaksi(dompetDigital, nominalTransaksi)
    print("\n2. Menguji objek Kartu Kredit (child class): ")
    jalankanTransaksi(kartuBCA, nominalTransaksi)
    print("\n3. Menguji objek QRIS (tanpa inheritance): ")
    jalankanTransaksi(qrisGojek, nominalTransaksi)