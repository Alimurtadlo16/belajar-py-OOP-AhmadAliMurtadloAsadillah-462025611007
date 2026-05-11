class Bank:
    nama = ''
    saldo = 0

    def jika_saldo(self):
        print(f"Halo {self.nama}, Saldo anda Adalah {self.saldo}")

    def __init__(self, nama, saldo) -> None:
        self.nama = nama
        self.saldo = saldo
        if self.saldo < 0:
            print("Saldo tidak boleh negatif")
        print(f"Halo {self.nama}, Saldo anda Adalah {self.saldo}")

    def __str__(self) -> str:
        return f"Halo {self.nama}, Saldo anda Adalah {self.saldo}"
    
    def __eq__(self, value: object) -> bool:
        return self.nama == value.nama and self.saldo == value.saldo
    
    def __le__(self, other):
        return self.saldo <= other.saldo
    
bank1 = Bank('John Doe', 100000)
bank2 = Bank('Jane Doe', 500000)
print(bank1 == bank2) 