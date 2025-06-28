class SaldoDAO:
    def __init__(self):
        self.saldos = {
            "admin": 1000.0,
            "duran": 750.0
        }

    def obtener_saldo(self, usuario):
        return self.saldos.get(usuario, None)

    def ingresar(self, usuario, monto):
        if usuario in self.saldos:
            self.saldos[usuario] += monto
            return self.saldos[usuario]
        return None

    def retirar(self, usuario, monto):
        if usuario in self.saldos and self.saldos[usuario] >= monto:
            self.saldos[usuario] -= monto
            return self.saldos[usuario]
        return None

    def actualizar_saldo_interactivo(self, usuario):
        saldo_actual = self.obtener_saldo(usuario)
        if saldo_actual is None:
            print("Usuario sin cuenta.")
            return

        while True:
            try:
                cantidad = input("Ingresa la cantidad a agregar o restar (usa '-' para restar): $ ")
                cantidad = float(cantidad)
                saldo_actual += cantidad
                self.saldos[usuario] = saldo_actual
                print(f"Saldo actualizado: ${saldo_actual:.2f}")
                return saldo_actual
            except ValueError:
                print("Por favor, ingresa un valor numérico válido.")
