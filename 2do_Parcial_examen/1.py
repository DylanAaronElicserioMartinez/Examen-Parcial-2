print(" ")#imprime un espacio en blanco
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")#imprime mi nombre completo con mi grado y grupo mas mi numero de control
print(" ")#imprime un espacio en blanco
print("Hola buenas tardes alumno me podria ayudar diciendome sus calificaciones de las siguientes materias Por favor y Gracias.")#Imprime en pantalla que ingresemos nuestra calificacion en la materia correspondiente
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
