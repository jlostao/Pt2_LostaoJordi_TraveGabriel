if sel == 1:
    frase = input("Dame una frase: ")
if sel == 2:
    vocales = "aeiou"
    newfrase = ""
    for letter in frase:
        if letter.lower() not in vocales:
            newfrase += letter
    frase = newfrase
