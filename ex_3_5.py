
frase = input("Dame una frase: ")
vocales = ["a", "e", "i", "o", "u"]
nueva = ""
for i in frase:
    if i in vocales:
        nueva = nueva + i
print(nueva)
