funcionario = [[]]

while True:
    print('\n1-Cadastrar pessoa')
    print('2-Lista Cadastros')
    print('3-Apagar funcionario específico')
    print('4-Alterar um funcionário')
    print('5-Adicionar aumento de salario.')
    op = int(input())

    if op == 1:
        nova = []
        codigo = int(input('Código do Funcionário: '))
        nome = str(input('Digite o nome do Funcionário: '))
        dataAdmissao = str(input('Data de admissão: '))
        salario = int(input('Salário do Funcionário: '))
        nova.append((codigo, nome, salario, dataAdmissao))
        funcionario.append(nova)

    elif op == 2:
        for pessoa in funcionario:
            for i in pessoa:
                print(
                    f'- Nome do funcionário: {i[1]}. Código do funcionário: {i[0]}. Data de admissão: {i[2]}. Salário do funcionário: {i[3]}.')

    elif op == 3:
        print('Digite o numero do funcionario que você deseja apagar.')
        del funcionario[int(input())]

    elif op == 4:
        print('Digite o numero do funcionario que voce deseja alterar.')
        funcionario[int(input())] = alterar = []
        codigo = int(input('Código do Funcionário: '))
        nome = str(input('Digite o nome do Funcionário: '))
        dataAdmissao = int(input('Data de admissão: '))
        salario = int(input('Salário do Funcionário: '))
        nova.append((codigo, nome, salario, dataAdmissao))
        funcionario.append(alterar)

    elif op == 5:
        print('Adicionar aumento de salario.')
        salario = float(input('Salário do funcionario: '))
        aumento = salario + float(input('adicione o valor do aumento:'))
        print('Novo salário: R$ ', aumento)
