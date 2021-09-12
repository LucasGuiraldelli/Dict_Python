Tel_validos = []
Tel_invalidos = []

arq = open('telefones.txt').read()      # read() por fora para ser possível o uso dos telefones dentro do arquivo
arquivo = arq.split()                   # split() para demarcar um ponto de ruptura dos números de telefone


for Telefone in range(len(arquivo)):
    soma = 0
    invalido = True
    elemento = list(arquivo[Telefone])
    soma = sum(map(int, elemento))
    for caracter in range(len(elemento) -1):
        ProxCaracter = caracter + 1
        if (elemento[caracter] == elemento[ProxCaracter]) or (int(soma) % 2 != 0) or (elemento[0] == elemento[-1]):   # reponsável por fazer esse esquema de ir para o próximo número
            invalido = True
            break
        else:
            invalido = False

    if invalido == False:
        Tel_validos.append(''.join(elemento))

    elif invalido == True:
        Tel_invalidos.append(elemento)



arq_Valido = open("tel_validos.txt", "w", encoding="utf-8")
arq_Valido.write("Números Válidos: \n")
arq_Valido.write("\n".join([str(item) for item in Tel_validos]))
arq_Valido.close()

arq_Invalido = open("tel_invalidos.txt", "w", encoding="utf-8")
arq_Invalido.write("Números Inválidos: \n")
arq_Invalido.write("\n".join([str(item) for item in Tel_invalidos]))
arq_Invalido.close()