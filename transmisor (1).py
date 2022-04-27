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

#----------------------Funciones ----------------------------------

def binario_a_ascii(binario):
    # Convertir binario a decimal
    valor = int(binario, 2)
    # Convertir el decimal a su representación ASCII
    return chr(valor)

def ascii_a_binario(letra):
    # Extraer su valor entero
    valor = ord(letra)
    # Convertirlo a binario
    return "{0:08b}".format(valor)

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

def cifradopropio (txt):
    tipcifra = random.randint(0,2)
    print("")
    if tipcifra  == 0:
        txt= txt.replace("m","0")
        txt= txt.replace("u","1")
        txt= txt.replace("r","2")
        txt= txt.replace("c","3")
        txt= txt.replace("i","4")
        txt= txt.replace("e","5")
        txt= txt.replace("l","6")
        txt= txt.replace("a","7")
        txt= txt.replace("g","8")
        txt= txt.replace("o","9")
    if tipcifra  == 1:
        txt= txt.replace("n","0")
        txt= txt.replace("e","1")
        txt= txt.replace("u","2")
        txt= txt.replace("m","3")
        txt= txt.replace("a","4")
        txt= txt.replace("t","5")
        txt= txt.replace("i","6")
        txt= txt.replace("c","7")
        txt= txt.replace("o","8")
        txt= txt.replace("s","9")

    if tipcifra  == 2:
        txt= txt.replace("e","0")
        txt= txt.replace("u","1")
        txt= txt.replace("c","2")
        txt= txt.replace("a","3")
        txt= txt.replace("l","4")
        txt= txt.replace("i","5")
        txt= txt.replace("p","6")
        txt= txt.replace("t","7")
        txt= txt.replace("o","8")
        txt= txt.replace("s","9")
    msg = txt+str(tipcifra)
    return (msg)

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

def hamming(mensaje_a_codificar):
    arreglo = list(mensaje_a_codificar)
    letra_a_binario = [ascii_a_binario(num) for num in arreglo]
    for index, value in enumerate(letra_a_binario):        
        l = str(value)
        letra = l[1:]
        letra_a_binario[index] = letra
        d1 = int(letra[0])
        d2 = int(letra[1])
        d3 = int(letra[2])
        d4 = int(letra[3])
        d5 = int(letra[4])
        d6 = int(letra[5])
        d7 = int(letra[6])
        p1 = xor_5(d1,d2,d4,d5,d7)
        p2 = xor_5(d1,d3,d4,d6,d7)
        p3 = xor_3(d2,d3,d4)
        p4 = xor_3(d5,d6,d7)
        letraH = str(p1)+str(p2)+str(d1)+str(p3)+str(d2)+str(d3)+str(d4)+str(p4)+str(d5)+str(d6)+str(d7)
        letra_a_binario[index] = letraH

    return (letra_a_binario)

def cifradocesar (txt):
    
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    codificado_cesar = ""
    for letra in txt:
        if not letra.isalpha() or letra.lower() == 'ñ':  
            codificado_cesar += letra
            continue
        valor_letra = ord(letra) 
        alfabeto_a_usar = alfabeto  
        limite = 97  
        if letra.isupper():    
            limite = 65
            alfabeto_a_usar = alfabeto_may

        posicion = (valor_letra - limite + 3) % longitud_alfabeto

        codificado_cesar += alfabeto_a_usar[posicion]  #regresa los valores a letras y las concatena
    return codificado_cesar


def cifradohill(message, key):


    ciphertext = ''



    matrix_mensaje = []
    list_temp = []
    cifrado_final = ''
    ciphertext_temp = ''
    cont = 0

    # Convertir el mensaje a mayusculas

    message = message.upper()

    # Si el tamaño del mensaje es menor o igual al tamaño de la clave

    if len(message) <= len(key):

        # Convertir el tamaño del mensaje al tamaño de la clave, si no es igual, se añaden 'X' hasta que sean iguales los tamaños.

        while len(message) < len(key):
            message = message + 'X'

        # Crear la matriz para el mensaje

        for i in range(0, len(message)):
            matrix_mensaje.append(diccionario_encryt[message[i]])

        # Se crea la matriz

        matrix_mensaje = np.array(matrix_mensaje)

        # Se multiplica la matriz clave por la de mensaje

        cifrado = np.matmul(key, matrix_mensaje)

        # Se obtiene el modulo sobre el diccionario de cada celda

        cifrado = cifrado % 41

        # Se codifica de valores numericos a los del diccionario, añadiendo a ciphertext el valor en el diccionario pasandole como indice la i posicion de la variable cifrado

        for i in range(0, len(cifrado)):
            ciphertext += diccionario_decrypt[str(cifrado[i])]
    else:

    # Si el tamaño del mensaje es menor o igual al tamaño de la clave

        # Si al dividir en trozos del tamaño de la clave, existe algun trozo que tiene menos caracteres que la long. de la clave se añaden tantas 'X' como falten

        while len(message) % len(key) != 0:
            message = message + 'X'

        # Se troce el mensaje en subsstrings de tamaño len(key) y se alamcenan como valores de un array

        matrix_mensaje = [message[i:i + len(key)] for i in range(0,
                          len(message), len(key))]

        # Para cada valor del array (grupo de caracteres de la longitud de la clave)

        for bloque in matrix_mensaje:

            # Crear la matriz para el bloque

            for i in range(0, len(bloque)):
                list_temp.append(diccionario_encryt[bloque[i]])

            # Se crea la matriz de ese bloque

            matrix_encrypt = np.array(list_temp)

            # Se multiplica la matriz clave por la del bloque

            cifrado = np.matmul(key, matrix_encrypt)

            # Se obtiene el modulo sobre el diccionario de cada celda

            cifrado = cifrado % 41

            # Se codifica de valores numericos a los del diccionario, añadiendo a ciphertext el valor en el diccionario pasandole como indice la i posicion de la variable cifrado

            for i in range(0, len(cifrado)):
                ciphertext_temp += diccionario_decrypt[str(cifrado[i])]

            # Se inicializan las variables para el nuevo bloque

            matrix_encrypt = []
            list_temp = []

        # Se añade el mensaje encriptado a la variable que contiene el mensaje encriptado completo

        ciphertext = ciphertext_temp

    # --------------------------------

    return ciphertext

print("""
    1)Cifrado Cesar
    2)Cifrado Hill
    3)Cifrado propio
    """)

while (True):
    tipo_cifrado = int(input("Ingrese el tipo de cifrado que quiere: "))
    if(tipo_cifrado <= 3):
        txt = input("Mensaje a trasnmitir: ") #------Mensaje que queremos enviar
        if (tipo_cifrado == 1):
            cifrado = cifradocesar(txt)
            print("Mensaje cifrado: ",cifrado)
            mensaje_cifrado_y_codificado = hamming(cifrado)
        elif(tipo_cifrado == 2):
            key =  [[13, 17], [10, 16]]
            cifrado = cifradohill(txt,key)
            mensaje_cifrado_y_codificado = hamming(cifrado)
            print("Mensaje cifrado: ",cifrado)
        elif(tipo_cifrado == 3):
            cifrado = cifradopropio(txt)
            mensaje_cifrado_y_codificado = hamming(cifrado)
            print("Mensaje cifrado: ",cifrado)
    else:
        tipo_cifrado = int(input("Elegir un cifrado valido: "))
    print ("El mensaje transmitido: "," ".join(mensaje_cifrado_y_codificado)) 
#----------------Transmision de informacion---------------------
#-------Sustituir por el metodo de envio de informacion-------#
 








