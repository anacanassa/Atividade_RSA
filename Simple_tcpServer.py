from socket import *
import Utils
import random

#Definindo valores diffie-helman
n = Utils.gerar_primo(256)
g = 5
x = random.randint(2, n-2)
r1 = pow(g, x, n)

#Definindo informação do servidor
serverPort = 12500
serverSocket = socket(AF_INET,SOCK_STREAM)

#Abrindo a porta
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()


#Recebendo a mensagem
sentence = connectionSocket.recv(65000)
received = str(sentence,"utf-8")
print ("Received From Client: ", received)

capitalizedSentence = sentence.upper() # processamento

connectionSocket.send(capitalizedSentence)

sent = str(capitalizedSentence,"utf-8")
print ("Sent back to Client: ", sent)
connectionSocket.close()