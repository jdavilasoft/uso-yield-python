def devuelve_ciudades(*ciudades):
    for item in ciudades:
        yield item

ciudades_devueltas = devuelve_ciudades("Madrid", "Sao Paulo", "New York", "Bogotá", "Lima")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))

# Solo devuelve una ciudad a la vez
# cada vez que se llama al metodo 'next'