from dao.dao_usuario import UsuarioDAO
from dao.dao_saldo import SaldoDAO


usuarios = UsuarioDAO()
saldos = SaldoDAO()

# Inicio de sesión
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

if usuarios.verificar_usuario(usuario, contraseña):
    print("¡Inicio de sesión exitoso!")

    while True:
        print("\n1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Actualizar saldo manualmente")
        print("4. Ver saldo actual")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            monto = float(input("Monto a ingresar: $ "))
            nuevo_saldo = saldos.ingresar(usuario, monto)
            print(f"Nuevo saldo: ${nuevo_saldo:.2f}")
        elif opcion == "2":
            monto = float(input("Monto a retirar: $ "))
            nuevo_saldo = saldos.retirar(usuario, monto)
            if nuevo_saldo is not None:
                print(f"Nuevo saldo: ${nuevo_saldo:.2f}")
            else:
                print("Fondos insuficientes.")
        elif opcion == "3":
            saldos.actualizar_saldo_interactivo(usuario)
        elif opcion == "4":
            actual = saldos.obtener_saldo(usuario)
            print(f"Tu saldo actual es: ${actual:.2f}")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

else:
    print("Usuario o contraseña incorrectos.")
