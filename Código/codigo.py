print("Ejercicio propuesto por el docente:")
num = [x for x in range (1, 11)]
print(f"La lista por comprensión es: {num}")
print(" ")

print("///////////////////////////////////////////////////")
#Ingresando número por teclado

print("****Sr. Usuario, a través de este software podrás visualizar una lista por comprensión con los números que usted desee****")
print(" ")
z = int(input("Ingrese desde qué número quieres que vaya la lista: "))
m = int(input("Ingrese hasta qué número quiere que vaya la lista: "))
m+=1
print(" ")

num = [x for x in range(z, m)]
print(f"Su lista por comprensión es la siguiente: {num}")