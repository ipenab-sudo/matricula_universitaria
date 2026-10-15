nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >= 17:
    graduado = input("Usted esta graduado s/n: ")
    if graduado == "s":
        print(f"{nombre} al usted ser mayor de 17 y estar graduado puede matricular tecnicos o bachilleratos segun su preferencia")
    else:
        print(f"{nombre} al usted ser mayor de 17, pero no estar graduado solo puede matricular tecnicos")
else:
    print(f"{nombre} al usted ser menor de 17 solo puede matricular tecnicos")
