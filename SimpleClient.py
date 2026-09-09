from socket import *
import Utils
import time

ini = time.perf_counter()
#Informação de rede
serverName = "10.1.70.9"
serverPort = 25000

#Criar a conexão
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Definindo valores diffie-helman
severInfo = str(clientSocket.recv(65000),"utf-8")
chavePublicaServer = severInfo 
chavePublicaClient, chavePrivadaClient = Utils.gen_rsa_key()

mensagem = "The information security is of significant importance to ensure the privacy of communications"

cripty_msg = Utils.crip_wtih_rsa(mensagem, chavePublicaServer)

package = f"{chavePublicaClient},{mensagem}"

#Enviando chave e mensagem
clientSocket.send(bytes(package, "utf-8"))

modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence,"utf-8")

decriptoModified = Utils.decrip_wtih_rsa(text, chavePrivadaClient)

print ("Received from Make Upper Case Server: ", decriptoModified)
clientSocket.close()

fim = time.perf_counter()

print(f"Tempo: {fim - ini:.10f} segundos")