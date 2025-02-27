precioTacoMaiz = 35
precioTacoHarina = 45
precioBebida = 15

tacosMaiz = int(input("cuantos tacos de maiz desea ordenar?"))
tacosHarina = int(input("cuantos tacos de harina desea ordenar?"))
bebidas = int(input("Cuantas bebidas va a ordenar?"))

totalMaiz = tacosMaiz * precioTacoMaiz
totalHarina = tacosHarina * precioTacoHarina
totalBebida = bebidas * precioBebida

print(f"tacos de maiz: {tacosMaiz} y es un total de {totalMaiz}")
print(f"tacos de harina: {tacosHarina} y es un total de {totalHarina}")
print(f"el total de tu compra es: {totalMaiz + totalHarina} y {totalBebida} de las bebidas dando un subtotal de {totalMaiz + totalHarina + totalBebida}")