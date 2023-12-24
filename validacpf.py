import re


def validacpf(cpf):
    cpf = str(cpf)

    if not cpf or len(cpf) != 11:
        return False
    cpf = re.sub(r'[^0-9]', '', cpf)
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(9):
        total += int(novo_cpf[index]) * reverso
        reverso -= 1

    reverso = 11
    d = 11 - (total % 11)

    if d > 9:
        d = 0
    novo_cpf += str(d)

    reverso = 10
    total = 0

    for index in range(10):
        total += int(novo_cpf[index]) * reverso
        reverso -= 1

    reverso = 11
    d = 11 - (total % 11)

    if d > 9:
        d = 0
    novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False
