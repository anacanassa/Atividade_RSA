from socket import *
import random
import Utils

#Informação de rede
serverName = "192.168.200.169"
serverPort = 12500

#Criar a conexão
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Definindo valores diffie-helman
n = Utils.gerar_primo(256)
g = 5
y = random.randint(2, n-2)
r2 = pow(g, y, n)

#Enviando r1
clientSocket.send(bytes(r2, "utf-8"))

#Recebendo r2
r2 = clientSocket.recv(65000)



#Definir a mensagem
sentence = input("Input lowercase sentence: ")

clientSocket.send(bytes(sentence, "utf-8"))
modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence,"utf-8")
print ("Received from Make Upper Case Server: ", text)
clientSocket.close()