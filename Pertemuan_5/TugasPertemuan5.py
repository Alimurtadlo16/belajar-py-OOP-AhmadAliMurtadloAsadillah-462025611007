class DompetDigital:
    def __init__(self, pemilik, data_rahasia, saldo, pin) -> None:
        self.__pemilik = pemilik
        self.__data_rahasia = data_rahasia
        self.__saldo = saldo
        self.pin = pin

    def get_pemilik(self):
        return self.__pemilik
    
    def get_data_rahasia(self):
        return self.__data_rahasia
    
    def cek_saldo(self, pin_input):
        if pin_input == self.pin:
            print(f"Saldo {self.__pemilik}: Rp: {self.__saldo}")
        else:
            print("PIN salah. Akses ditolak.")

    def tarik_tunai(self, jumlah, pin_input):
        if pin_input != self.pin:
            print("PIN salah. Akses ditolak.")
            return  
        
        if jumlah > self.__saldo:
            print("Saldo tidak cukup untuk melakukan penarikan.")
        elif jumlah <= 0:
            print("Jumlah penarikan harus lebih besar dari 0.")
        else:
            self.__saldo -= jumlah
            print(f"Penarikan berhasil. Saldo baru: Rp: {self.__saldo}")

dompet_saya = DompetDigital("Alice", "Data Rahasia Alice", 1000000, "4321")
print("Pemilik Dompet:", dompet_saya.get_pemilik())

print("\n--- Percobaan dengan PIN salah ---")
dompet_saya.cek_saldo("0000")
dompet_saya.tarik_tunai(500000, "0000")

print("\n--- Percobaan dengan PIN benar ---")
dompet_saya.cek_saldo("4321")  
dompet_saya.tarik_tunai(500000, "4321")
dompet_saya.cek_saldo("4321")