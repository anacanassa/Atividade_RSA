from socket import *
import Utils
import ast

#Informação de rede
serverName = "192.168.0.141"
serverPort = 25000

#Criar a conexão
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Definindo valores diffie-helman
severInfo = str(clientSocket.recv(65000),"utf-8")
chavePublicaServer = ast.literal_eval(severInfo) 
chavePublicaClient, chavePrivadaClient = Utils.gen_rsa_key()

mensagem = "The information security is of significant importance to ensure the privacy of communications"

cripty_msg = Utils.crip_wtih_rsa(mensagem, chavePublicaServer)

package = f"{chavePublicaClient},{cripty_msg}"

#Enviando chave e mensagem
clientSocket.send(bytes(package, "utf-8"))

modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence,"utf-8")

decriptoModified = Utils.decrip_wtih_rsa(ast.literal_eval(text), chavePrivadaClient)

print ("Received from Make Upper Case Server: ", decriptoModified)
clientSocket.close()