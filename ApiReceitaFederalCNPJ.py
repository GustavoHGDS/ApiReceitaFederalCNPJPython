import requests
import json
from pycpfcnpj import cnpj as cnpjlib
import re
import os

rodando = True

while rodando:
    try:
        cnpj = input('Insira o CNPJ ou CPF: ')
        if cnpjlib.validate(cnpj):
            cnpj = re.sub('[^0-9]', '', cnpj)
            url = f'https://receitaws.com.br/v1/cnpj/{cnpj}'

            data = requests.get(url)

            teste = json.loads(data.text)
            for test in teste['atividade_principal']:
                print(test['text'], ' | Cnae:', test['code'], '\n')
            print('Abertura:', teste['abertura'], '\n')
            print('Data Situação:', teste['data_situacao'], '\n')
            print('Tipo:', '', teste['tipo'], '\n')
            print('Telefone:', teste['telefone'], '\n')
            print('E-mail:', teste['email'], '\n')


            for atvdd_secundarias in teste['atividades_secundarias']:
                print('Descrição / Atividade:', atvdd_secundarias['text'], '\n')
            print('Situação:', teste['situacao'], '\n')
            print('Bairro:', teste['bairro'], '\n')
            print('Logradouro:', teste['logradouro'], '\n')
            print('Numero:', teste['numero'], '\n')
            print('CEP:', teste['cep'], '\n')
            print('Município:', teste['municipio'], '\n')
            print('Porte:', teste['porte'], '\n')
            print('Natureza Jurídica:', teste['natureza_juridica'], '\n')
            print('CNPJ:', teste['cnpj'], '\n')
            print('Ultima_atualizacao:', teste['ultima_atualizacao'], '\n')
            print('Status:', teste['status'], '\n')
            print('Fantasia:', teste['fantasia'], '\n')
            print('Complemento:', teste['complemento'], '\n')
            print('EFR:', teste['efr'], '\n')
            print('Motivo Situação:', teste['motivo_situacao'], '\n')
            print('Situação Especial:', teste['situacao_especial'], '\n')
            print('Data Situação Especial:', teste['data_situacao_especial'], '\n')
            print('Capital Social:', teste['capital_social'], '\n')

            for test in teste['qsa']:
                print('QSA:', test, '\n')

            sair = input('Deseja Sair? (s) ou (n)\n')
            if sair == 's':
                rodando = False
            else:
                os.system('cls')
        else:
            print('CNPJ Inválido!')
    except:
        print('Aguarde 1 minuto e tente novamente, somente 3 consultas por minuto.')
