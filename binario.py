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

print("\n****************************************\n")

# Conversion de hexadecimal a binarios
diccionario = {"1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}

binario = ""

hexadecimal = input("Ingrese el número hexadecimal que desea convertir a binario:\n")
hexadecimal = hexadecimal.upper()
for letra in hexadecimal:
    valor = diccionario[str(letra)]
    binario = binario + valor

while len(binario)>0:
    if int(binario[0]) == 0:
        binario = binario[1:]
    else:
        break

print(f"El número hexadecimal {hexadecimal} a binario es: {binario}")
