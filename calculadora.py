def menu():
    print("     =>MENU<=","\n","1-Sumar uno o mas numeros","\n","2-Restar uno o mas numeros","\n","3-Multiplicar uno o mas numeros\n","4-Dividir un numero\n","5-Salir del programa")
#hola
#comienza el programa
while exit != 1:
    menu()

    #el usuario ingresa la opcion que desea
    try:
        opcion = int(input("Eliga el valor correspondiente a la opcion deseada=>"))
    except ValueError:
        print("Valor incorrecto")
    
    #si la opcion es 5, sale del programa
    if opcion == 5:
        break

    #aqui finaliza en programa y pregunta si desea repetir el programa
    try:
        exit = int(input("Desea salir del programa?: \n 1-Si \n 2-No \n=>"))
    except ValueError:
        print("Valor incorrecto")