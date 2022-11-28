from fila_normal import filanormal
from fila_prioritaria import filaprioritaria

""" filaTeste = filanormal()
filaTeste.AtualizaFila()
filaTeste.AtualizaFila()
filaTeste.AtualizaFila()
output = filaTeste.ChamaCliente(7)
print(output)
print(filaTeste.ChamaCliente(10)) """

fila_teste_2 = filaprioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(6))
print(fila_teste_2.estatistica('10/01/1993', 4, 'detail'))
