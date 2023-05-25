def menu():
    print("     =>MENU<=","\n","1-Sumar uno o mas numeros","\n","2-Restar uno o mas numeros","\n","3-Multiplicar uno o mas numeros\n","4-Dividir un numero\n","5-Salir del programa")
#comienza el programa
while exit != 1:
    menu()
    
    #el usuario ingresa la opcion que desea
    try:
        opcion = int(input("Eliga el valor correspondiente a la opcion deseada=>"))
    except ValueError:
        print("Valor incorrecto")
        continue

    #Si la opcion es 1 entra en la suma
    if opcion == 1:
        salir_suma = int
        while salir_suma != 1:
            try:        
                num1_suma = int(input("Ingrese un numero:=>"))
                num2_suma = int(input("Ingrese la cantidad que desea sumar:=>"))
                result_suma = num1_suma + num2_suma
                print("RESULTADO=>",result_suma)
                opcion_user = 0
                while opcion_user != 2:
                    try:
                        opcion_user = int(input("Desea agregar otro numero para suamrlo?: \n 1-Si \n 2-No \n =>"))
                        if opcion_user == 1:
                            num3_suma = int(input("Ingrese un numero a sumar:=>"))
                            result_suma = result_suma + num3_suma
                            print("RESULTADO=>",result_suma)
                        salir_suma = int(input("Desea salir de la suma?: \n 1-Si \n 2-No \n =>"))
                    except ValueError:
                        print("Valor incorrecto")
                        opcion_user = 0
                        continue
            except ValueError:
                print("Valor incorrecto")
                continue

    #Si la opcion es 2 entra en la resta
    if opcion == 2:
        salir_resta = int
        while salir_resta != 1:
            try:
                num1_resta = int(input("Ingrese un numero:=>"))
                num2_resta = int(input("Ingrese la cantidad que desea restar:=>"))
                result_resta = num1_resta - num2_resta
                print("RESULTADO=>",result_resta)
                opcion_user = 0
                while opcion_user != 2:
                    try:
                        opcion_user = int(input("Desea agregar otro numero para restarlo?: \n 1-Si \n 2-No \n =>"))
                        if opcion_user == 1:
                            num3_resta = int(input("Ingrese un numero a restar:=>"))
                            result_resta = result_resta - num3_resta
                            print("RESULTADO=>",result_resta)
                        salir_resta = int(input("Desea salir de la resta?: \n 1-Si \n 2-No \n =>"))
                    except ValueError:
                        print("Valor incorrecto")
                        opcion_user = 0
                        continue
            except ValueError:
                print("Valor incorrecto")
                continue

    #si la opcion es 5, sale del programa
    if opcion == 5:
        break

    #aqui finaliza en programa y pregunta si desea repetir el programa
    try:
        exit = int(input("Desea salir del programa?: \n 1-Si \n 2-No \n=>"))
    except ValueError:
        print("Valor incorrecto")
        continue