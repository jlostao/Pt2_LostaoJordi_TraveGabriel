menu = "1. Introdueix una frase \n2. Elimina les vocals \n3. Elimina les consonants \n" \
       "4. Ordena la frase al revés i printala per pantalla \n5. Ordena les paraules de la frase en " \
       "ordre ascendent i printales per pantalla \n6. Sortir \nSelecció: "

while True:
    sel = int(input(menu))
    if sel == 3:
        frase = input("Dame una frase: ")
        vocales = ["a", "e", "i", "o", "u"]
        nueva = ""
        for i in frase:
            if i in vocales:
                nueva = nueva + i
        print(nueva)
    if sel == 6:
        break