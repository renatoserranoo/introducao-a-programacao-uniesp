from unicodedata import name


def nome(name, sobrenome):
    nomecompleto = name + '' + sobrenome
    print(nomecompleto)
    return 'a funçao ta ok'


nome('renato', 'serrano')
