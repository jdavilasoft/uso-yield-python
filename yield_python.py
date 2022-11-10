def genera_pares(limite):
    num = 1
    while num<limite:
        yield num*2
        num+=1
    
lista_pares = genera_pares(10)

print(next(lista_pares))
print(next(lista_pares))

# La funcion solo es llamada cuando se usa next
# e itera una sola vez, en este caso solo genera
# un olo numero par.
