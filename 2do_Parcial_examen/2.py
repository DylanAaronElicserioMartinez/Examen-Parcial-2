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