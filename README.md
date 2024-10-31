# Examen-Parcial-2
Examen

#Codigo 1 

print(" ")#imprime un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#imprime un espacio en blanco

print("Hola buenas tardes alumno me podria ayudar diciendome sus calificaciones de las siguientes materias Por favor y Gracias.")#Imprime en pantalla que ingresemos nuestra calificacion
en la materia correspondiente

M = int(input("Que Calificacion saco en matematicas:"))#nos pide que ingresemos la calificacion de matematicas

F = int(input("Que Calificacion saco en física:"))#nos pide que ingresemos la calificacion de física

Q = int(input("Que Calificacion saco en química:"))#nos pide que ingresemos la calificacion de química

H = int(input("Que Calificacion saco en historia:"))#nos pide que ingresemos la calificacion de historia

L = int(input("Que Calificacion saco en lengua:"))#nos pide que ingresemos la calificaciuon de lengua

print(" ")#imprime un espacio en blanco

print("Estas son todas tus materias.")#imprime en la pantalla un mensaje de texto

Mate = ["Matematicas:",M, "Física:",F, "Química:",Q, "Historia:",H, "Lengua:",L]#creamos una lista llamada mate donde estan las materias y donde ingresamos nuestras caificaciones

print(Mate)#imprime en la pantalla la lista

print("Ahora vamos a quitar de la lista las materias que no aprovaste y solo dejaremos las materias que  has aprovado.")#imprime en la pantalla un mensaje de texto

if 6>M:#nos indica que si la calificacion es menor a 6 se borrara de la lista

    Mate.pop(0)#borrara de la lista el valor asignado
    
elif 6>F:#nos indica que si la calificacion es menor a 6 se borrara de la lista

    Mate.pop(1)#borrara de la lista el valor asignado
    
elif 6>Q:#nos indica que si la calificacion es menor a 6 se borrara de la lista

    Mate.pop(2)#borrara de la lista el valor asignado
    
elif 6>H:#nos indica que si la calificacion es menor a 6 se borrara de la lista

    Mate.pop(3)#borrara de la lista el valor asignado
    
elif 6>L:#nos indica que si la calificacion es menor a 6 se borrara de la lista

    Mate.pop(4)#borrara de la lista el valor asignado
    
print(Mate)#imprime la lista

![image](https://github.com/user-attachments/assets/ee5afbe1-bd28-4179-9ea5-ea77173953ec)

![image](https://github.com/user-attachments/assets/a4cbf50b-9ac0-4fa2-9e6e-d1cbb29bced9)

#Codigo 2

print(" ")#imprime un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#imprime un espacio en blanco

M1=int(input("Ingresa la calificacion de la unidad 1 de matematicas:"))#nos pide que ingresemos la calificacion de matematicas de la primera unidad

M2=int(input("Ingresa la calificacion de la unidad 2 de matematicas:"))#nos pide que ingresemos la calificacion de matematicas de la segunda unidad

M3=int(input("Ingresa la calificacion de la unidad 3 de matematicas:"))#nos pide que ingresemos la calificacion de matematicas de la tercera unidad

F1=int(input("Ingresa la calificacion de la unidad 1 de Física:"))#nos pide que ingresemos la calificacion de física de la primera unidad

F2=int(input("Ingresa la calificacion de la unidad 2 de Física:"))#nos pide que ingresemos la calificacion de física de la segunda unidad

F3=int(input("Ingresa la calificacion de la unidad 3 de Física:"))#nos pide que ingresemos la calificacion de física de la tercera unidad

Q1=int(input("Ingresa la calificacion de la unidad 1 de Química:"))#nos pide que ingresemos la calificacion de química de la primera unidad

Q2=int(input("Ingresa la calificacion de la unidad 2 de Química:"))#nos pide que ingresemos la calificacion de química de la segunda unidad

Q3=int(input("Ingresa la calificacion de la unidad 3 de Química:"))#nos pide que ingresemos la calificacion de química de la tercera unidad

Materias = {#creamos una lista llamada mate donde estan las materias y donde ingresamos nuestras caificaciones

    "Matematicas I" : M1,
    
    "Matematicas II" : M2,
    
    "Matematicas III" : M3,
    
    "Física I" : F1,
    
    "Física II" : F2,
    
    "Física III" : F3,
    
    "Química I" : Q1,
    
    "Química II" : Q2,
    
    "Química III" : Q3,
}

print(Materias)#imprime la biblioteca

print(" ")#imprime un espacio en blanco

print("Ahora vamos a ver el promedeio de cada materia.")#imoprime en la pantalla que vamos a sacar el promedio de cada calificacion

Promedio1 = (M1+M2+M3)/3#sacamos el promedio de la materia 

Promedio2 = (F1+F2+F3)/3#sacamos el promedio de la materia 

Promedio3 = (Q1+Q2+Q3)/3#sacamos el promedio de la materia 

print("Este es el promedio de matematicas",Promedio1)#imprimimos en la pantalla el nombre de la materia con su promedio

print("Este es el promedio de Física",Promedio2)#imprimimos en la pantalla el nombre de la materia con su promedio

print("Este es el promedio de Química",Promedio3)#imprimimos en la pantalla el nombre de la materia con su promedio

![image](https://github.com/user-attachments/assets/eeb65174-7cc9-4e4e-bd34-60337e93aebc)

![image](https://github.com/user-attachments/assets/37aa9fca-ac9a-426d-800c-4fefc6aa13c5)

#Codigo 3

print(" ")#imprime un espacio en blanco

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime mi nombre completo con mi grado y grupo mas mi numero de control

print(" ")#imprime un espacio en blanco

print("Hola buenas tardes me podria dar sus calificaciones de cada materia a continuacion.")#Imprime en pantalla que ingresemos nuestra calificacion en la materia correspondiente

M=input("Porfavor Ingrese la calificacion que saco en matematicas:")#nos pide que ingresemos la calificacion de matematicas

F=input("Porfavor Ingrese la calificacion que saco en física:")#nos pide que ingresemos la calificacion de física

Q=input("Porfavor Ingrese la calificacion que saco en química:")#nos pide que ingresemos la calificacion de química

H=input("Porfavor Ingrese la calificacion que saco en historia:")#nos pide que ingresemos la calificacion de historia

L=input("Porfavor Ingrese la calificacion que saco en lengua:")#nos pide que ingresemos la calificaciuon de lengua

Mate = ["Matematicas:",M, "Física:",F, "Química:",Q, "Historia:",H, "Lengua:",L]#creamos una lista llamada mate donde estan las materias y donde ingresamos nuestras caificaciones

print("A continuacion le mostrare la materia con su calificacion respectivamente.")#imprime un mensaje de texto

print(Mate)#imprime en la pantalla la lista 

![image](https://github.com/user-attachments/assets/0ced1867-eac0-4884-9621-eebeb7c2b8e9)

![image](https://github.com/user-attachments/assets/28b41078-be92-4a73-b37f-08f82db47e0c)

#Codigo 4

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

![image](https://github.com/user-attachments/assets/99a2a507-5f7a-4bfe-b984-1440375c1578)

![image](https://github.com/user-attachments/assets/25191e3f-dd21-4b2f-bec2-5dc4c6d993ef)

