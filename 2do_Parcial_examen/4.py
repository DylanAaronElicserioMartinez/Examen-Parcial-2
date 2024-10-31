print(" ")#imprime un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime mi nombre completo con mi grado y grupo mas mi numero de control
print(" ")#imprime un espacio en blanco
print("Buenas tardes me podria dar su informacion personal gracias.")#nos pide que ingresemos nuestra informacion personal
N=input("Ingresa tu nombre:")#nos pide ingresar nuestro nombre
E=input("Ingresa tu edad:")#nos pide ingresar nuestra edad
D=input("Ingresa tu direccion(País):")#nos pide ingresar nuestra direccion o pais
T=input("Ingresa tu numero de telefono:")#nos pide ingresar nuestro numer de telefono
Lista={#creamos una biblioteca
    "Nombre" : N,
    "Edad" : E,
    "Direccion" : D,
    "Telefono" : T
}
print(" ")#imprime un espacio en blanco
print("El usuario se llama:")#impriime en la pantalla nuestro nombre
print(Lista["Nombre"])
print("La edad de",N,"es:")#impriime en la pantalla nuestra edad
print(Lista["Edad"])
print(N,"vive en:")#impriime en la pantalla nuestra direccion
print(Lista["Direccion"])
print("El numero de telefono de",N,"es:")#impriime en la pantalla nuestro numero de telefono
print(Lista["Telefono"])