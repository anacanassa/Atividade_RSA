import random

def withCesar(text: list, num_traslation: int, isEncode: bool):

    traslocated_text = []

    if isEncode:
        for character in text:
            traslocated_text.append(chr(ord(character) + num_traslation))
    else:
        for character in text:
            traslocated_text.append(chr(ord(character) - num_traslation))

    return traslocated_text

def miller_rabin(n, k=20):
    if n < 2:
        return False

    # Casos pequenos
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False

    # Escreve n - 1 como d * 2^s
    d = n - 1
    s = 0

    while d % 2 == 0:
        d //= 2
        s += 1

    # Testes de Miller-Rabin
    for _ in range(k):
        a = random.randrange(2, n - 1)

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


def gerar_primo(bits):
    while True:
        n = random.getrandbits(bits)

        n |= (1 << (bits - 1))

        # Garante que seja ímpar
        n |= 1

        if miller_rabin(n):
            return n


if __name__ == '__main__':
    n = gerar_primo(256)
    g = 5

    # print("Tamanho em bits:", n.bit_length())

    x = random.randint(2, n-2)
    y = random.randint(2, n-2)

    r1 = pow(g, x, n)
    r2 = pow(g, y, n)

    k1 = pow(r2, x, n)
    k2 = pow(r1, y, n)

    print("Primo gerado:")
    print(n)
    print("Gerador:")
    print(g)

    print("X e Y:")
    print(x)
    print(y)

    print("R1 e 2:")
    print(r1)
    print(r2)

    print("K1 e 2:")
    print(k1)
    print(k2)

    chave = k1 % 26

    print (chave)

    texto_teste = 'Hello world'

    criptografado = withCesar(texto_teste, chave, True)

    descrip = withCesar(criptografado, chave, False)

    print(texto_teste)
    print(criptografado)
    print(descrip)