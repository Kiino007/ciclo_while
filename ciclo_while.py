# ciclo while

# while condicion:
    # bloque de codigo a repetir

# Diferencias con for
#  for                                                  while
#  se requiere una secuencia                            no por que depende de una condicion 
# cuando necesito saber cuantas veces se va ejecutar    cuando no necesito saber cuantas veces se tiene que ejecutar
# control automatico con rango o secuencua              requiere controlar la condicion
# recorrer listas, rangos o matrices                    validacion, simulaciones, menus dinamicos.



# definir una variable que lleve el control del ciclo

# numero = 1

# while numero <= 5: #condicion para iterar n veces.....
#     print(numero)
#     numero += 1  #no se puede poner antes de la linea del print por que imprimira numeros 1 infinitas veces



# contamos hacia atras 
  
# numero = 10

# while numero >= 1:
#     print(numero)
#     numero -= 1

# crear un programa que sume 

# suma = 0

# numero = int(input("Ingresa un numero o pulsa 0 para salir:  "))

# while numero != 0:
#     suma += numero
#     numero = int(input("Ingresa un numero o pulsa 0 para salir:  "))

# print(f"La suma total es: {suma}")

#condiciones dinamicas: 
#Son aleatorias, y pueden cambiar con la ejecucion del codigo

#simulacion basada en una condicion externa.
# Simular el crecimiento de una poblacion hasta que alcance un limite. 

# poblacion = 1000
# limite = 5000
# tasa_crecimiento = 1.1
# anio = 1

# while poblacion < limite:
#     print(f"En el año {anio} la poblacion actual: {poblacion}")
#     poblacion = int(poblacion * tasa_crecimiento)
#     anio += 1

# print(f"Poblacion final alcanzada: {poblacion}")
