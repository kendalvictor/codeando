class CuentaCorriente:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def transferir(self, cuenta, monto):
        if self.saldo - monto < 0:
            print('No procede')
        else:
            cuenta.saldo += monto
            self.saldo -= monto


keiko = CuentaCorriente(999999999)
AG = CuentaCorriente(2345)

AG.depositar(623)
keiko.transferir(AG, 8239)

print(AG.saldo)
print(keiko.saldo)
