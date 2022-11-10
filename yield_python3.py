def devuelve_ciudades(*ciudades):
    for ciudad in ciudades:
        for caracter in ciudad:
            yield caracter

ciudades_devueltas = devuelve_ciudades("Madrid", "Sao Paulo", "New York", "Bogotá", "Lima")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

# Ahora devuelve caracater a caracter de
# cada ciudad iterada, y solo se genera
# cada vez que se llama al metodo 'next'