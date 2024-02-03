# Conversion de números decimales a binarios
numero = int(input("Ingrese el número decimal que desea convertir a binario:\n"))
binario = ""
valorInicial = numero
while numero > 0:
    cociente = numero / 2
    residuo = numero % 2
    numero = int(cociente)
    binario = str(residuo)+binario

print(f"El número {valorInicial} a binario es: {binario}")

