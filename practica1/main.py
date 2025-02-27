import os
import time

def clear_screen():
    """Limpia la pantalla en Windows."""
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    """Muestra el menú de opciones."""
    clear_screen()
    print("=" * 40)
    print("     🌍 Programa en Python 🚀     ")
    print("=" * 40)
    print("1️⃣  Mostrar un mensaje")
    print("2️⃣  Contar hasta 5")
    print("3️⃣  Mostrar la hora actual")
    print("4️⃣  Salir")
    print("=" * 40)

def mostrar_mensaje():
    """Muestra un mensaje en pantalla."""
    print("\n✨ ¡Bienvenido a este programa interactivo! ✨\n")

def contar():
    """Cuenta del 1 al 5 con una animación."""
    print("\nContando: ", end="", flush=True)
    for i in range(1, 6):
        print(i, end=" ", flush=True)
        time.sleep(0.5)
    print("\n✅ Listo!")

def mostrar_hora():
    """Muestra la hora actual."""
    from datetime import datetime
    ahora = datetime.now().strftime("%H:%M:%S")
    print(f"\n⏰ La hora actual es: {ahora}")

def main():
    while True:
        menu()
        opcion = input("\nElige una opción (1-4): ")

        if opcion == "1":
            mostrar_mensaje()
        elif opcion == "2":
            contar()
        elif opcion == "3":
            mostrar_hora()
        elif opcion == "4":
            print("\n👋 Saliendo del programa...")
            time.sleep(1)
            break
        else:
            print("\n❌ Opción no válida, intenta de nuevo.")

        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
