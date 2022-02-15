from limite.tela import Tela 

class TelaOrganizador:
    def trata_opçoes(self, msg: str = '', inteiros_validos = []):
        valor = input(msg)
        try:
            inteiro = int(valor)
            if inteiros_validos and inteiro not in inteiros_validos:
                raise ValueError
            return inteiro
        except ValueError:
            print('Valor inválido!!\n'
                  'Por favor, digite novamente.')
            if inteiros_validos:
                print('Valores aceitos: {}'.format(inteiros_validos))
                
    def tela_opçoes(self):
        print('-'*25)
        print(' O R G A N I Z A D O R E S ')
        print('-'*25)
        print('(1) - Adicionar organizador \n'
              '(2) - Alterar dados do organizador \n'
              '(3) - Excluir organizador \n'
              '(4) - Listar organizador selecionado \n'
              '(5) - Listar todos os organizadores \n '
              '(0) - Voltar')
        opçao = self.trata_opçoes('Digite a opção: ', [1,2,3,4,5,0])    
        return opçao
    
    def seleciona_organizador(self):
        codigo = input('Código do organizador: ')
        try:
            if codigo.isnumeric() == False: 
                raise ValueError
        except ValueError:
            print('Digite um código válido!! \n'
                      'Os códigos devem conter SOMENTE números')
    
    def pega_dados_organizador(self, lista_organizadores= []):
        print('DADOS DO ORGANIZADOR \n')
        organizador = {}
        codigos = []
        
        for organizer in lista_organizadores:
            codigos.append(organizer.codigo)
            
        while True:
            nome = input('Nome: ').capitalize()
            try:
                if nome.isascii() == False or nome.isnumeric == True:
                    raise ValueError
                if len(nome) < 1:
                    raise ValueError
                organizador['nome'] = nome 
                break
            except ValueError:
                print('Digite um nome válido!! \n'
                      'O nome deve ter, no mínimo, 1 carácter; \n'
                      'O nome não pode ser composto SOMENTE por números')
                
        while True:
            cpf = input('CPF: ')
            try:
                if cpf.isnumeric() == False: 
                    raise ValueError
                organizador['cpf'] = cpf 
                break 
            except ValueError:
                print('Digite um CPF válido!! \n'
                      'O CPF deve ter, precisamente, 11 caracteres numéricos')
                
        while True:
            endereço = input('Endereço: ')
            try: 
                if endereço.isascii() == False or endereço.isnumeric() == True:
                    raise ValueError
                organizador['endereço'] = endereço
                break
            except ValueError:
                print('Digite um endereço válido!! \n'
                      'O endereço deve conter a rua, o bairro e o número da residência')
                
        while True:
            idade = input('Idade: ')
            try: 
                if idade.isnumeric() == False:
                    raise ValueError
                organizador['idade'] = idade
                break
            except ValueError:
                print('Digite uma idade válida!! \n'
                      'Idades devem conter somente o número')
                
        while True:
            codigo_org = input('Código de organizador: ')
            try: 
                if codigo_org.isnumeric() == False:
                    raise ValueError
                if int(codigo_org) in codigos:
                    raise Exception 
                organizador['código'] = codigo_org
                break 
            except ValueError:
                print('Digite um código válido!! \n'
                      'Os códigos devem conter SOMENTE números')
            except Exception:
                print('Esse código já foi cadastrado')
        return organizador 
    
    def mostra_organizador(self, dados_organizador):
        print('-' *35)
        print('DADOS DO ORGANIZADOR: \n')
        print('Nome: {}'.format(dados_organizador['nome']))
        print('CPF: {}'.format(dados_organizador['cpf']))
        print('Endereço: {}'.format(dados_organizador['endereço']))
        print('Idade: {}'.format(dados_organizador['idade']))
        print('Código: {}'.format(dados_organizador['código']))
        print('-' *35) 
    
    def mostra_mensagem(self, msg: str):
        print(msg)