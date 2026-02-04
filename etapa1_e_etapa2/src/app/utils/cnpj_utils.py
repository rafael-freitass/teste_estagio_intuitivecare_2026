import re

def cnpj_eh_valido(cnpj: str) -> bool:
    if not isinstance(cnpj, str):
        return False

    cnpj = re.sub(r"\D", "", cnpj)

    if len(cnpj) != 14:
        return False

    if cnpj == cnpj[0] * 14:
        return False

    def calc_digito(cnpj, peso):
        soma = sum(int(cnpj[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return "0" if resto < 2 else str(11 - resto)

    peso1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    peso2 = [6] + peso1

    digito1 = calc_digito(cnpj[:12], peso1)
    digito2 = calc_digito(cnpj[:13], peso2)

    return cnpj[-2:] == digito1 + digito2