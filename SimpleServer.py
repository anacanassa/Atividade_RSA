from socket import *
import Utils
import ast

#Definindo valores rsa
chavePublicaServer, chavePrivadaServer = Utils.gen_rsa_key()

#Definindo informação do servidor
serverPort = 25000
serverSocket = socket(AF_INET,SOCK_STREAM)

#Abrindo a porta
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()

connectionSocket.send(bytes(str(chavePublicaServer), "UTF-8"))

#Recebendo a mensagem
clientr2 = connectionSocket.recv(65000)
clientinfo = str(clientr2,"utf-8")

parte1, parte2 = clientinfo.split("),")

chavePublicaClient = ast.literal_eval(parte1 + ')')
mensagem = ast.literal_eval(parte2)

print(mensagem)

decripReceived = Utils.decrip_wtih_rsa(mensagem, chavePrivadaServer)

print ("Received From Client: ", decripReceived)

capitalizedSentence = decripReceived.upper() # processamento

criptCapitalized = Utils.crip_wtih_rsa(capitalizedSentence, chavePublicaClient)

connectionSocket.send(bytes(str(criptCapitalized), "UTF-8"))

sent = capitalizedSentence
print ("Sent back to Client: ", sent)
connectionSocket.close()