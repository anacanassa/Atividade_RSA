import random
import time

def withCesar(text: list, num_traslation: int, isEncode: bool):

    traslocated_text = []

    if isEncode:
        for character in text:
            traslocated_text.append(chr(ord(character) + num_traslation))
    else:
        for character in text:
            traslocated_text.append(chr(ord(character) - num_traslation))

    return "".join(traslocated_text)

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

def estimar_e(m):

    ini = time.perf_counter()
    e = gerar_primo(128)

    while not primos_entre_si(m, e):
        e = gerar_primo(128)

    fim = time.perf_counter()

    print(f"Tempo: {fim - ini:.10f} segundos")

    return e

def primos_entre_si(a, b):
    while b != 0:
        a, b = b, a % b

    if a == 1:
        return True

    return False


def gen_rsa_key():
    #Definindo valores rsa
    p = gerar_primo(256)
    q = gerar_primo(256)
    n = p * q

    m = (p-1) * (q-1)

    primos_entre_si = True

    e = estimar_e(m)

    d = pow(e, -1, m)

    return ((e, n), (d, n))

def crip_wtih_rsa(msg: str, chave):
    e, n = chave
    return [pow(ord(c), e, n) for c in msg]

def decrip_wtih_rsa(msg, chave):
    d, n = chave
    return "".join(chr(pow(c, d, n)) for c in msg)


if __name__ == '__main__':
    chave_publica, chave_privada = gen_rsa_key()

    mensagem = "The information security is of significant importance to ensure the privacy of communications"

    encryp = crip_wtih_rsa(mensagem, chave_publica)
    print("Cifrado:", encryp)

    original = decrip_wtih_rsa(encryp, chave_privada)
    print("Decifrado:", original)