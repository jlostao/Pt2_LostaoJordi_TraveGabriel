menu = "1. Introdueix una frase \n2. Elimina les vocals \n3. Elimina les consonants \n" \
       "4. Ordena la frase al revés i printala per pantalla \n5. Ordena les paraules de la frase en " \
       "ordre ascendent i printales per pantalla \n6. Sortir \nSelecció: "

while True:
    sel = int(input(menu))
    if sel == 1:
        frase = input("Dame una frase: ")
    if sel == 2:
        vocales = "aeiou"
        newfrase = ""
        for letter in frase:
            if letter.lower() not in vocales:
                newfrase += letter
        frase = newfrase
    if sel == 3:
        vocales = ["a", "e", "i", "o", "u"]
        nueva = ""
        for i in frase:
            if i in vocales:
        nueva = nueva + i
        print(nueva)
    if sel == 4:
        newfrase = ""
        for i in range(len(frase) - 1, -1, -1):
            newfrase += frase[i]
        print(newfrase)
    if sel == 5:
        frase=input("dame una frase: ")
        frase = frase.split(" ")
        for i in range(len(frase)):
            a = 1
            for j in range(0, len(frase) - (a)):
                if frase[j][1].lower() > frase[a][1].lower():
                    frase[j], frase[a] = frase[a], frase[j]
            a += 1
        print(frase)
    if sel == 6:
        break
