class filanormal:
    codigo:int = 0
    fila = []
    clientesAtendidos = []
    senhaAtual:str = None 

    def GeraSenhaAtual(self) -> None:
        self.senhaAtual = f'NM{self.codigo}'

    def ResetaFila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def AtualizaFila(self) -> None:
        self.ResetaFila() 
        self.GeraSenhaAtual()
        self.fila.append(self.senhaAtual)

    def ChamaCliente(self, caixa:str) -> str:
        clienteAtual:str = self.fila.pop()
        self.clientesAtendidos.append(clienteAtual)
        return(f'Cliente atual: {clienteAtual}, dirija-se ao caixa {caixa}')