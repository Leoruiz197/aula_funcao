lista = [4,7,3,8]

def media(lista):
    acumulador = 0
    for nota in lista:
        acumulador += nota
    return acumulador / len(lista)
