# Biblioteca que permite passagem de parâmetros/conversão de leitura de bytes do C pra Python/uso de funções em C
import ctypes

# Carrega a biblioteca compartilhada do C
meucodigo = ctypes.CDLL(r".\funcoesC.dll") # Windows: .dll | Linux: .so

#Informa o Python para ler o retorno de obter_mensagem() como um PONTEIRO
meucodigo.obter_mensagem.restype = ctypes.POINTER(ctypes.c_char)

pMensagem = meucodigo.obter_mensagem() #Recebeu o ponteiro da string mensagem.
#Se isso nao for feito, o endereço de memória será perdido e não terá como liberar depois,
#então, basicamente é so criar uma variável (pMensagem) para armazenar antes de interpretar como
#ponteiro para caracter.

#Diz pro Python como os retornos devem ser lidos (converter float do C para float do Python) e etc.
meucodigo.multiplica.argtypes = [ctypes.c_float, ctypes.c_float]
meucodigo.multiplica.restype = ctypes.c_float
meucodigo.obter_mensagem.restype = ctypes.c_char_p #Agora informa para ele ler como ponteiro para string.
meucodigo.libera_memoria.argtypes = [ctypes.c_void_p]

############ Função multiplica() do C a ############

print("Função multiplica(float a, float b) do C\n")
n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))

#Insere as entradas na função, convertendo n1 e n2 para float do C.
resultado = meucodigo.multiplica(ctypes.c_float(n1), ctypes.c_float(n2))
print(f"Resultado da multiplicação: {resultado}")

############ Função para ler uma string do C ############

#Agora recebe o retorno como ponteiro para string (foi alterado como ia ser lido após o armazenamento do ponteiro)
mensagem = meucodigo.obter_mensagem()
print("\nString recebida do C --> ", mensagem.decode('utf-8'))

meucodigo.libera_memoria(pMensagem) #Libera a memória alocada do ponteiro.
input("\nFim do programa - Pressione Enter para sair.\n")
