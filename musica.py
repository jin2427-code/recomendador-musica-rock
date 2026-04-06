print("recomendador de bandas de rock")
while True:
    print("\n¿como te sientes?")
    print("1. tristre")
    print("2. feliz")
    print("3. relajado")
    print("4. emocionado")
    print("5. salir")
    
    opcion = input("elige una opcion (1-5): ")
    if opcion == "1":
        print("podrias escuchar algo de: boys dont cry o love my life ")
    elif opcion == "2":
        print("a ver algo como: Mr.Blue SKY o algo mas como here comes the sun")
    elif opcion == "3":
        print("algo relax: que te parece Sacr Tissue o The ZephyrSong")
    elif opcion == "4":
        print("algo emocionante en camino: que tal smell like teen spirit o american idiot")
    elif opcion == "5":
        print("adios espero que te haya ayudado")
    else:
        print("opcion invalida, intenta otra vez")
