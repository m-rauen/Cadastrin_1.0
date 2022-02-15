from limite.tela import Tela

class TelaParticipante: 
    def tela_opçoes(self):
        print('-'*25)
        print(' P A R T I C I P A N T E S ')
        print('-'*25)
        print('(1) - Adicionar participante \n'
              '(2) - Alterar dados do participante \n'
              '(3) - Excluir participante \n'
              '(4) - Listar participante selecionado \n'
              '(5) - Listar todos os participantes \n '
              '(0) - Voltar')
        opçao = self.trata_opçoes('Digite a opção: ')    
        return opçao
    
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
    
    def pega_dados_participante(self, lista_participantes = []):
        print('DADOS DO PARTICIPANTE \n')
        participante = {}
        codigos = []
        
        for participant in lista_participantes:
            codigos.append(participant.codigo)
            
        while True:
            nome = input('Nome: ').capitalize()
            try:
                if nome.isascii() == False or nome.isnumeric == True:
                    raise ValueError
                if len(nome) < 1:
                    raise ValueError
                participante.update({'nome':nome})
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
                participante.update({'cpf':cpf})
                break 
            except ValueError:
                print('Digite um CPF válido!! \n'
                      'O CPF deve ter, precisamente, 11 caracteres numéricos')
                
        while True:
            endereço = input('Endereço: ')
            try: 
                if endereço.isascii() == False or endereço.isnumeric() == True:
                    raise ValueError
                participante.update({'endereço':endereço})
                break
            except ValueError:
                print('Digite um endereço válido!! \n'
                      'O endereço deve conter a rua, o bairro e o número da residência')
                
        while True:
            idade = input('Idade: ')
            try: 
                if idade.isnumeric() == False:
                    raise ValueError
                participante.update({'idade': idade})
                break
            except ValueError:
                print('Digite uma idade válida!! \n'
                      'Idades devem conter somente o número')
                
        while True:
            vacina_3d = input('Apresenta 3 doses da vacina? (S/N): ').upper()
            try:
                if vacina_3d.isnumeric() == True:
                    raise ValueError
                participante.update({'vacina':vacina_3d})
                break 
            except ValueError:
                print('Digite uma resposta válida!! \n'
                      'A resposta deve ser somente uma letra, S ou N, maiúscula ou minúscula')
                
        while True:
            exame_pcr = input('Apresenta o exame PCR negativo? (S/N): ').upper()
            try: 
                if exame_pcr.isnumeric() == True:
                    raise ValueError
                participante.update({'pcr':exame_pcr})
                break 
            except ValueError:
                print('Digite uma resposta válida!! \n'
                      'A resposta deve ser somente uma letra, S ou N, maiúscula ou minúscula')
                
        while True:
            codigo = input('Código de participante: ')
            try: 
                if codigo.isnumeric() == False:
                    raise ValueError
                if int(codigo) in codigos:
                    raise Exception 
                participante.update({'codigo':codigo})
                break 
            except ValueError:
                print('Digite um código válido!! \n'
                      'Os códigos devem conter SOMENTE números')
            except Exception:
                print('Esse código já foi cadastrado')
        
        return participante
        
    def mostra_participante(self, dados_participante):
        print('-' *35)
        print('DADOS DO PARTICIPANTE: \n')
        print('Nome: ', dados_participante["nome"])
        print('CPF: {}'.format(dados_participante["cpf"]))
        print('Endereço: {}'.format(dados_participante["endereço"]))
        print('Idade: {}'.format(dados_participante["idade"]))
        print('Vacina - 3 doses: {}'.format(dados_participante["vacina"])) 
        print('Exame PCR negativo: {}'.format(dados_participante["pcr"]))
        print('Código: {}'.format(dados_participante["codigo"]))
        print('-' *35)
                
    def pega_participante_codigo(self):
        codigo = input('Código do participante: ')
        try:
            if codigo.isnumeric() == False: 
                raise ValueError
        except ValueError:
            print('Digite um código válido!! \n'
                      'Os códigos devem conter SOMENTE números')
        
    def mostra_mensagem(self, msg: str):
        print(msg)
                
                
        