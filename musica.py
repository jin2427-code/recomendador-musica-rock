nombre = input("nombre: ")
print("bienvenido", nombre, "a tu recomendacion de rock")
estado = input("¿como estas hoy? (feliz, triste, relajado, emocionado): ")
if estado == "triste":
    print("te recomiendo escuchar algo de: hey jude o No surprises")
elif estado == "feliz":
    print("algo de: te hacen falta vitaminas o el ataque de las chicas cocodrilo que te parece")
elif estado == "relajado":
    print("algo tranqui va que te parece:there is a light that never goes out o algo de back to the old house")
elif estado == "emocionado":
    print("estas emocionado va a ver que te parece: smell like teen spirit o american idiot")    
else:
    print("este se mejora en algun tiempo pero para mientras explora mas musica rock")