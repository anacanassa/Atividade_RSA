# Atividade_RSA

# Aplicação RSA — Comunicação Cliente-Servidor

## Descrição

Este projeto apresenta uma implementação simplificada do algoritmo de criptografia **RSA**, integrada a uma comunicação entre **cliente e servidor utilizando sockets TCP**.

A aplicação demonstra o processo de geração de chaves RSA, troca de chaves públicas, criptografia e descriptografia de mensagens. Além da comunicação segura, o servidor realiza um processamento simples sobre a mensagem recebida, convertendo seu conteúdo para letras maiúsculas antes de enviá-la novamente ao cliente.

O projeto foi desenvolvido em Python e não utiliza bibliotecas externas para realizar as operações principais do RSA.

## Estrutura do projeto

```text
.
├── SimpleClient.py
├── SimpleServer.py
└── Utils.py
```

### `Utils.py`

Contém as funções responsáveis pela implementação do RSA e pela geração dos números primos.

Entre as principais funções estão:

* `miller_rabin()` — realiza o teste probabilístico de primalidade de Miller-Rabin.
* `gerar_primo()` — gera números primos aleatórios.
* `primos_entre_si()` — verifica se dois números são coprimos.
* `estimar_e()` — determina o expoente público `e`.
* `gen_rsa_key()` — gera as chaves pública e privada do RSA.
* `crip_wtih_rsa()` — realiza a criptografia da mensagem.
* `decrip_wtih_rsa()` — realiza a descriptografia da mensagem.

A geração das chaves utiliza dois números primos de 256 bits, formando o módulo `n = p × q`.

### `SimpleServer.py`

É responsável por iniciar o servidor TCP e gerar o par de chaves RSA.

O servidor:

1. Gera sua chave pública e privada.
2. Inicializa um socket TCP na porta `25000`.
3. Aguarda uma conexão do cliente.
4. Envia sua chave pública para o cliente.
5. Recebe a chave pública do cliente e a mensagem criptografada.
6. Descriptografa a mensagem utilizando sua chave privada.
7. Converte a mensagem para letras maiúsculas.
8. Criptografa a resposta utilizando a chave pública do cliente.
9. Envia a resposta criptografada de volta ao cliente.

### `SimpleClient.py`

É responsável por estabelecer a conexão com o servidor e realizar a comunicação.

O cliente:

1. Conecta-se ao servidor utilizando TCP.
2. Recebe a chave pública do servidor.
3. Gera seu próprio par de chaves RSA.
4. Criptografa a mensagem utilizando a chave pública do servidor.
5. Envia sua chave pública juntamente com a mensagem criptografada.
6. Recebe a resposta criptografada.
7. Descriptografa a resposta utilizando sua chave privada.

## Funcionamento do RSA

O RSA utiliza um par de chaves:

* **Chave pública:** utilizada para criptografar mensagens.
* **Chave privada:** utilizada para descriptografar mensagens.

Neste projeto, as chaves são representadas pela tupla:

```text
(e, n)
```

para a chave pública e:

```text
(d, n)
```

para a chave privada.

A geração das chaves segue o processo:

```text
p, q → n = p × q
      ↓
φ(n) = (p-1) × (q-1)
      ↓
escolha de e
      ↓
d = e⁻¹ mod φ(n)
      ↓
Chave pública: (e, n)
Chave privada: (d, n)
```

A criptografia é realizada individualmente para cada caractere da mensagem:

```text
c = m^e mod n
```

Enquanto a descriptografia utiliza:

```text
m = c^d mod n
```

Essas operações estão implementadas nas funções `crip_wtih_rsa()` e `decrip_wtih_rsa()`.

## Fluxo da comunicação

O funcionamento da aplicação pode ser representado da seguinte maneira:

```text
                 SERVIDOR
                    │
             Gera chaves RSA
                    │
          ┌─────────┴─────────┐
          │                   │
     Chave pública       Chave privada
          │
          │
          ▼
        CLIENTE
          │
    Recebe chave pública
          │
    Gera suas próprias
       chaves RSA
          │
          ▼
    Criptografa mensagem
    com chave pública
       do servidor
          │
          ▼
      ┌───────────┐
      │  SERVIDOR │
      └─────┬─────┘
            │
      Descriptografa
      com chave privada
            │
            ▼
      Converte para
      letras maiúsculas
            │
            ▼
       Criptografa
       resposta com
       chave pública
       do cliente
            │
            ▼
        CLIENTE
            │
      Descriptografa
      com chave privada
            │
            ▼
       Exibe resposta
```

## Mensagem utilizada

O cliente envia inicialmente a seguinte mensagem:

```text
The information security is of significant importance to ensure the privacy of communications
```

Essa mensagem é criptografada utilizando a chave pública do servidor antes de ser enviada.

O servidor descriptografa a mensagem e realiza o processamento:

```python
capitalizedSentence = decripReceived.upper()
```

Em seguida, a resposta é criptografada novamente utilizando a chave pública enviada pelo cliente.

Assim, o cliente recebe a mensagem processada e a descriptografa utilizando sua chave privada.

## Requisitos

* Python 3.x
* Dois processos em execução na mesma rede ou máquina
* Arquivos `SimpleClient.py`, `SimpleServer.py` e `Utils.py`

Não são necessárias bibliotecas externas para a implementação do RSA.

## Como executar

### 1. Configurar o servidor

No arquivo `SimpleClient.py`, verifique o endereço IP configurado:

```python
serverName = "192.168.0.141"
serverPort = 25000
```

O endereço deve corresponder ao IP da máquina onde o servidor estiver executando.

### 2. Executar o servidor

Em um terminal, execute:

```bash
python SimpleServer.py
```

O servidor ficará aguardando uma conexão na porta `25000`.

### 3. Executar o cliente

Em outro terminal, execute:

```bash
python SimpleClient.py
```

O cliente estabelecerá a conexão com o servidor e iniciará o processo de troca de chaves e envio da mensagem.

### 4. Resultado esperado

O servidor deverá apresentar a mensagem recebida após a descriptografia e, posteriormente, a mensagem convertida para letras maiúsculas.

O cliente deverá apresentar a resposta recebida e descriptografada, por exemplo:

```text
Received from Make Upper Case Server:
THE INFORMATION SECURITY IS OF SIGNIFICANT IMPORTANCE TO ENSURE THE PRIVACY OF COMMUNICATIONS
```

## Tecnologias utilizadas

* **Python**
* **Sockets TCP**
* **Criptografia RSA**
* **Teste de primalidade de Miller-Rabin**
* **Aritmética modular**
* **Comunicação cliente-servidor**

## Observação sobre a implementação

Esta aplicação possui finalidade **acadêmica e didática**, demonstrando os principais conceitos matemáticos e computacionais envolvidos no RSA.

Ela não deve ser utilizada como implementação de criptografia para sistemas reais. Uma implementação de produção deve utilizar bibliotecas criptográficas consolidadas e técnicas adicionais, como padding seguro (por exemplo, OAEP), além de mecanismos adequados de autenticação e gerenciamento de chaves.

## Autores

Ana Beatriz 081220007
Erik 081220014
Estela 081220015
Pedro 081220044
