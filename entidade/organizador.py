from entidade.usuario import Usuario 

class Organizador(Usuario):
    def __init__(self, nome: Usuario, cpf: Usuario, endereço: Usuario, idade: Usuario, codigo_org: int): 
        super().__init__(nome, cpf, endereço, idade)
        self.__codigo_org = codigo_org
        
    @property
    def codigo_org(self):
        return self.__codigo_org
    
    @codigo_org.setter
    def codigo_org(self, codigo_org: int):
        self.__codigo_org = codigo_org
        
    
    