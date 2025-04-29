class Bank:
    # Class variable 
    bank_name = "💳 National Beero Bank"

    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def show_details(self):
        print("🏦 Account Info:")
        print(f"👤 Account Holder: {self.account_holder}")
        print(f"💵 Balance: ${self.balance}")
        print(f"🏛️ Bank Name: {Bank.bank_name}")

    @classmethod
    def change_bank_name(cls, name: str):
        print(f"🔄 Bank ka naam change ho gaya! 🎉 Naya naam: {name}")
        cls.bank_name = name


acc1 = Bank("HIKMAT KHAN", 5000)
acc2 = Bank("RAES KHAN", 10000)

acc1.show_details()
acc2.show_details()

Bank.change_bank_name("🏦 Beero Global Finance")

acc1.show_details()
acc2.show_details()
