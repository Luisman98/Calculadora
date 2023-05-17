def menu():
    print("     ...:MENU:...","\n","1-Sumar uno o mas numeros","\n","2-Restar uno o mas numeros","\n","3-Multiplicar uno o mas numeros\n","4-Dividir un numero\n","5-Salir del programa")

exit = 0
while exit == 0:
    menu()
    try:
        opcion = int(input("Eliga el valor correspondiente a la opcion deseada=>"))
    except ValueError:
        print("Valor incorrecto")
    