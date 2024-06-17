def lectura_datos(nombre):
    archivo = open("protocolo_vigilancia.txt", "r", encoding="UTF-8")
    datos = []
    conta = 0
    lineas = archivo.readlines()
    for linea in lineas:
        linea = linea.rstrip("\n").split(",")
        datos.append(linea)
    return datos
def positivos(datos):
    positivos = []
    for linea in datos:
        if linea[-1].upper() == "POSITIVO":
            positivos.append(linea)
    return positivos

def funcion_a(datos):
    regiones = []
    for linea in datos:
        if linea[3] not in regiones:
            regiones.append(linea[3])
    cont = 0
    casos = 0
    while cont <= 15:
        for linea in positivos:   
            if regiones[cont] == linea[3]:
                del linea
                casos += 1
        print(regiones[cont] , ":", casos)
        cont += 1
        casos = 0
def funcion_b(positivos):
    postivofebrero = 0
    for linea in positivos:
        if linea[2][3:] == "02-2023":
            postivofebrero += 1
    return postivofebrero
def funcion_c(positivos):
    pelicanos = 0
    for linea in positivos:
        if linea[5].upper() == "PELICANO":
            pelicanos += 1
    return pelicanos
def funcion_d(positivos):
    loro = 0   
    for linea in positivos:
        if linea[5].upper() == "LORO TRICAHUE CHILENO":
            if linea[2][3:] == "03-2022":
                loro += 1
    return loro
datos = lectura_datos("protocolo_vigilancia.txt")
positivos = positivos(datos)
funcion_a(positivos)


