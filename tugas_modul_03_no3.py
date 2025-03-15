from abc import ABC, abstractmethod

# Membuat kelas abstrak untuk akun bank
class Account(ABC):
    def __init__(self, account_holder, balance, currency):
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency
    
    @abstractmethod
    def apply_interest(self):
        pass

    @abstractmethod
    def withdraw(self, amount, currency):
        pass

# Kelas BankAccount mengimplementasikan Account
class BankAccount(Account):
    exchange_rates = {
        ("USD", "EUR"): 0.91,
        ("EUR", "USD"): 1.10,
        ("USD", "IDR"): 15000,
        ("IDR", "USD"): 0.000067,
        ("EUR", "IDR"): 16500,
        ("IDR", "EUR"): 0.000061,
    }
    
    def convert_currency(self, amount, from_currency, to_currency):
        # Mengonversi mata uang dengan kurs tetap
        if from_currency == to_currency:
            return amount
        rate = self.exchange_rates.get((from_currency, to_currency), 1)
        return amount * rate
    
    def __add__(self, other):
        # Menambahkan saldo dari akun lain dengan konversi mata uang otomatis
        converted_amount = self.convert_currency(other.balance, other.currency, self.currency)
        self.balance += converted_amount
        return self
    
    def __sub__(self, amount):
        # Mengurangi saldo dengan pengecekan saldo cukup atau tidak
        if amount > self.balance:
            print("Low Balance Warning: Insufficient funds!")
        else:
            self.balance -= amount
        return self
    
    def apply_interest(self):
        # Menambahkan bunga berdasarkan saldo
        interest_rate = 0.02 if self.balance >= 5000 else 0.01
        self.balance += round(self.balance * interest_rate)
        print(f"Applying interest... New Balance = ${self.balance}")
    
    def withdraw(self, amount, currency):
        # Penarikan saldo dengan konversi mata uang otomatis
        converted_amount = self.convert_currency(amount, currency, self.currency)
        if converted_amount > self.balance:
            print("Insufficient balance for withdrawal!")
        else:
            self.balance -= converted_amount
        return self
    
    def __str__(self):
        return f"{self.account_holder}'s Account: Balance = {self.currency} {self.balance}"

# Contoh Skenario
arie = BankAccount("Arie", 5000, "USD")
leony = BankAccount("Leony", 1000, "EUR")

print(f"Arie's Account: Initial Balance = ${arie.balance}")
arie.apply_interest()
print(f"Arie's Account: New Balance = ${arie.balance}\n")

print(f"Leony's Account: Initial Balance = €{leony.balance}")
converted_amount = leony.convert_currency(leony.balance, "EUR", "USD")
print(f"Converted to USD: ${round(converted_amount)}")
leony.withdraw(1200, "USD")
print(f"Leony's Account: Balance remains at €{leony.balance}")
