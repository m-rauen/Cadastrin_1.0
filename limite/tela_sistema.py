from limite.tela import Tela 

class TelaSistema(Tela):
    def trata_opcoes(self, msg: str = "", inteiros_validos = []):
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
    
    def tela_opcoes(self):
        print("-------- GERENCIADOR ---------")
        print("Escolha sua opção:")
        print("(1) - Participantes")
        print("(2) - Organizadores")
        print("(3) - Eventos")
        print("(0) - Finalizar sistema")
        opcao = self.trata_opcoes("Digite a opção: ", [1,2,3,0])
        return opcao