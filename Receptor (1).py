from operator import xor
import random
from sympy import Matrix
import numpy as np


separador = " "  

diccionario_encryt = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
            '0':26, '1': 27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33, '8':34, '9':35, '.': 36, ',': 37, ':': 38, '?': 39 , ' ': 40}

diccionario_decrypt = {'0' : 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E', '5': 'F', '6': 'G', '7': 'H', '8': 'I', '9': 'J', '10': 'K', '11': 'L', '12': 'M',
            '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z', '26': '0',
            '27': '1', '28': '2', '29': '3', '30': '4', '31': '5', '32' : '6', '33' : '7', '34' : '8', '35' : '9', '36' : '.', '37' : ',', '38' : ':', '39' : '?', '40' : ' '}


#------------------------Funciones------------------# 
def ascii_a_binario(letra):
    # Extraer su valor entero
    valor = ord(letra)
    # Convertirlo a binario
    return "{0:08b}".format(valor)

def binario_a_ascii(binario):
    # Convertir binario a decimal
    valor = int(binario, 2)
    # Convertir el decimal a su representación ASCII
    return chr(valor)

def texto_a_binario(texto):
    texto_binario = ""  # El resultado
    contador = 0
    for letra in texto:
        texto_binario += ascii_a_binario(letra)
        # Agregar un espacio entre binarios, excepto si es el último carácter
        if contador + 1 < len(texto):
            texto_binario += separador
        contador += 1
    return texto_binario

def binario_a_texto(texto_binario):
    texto_plano = ""
    for binario in texto_binario.split(separador):
        texto_plano += binario_a_ascii(binario)
    return texto_plano
	
def binario_a_decimal(binario):
    posicion = 0
    decimal = 0
    # Invertir la cadena porque debemos recorrerla de derecha a izquierda
    # https://parzibyte.me/blog/2019/06/26/invertir-cadena-python/
    binario = binario[::-1]
    for digito in binario:
        # Elevar 2 a la posición actual
        multiplicador = 2**posicion
        decimal += int(digito) * multiplicador
        posicion += 1
    return decimal

def descifrado_propio(txt):
	ultcar = txt[-1]
	if ultcar == '0':
		txt= txt.replace("0","m")
		txt= txt.replace("1","u")
		txt= txt.replace("2","r")
		txt= txt.replace("3","c")
		txt= txt.replace("4","i")
		txt= txt.replace("5","e")
		txt= txt.replace("6","l")
		txt= txt.replace("7","a")
		txt= txt.replace("8","g")
		txt= txt.replace("9","o")
	if ultcar == '1':
		txt= txt.replace("0","n")
		txt= txt.replace("1","e")
		txt= txt.replace("2","u")
		txt= txt.replace("3","m")
		txt= txt.replace("4","a")
		txt= txt.replace("5","t")
		txt= txt.replace("6","i")
		txt= txt.replace("7","c")
		txt= txt.replace("8","o")
		txt= txt.replace("9","s")
	if ultcar == '2':
		txt= txt.replace("0","e")
		txt= txt.replace("1","u")
		txt= txt.replace("2","c")
		txt= txt.replace("3","a")
		txt= txt.replace("4","l")
		txt= txt.replace("5","i")
		txt= txt.replace("6","p")
		txt= txt.replace("7","t")
		txt= txt.replace("8","o")
		txt= txt.replace("9","s")
	final_str = txt[:-1] 
	return (final_str)

def xor_5(num1,num2,num3,num4,num5):
    a = xor(num1,num2)
    b = xor(a,num3)
    c = xor(b,num4)
    d = xor(c,num5)
    return (d)

def xor_3(num1,num2,num3):
    a = xor(num1,num2)
    b = xor(a,num3)
    return (b)

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario

