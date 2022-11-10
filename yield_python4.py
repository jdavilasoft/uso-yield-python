def devuelve_ciudades(*ciudades):
    for ciudad in ciudades:
        #for caracter in ciudad:
        yield from ciudad

ciudades_devueltas = devuelve_ciudades("Madrid", "Sao Paulo", "New York", "Bogotá", "Lima")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

# Una variación, usando un solo for