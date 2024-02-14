def validate_cpf(cpf):
    return len(cpf) == 11


def validate_rg(rg):
    return len(rg) == 9


def validate_celular(celular):
    return len(celular) == 14


def validate_nome(nome):
    return nome.isalpha()