def decodificacion(mensaje_a_decodificar):
	arreglo = mensaje_a_decodificar.split()
	salida = ""
	for index, value in enumerate(arreglo):
		letra = arreglo[index]
		p1 = int(letra[0])
		p2 = int(letra[1])
		d1 = int(letra[2])
		p3 = int(letra[3])
		d2 = int(letra[4])
		d3 = int(letra[5])
		d4 = int(letra[6])
		p4 = int(letra[7])
		d5 = int(letra[8])
		d6 = int(letra[9])
		d7 = int(letra[10])
		prueba1= xor_5(d1,d2,d4,d5,d7)
		prueba2= xor_5(d1,d3,d4,d6,d7)
		prueba3= xor_3(d2,d3,d4)
		prueba4= xor_3(d5,d6,d7)
		if (p4 == prueba4):
			error = "0"
		else:
			error = "1"

		if (p3 == prueba3):
			error = error+"0"
		else:
			error = error+"1"

		if (p2 == prueba2):
			error = error+"0"
		else:
			error = error+"1"

		if (p1 == prueba1):
			error = error+"0"
		else:
			error = error+"1"

		posicion = binario_a_decimal(error)
		deco = [p1,p2,d1,p3,d2,d3,d4,p4,d5,d6,d7]
		poserror = int(letra[posicion -1])
		if (posicion != 0):
			if (poserror == 1):
				deco[posicion-1] = 0
			else:
				deco[posicion-1] = 1 
		
		dec =str(deco[10])+str(deco[9])+str(deco[8])+str(deco[6])+str(deco[5])+str(deco[4])+str(deco[2])+"0"

		valor = 0

		for num in range(len(dec)):
			if(int(dec[num]) == 1):
				valor = valor + (2**num)
		
		letraenbinario = decimal_a_binario(valor)

		letradeco = binario_a_ascii(letraenbinario)


					
		
		salida = salida + letradeco


	return salida

def descifrado_cesar(mensaje):

    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    decod_cesar = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':  
            decod_cesar += letra
            continue
        valor_letra = ord(letra) 
        alfabeto_a_usar = alfabeto 
        limite = 97  
        if letra.isupper(): 
            limite = 65
            alfabeto_a_usar = alfabeto_may

        posicion = (valor_letra - limite - 3) % longitud_alfabeto

        
        decod_cesar += alfabeto_a_usar[posicion]  #regresa los valores a letras y las concatena
    return (decod_cesar)

def descifrado_hill(message, key):


    plaintext = ''

    matrix_mensaje = []
    plaintext_temp = ''
    list_temp = []
    matrix_inversa = []
    matrix_mensaje = [message[i:i + len(key)] for i in range(0,
                      len(message), len(key))]

    # Se calcula la matriz inversa aplicando el modulo 41

    matrix_inversa = Matrix(key).inv_mod(41)

    # Se transforma en una matriz

    matrix_inversa = np.array(matrix_inversa)

    # Se pasan los elementos a float

    matrix_inversa = matrix_inversa.astype(float)

    # Para cada bloque

    for bloque in matrix_mensaje:

        # Se encripta el mensaje encriptado

        for i in range(0, len(bloque)):
            list_temp.append(diccionario_encryt[bloque[i]])

        # Se convierte a matriz

        matrix_encrypt = np.array(list_temp)

        # Se multiplica la matriz inversa por el bloque

        cifrado = np.matmul(matrix_inversa, matrix_encrypt)

        # Se le aplica a cada elemento el modulo 41

        cifrado = np.remainder(cifrado, 41).flatten()

        # Se desencripta el mensaje

        for i in range(0, len(cifrado)):
            plaintext_temp += diccionario_decrypt[str(int(cifrado[i]))]

        matrix_encrypt = []
        list_temp = []
    plaintext = plaintext_temp

    # Se eleminan las X procedentes de su addicion en la encriptacion para tener bloques del tamaño de la clave

    while plaintext[-1] == 'X':
        plaintext = plaintext.rstrip(plaintext[-1])

    return plaintext

#------------Mensaje recibido----------------#


print("""
    1)Cifrado Cesar
    2)Cifrado Hill
    3)Cifrado propio
    """)



while (True):
	tipo_cifrado = int(input("Ingrese el tipo de cifrado que quiere: "))
	if(tipo_cifrado <= 3):
		txt = input("Ingrese mensaje recibido: ") #------Mensaje que queremos enviar
		if (tipo_cifrado == 1):
			mensaje_cifrado_y_codificado = decodificacion(txt)
			cifrado = descifrado_cesar(mensaje_cifrado_y_codificado)
			print ("El mensaje decodificado: "," ".join(mensaje_cifrado_y_codificado)) 
		elif(tipo_cifrado == 2):
			mensaje_cifrado_y_codificado = decodificacion(txt)
			key =  [[13, 17], [10, 16]]
			cifrado = descifrado_hill(mensaje_cifrado_y_codificado,key)
			print ("El mensaje decodificado: "," ".join(mensaje_cifrado_y_codificado)) 

		elif(tipo_cifrado == 3):
			mensaje_cifrado_y_codificado = decodificacion(txt)
			cifrado = descifrado_propio(mensaje_cifrado_y_codificado)
			print ("El mensaje decodificado: "," ".join(mensaje_cifrado_y_codificado)) 	
	else:
		tipo_cifrado = int(input("Elegir un cifrado valido: "))
 
	print("Mensaje recibido: ",cifrado)

