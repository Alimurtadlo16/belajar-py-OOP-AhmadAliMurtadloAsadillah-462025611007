class bank:
    __nama = ''
    __rekening = ""
    __saldo = 0
    __pin = ""

    def __init__(self, nama, rekening, saldo, pin: ""):
        self.__nama = nama
        self.__rekening = rekening
        self.__saldo = saldo
        self.__pin = pin

    def get_nama(self):
        return self.__nama
    
    def get_rekening(self):
        return self.__rekening
    
    def get_saldo(self):
        return self.__saldo
    
    def cek_saldo(self, pin):
        if pin != self.__pin:
            print("Pin salah!")
            return
        print(f"Halo {self.__nama}, Saldo anda Adalah {self.__saldo}")
        
    def topup_saldo(self, jumlah, pin):
        if pin != self.__pin:
            print("Pin salah!")
            return
        self.__saldo += jumlah
        print(f"Halo {self.__nama}, Saldo anda Adalah {self.__saldo}")
    
    def get_pin(self):
        return self.__pin
    
    def withdraw_saldo(self, jumlah, pin):
        if pin != self.__pin:
            print("Pin salah!")
            return
        if jumlah > self.__saldo:
            print("Saldo tidak cukup!")
            return
        self.__saldo -= jumlah
        print(f"Halo {self.__nama}, Saldo anda Adalah {self.__saldo}")
    
bank1 = bank("John Doe", "1234567890", 100000, "1234")
bank1.cek_saldo("1234")
bank1.topup_saldo(50000, "1234")
bank2 = bank("Jane Doe", "0987654321", 500000, "4321")
bank2.cek_saldo("4321")
bank2.withdraw_saldo(100000, "4321")
bank3 = bank("John Jack", "1234567890", 100000, "1234")
bank3.cek_saldo("1234")
bank3.withdraw_saldo(50000, "1234")