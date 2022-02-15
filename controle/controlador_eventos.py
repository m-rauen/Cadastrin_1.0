from entidade.evento import Evento 
from limite.tela_eventos import TelaEventos

class ControladorEventos: 
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_eventos = TelaEventos()
        self.__eventos = [] 
        
    @property
    def eventos(self):
        return self.__eventos
    
    def abre_tela(self):
        lista_opcoes = {1: self.adiciona_evento, 2: self.alterar_evento, 3: self.exclui_evento, 4: self.lista_um_evento, 5: self.lista_eventos, 0: self.voltar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_eventos.tela_opçoes()]()
    
    def pega_evento_codigo(self, codigo):
        for event in self.__eventos:
            if event.codigo == codigo:
                return event
            return None
        
    def lista_eventos(self):
        if len(self.__eventos) < 1:
            self.__tela_eventos.mostra_mensagem('Não foram cadastrados eventos até o momento!')
        else: 
            for festa in self.__eventos:
                self.__tela_eventos.mostra_evento({'nome':festa.nome, 'código':festa.codigo, 'lotação máxima':festa.lotaçao_max, 'faixa etária':festa.faixa_etaria, 'open bar':festa.open_bar})
                
    def lista_um_evento(self):
        if len(self.__eventos) < 1:
            self.__tela_eventos.mostra_mensagem('Não foram cadastrados eventos até o momento')
        else: 
            codigo_evento = self.__tela_eventos.seleciona_evento()
            event = self.pega_evento_codigo(codigo_evento)
            if event is not None:
                self.__tela_eventos.mostra_evento({'nome':event.nome, 'código':event.codigo, 'lotação máxima':event.lotaçao_max, 'faixa etária':event.faixa_etaria, 'open bar':event.open_bar})
            else:
                self.__tela_eventos.mostra_mensagem('Evento não encontrado!')
    
    def adiciona_evento(self):
        dados_evento = self.__tela_eventos.pega_dados_evento()
        new_evento = Evento(dados_evento["nome"], dados_evento["codigo"], dados_evento["lotação máxima"], dados_evento["faixa etária"], dados_evento["open bar"])
        self.__eventos.append(new_evento)
        
        
    def exclui_evento(self):
        self.lista_eventos
        if len(self.__eventos) < 1:
            pass
        else:
            codigo_evento = self.__tela_eventos.seleciona_evento()
            event = self.pega_evento_codigo(codigo_evento)
        if event is not None:
            self.__eventos.remove(event)
            self.__tela_eventos.mostra_mensagem('Evento excluído com sucesso!')
        else:
            self.__tela_eventos.mostra_mensagem('Evento inexistente!')       
            
            
    def alterar_evento(self):
        self.__tela_eventos.mostra_mensagem('* ALTERANDO EVENTO * \n')
        if len(self.__eventos) < 1:
            pass
        else:
            codigo_evento = self.__tela_eventos.seleciona_evento()
            event = self.pega_evento_codigo(codigo_evento)
            if event is not None:
                novo_evento = self.__tela_eventos.pega_dados_eventos(self.__eventos)
                event.nome = novo_evento['nome']
                event.codigo = novo_evento['codigo']
                event.lotaçao_max = novo_evento['lotaçao_max']
                event.faixa_etaria = novo_evento['faixa_etaria']
                event.open_bar = novo_evento['open_bar']
                self.lista_eventos
            else:
                self.__tela_eventos.mostra_mensagem('Evento inexistente!')
                
    def voltar(self):
        self.__controlador_sistema.abre_tela()
        
     
    
    
        
