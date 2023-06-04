import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz '
rot = 3
rep = 0
def cipher(message, dir):
    m = ''
    for x in message:
        if x in alphabet:
            pos = alphabet.index(x)
            m += alphabet[(pos + (rot * dir)) % len(alphabet)]
        else:
            m += x
    return m

def encrypt(message):
    return cipher(message, 1)

def decrypt(message):
    return cipher(message, -1)

while rep < 1:
    operacao = str(input('Bem-Vindo(a) ao sistema de criptografia!\nPara criptografar algo digite "C"\nPara desencriptografar digite "D"\nOperação:').lower())
    message = str(input('Digite a mensagem: ').lower())
    if operacao == 'c':
        print("A mensagem criptografada é ",encrypt(message).title())
    elif operacao == 'd':
        print("A mensagem traduzida é ",decrypt(message).title())
    else:
        print ('O comando {} não existe'.format(operacao))
    ap = str(input('Deseja usar o sistema novamente? ').lower())
    if ap == 'sim' or ap == "s":
        continue
    else:
        rep += 1

print('Sistema Finalizado!')
