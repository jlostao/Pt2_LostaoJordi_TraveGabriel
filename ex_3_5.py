
vocales = ["a", "e", "i", "o", "u"]
nueva = ""
for i in frase:
    if i in vocales:
        nueva = nueva + i
print(nueva)

frase=input("dame una frase: ")
frase = frase.split(" ")
for i in range(len(frase)):
    a = 1
    for j in range(0, len(frase) - (a)):

        a += 1
print(frase)