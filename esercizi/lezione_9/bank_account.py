class ContoBancario:
    
    total_accounts = 0

    def __init__(self, iban, saldo, nome) -> None:
        self.iban = iban
        self.saldo = saldo
        self.nome = nome

        ContoBancario.total_accounts += 1

    def deposito(self, importo):
        self.saldo += importo
        print(f'{importo} depositato. Il nuovo saldo è di {self.saldo}')

    def prelievo(self, importo):
        self.saldo -= importo
        print(f'{importo} prelevato. Il nuovo saldo è di {self.saldo}')


    @classmethod
    def get_total_accounts(cls):
        print(f'Account totali creati: {cls.total_accounts}')

    @staticmethod
    def valida_account(iban):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print("Iban valido")
            return True
        else:
            print("Iban non valido")
            return False
        
account1 = ContoBancario(1234567890, 0, 'Alice')
account2 = ContoBancario(9876543210, 1000, 'Bob')

account1.deposito(500)
account2.prelievo(200)

account1.deposito(200)
account2.prelievo(150)

ContoBancario.get_total_accounts()

ContoBancario.valida_account(1234567890)
ContoBancario.valida_account('12345ABCD')

def valida_account(iban):
    if isinstance(iban, int) and len(str(iban)) == 10:
        print("Iban valido")
        return True
    else:
        print("Iban non valido")
        return False
    

valida_account(iban=123821413)