from utils import generateKeys, saveKeyToFile, saveCodeToFile, get_input, readFromFile, moduloPower

def genKeys():
    bitsLen = int(get_input("Podaj liczbę bitów klucza: "))
    n, e, d = generateKeys(bitsLen)
    print(f'Klucz publiczny: n={n} d={d}')
    print(f'Klucz prywatny: n={n} e={e}')

def encrypt():
    message = get_input('Podaj wiadomość: ')
    n = int(get_input('Podaj n: '))
    d = int(get_input('Podaj d: '))
    code = map(lambda i: str(moduloPower(ord(i), d, n)), message)
    print(f'Podpis: {" ".join(code)}')

def decrypt():
    message = get_input('Podaj wiadomość: ')
    data = get_input('Podaj podpis: ').split()
    n = int(get_input('Podaj n: '))
    e = int(get_input('Podaj e: '))
    decrypted = map(lambda num: chr(moduloPower(int(num), e, n)), data)
    decrypted = ''.join(decrypted)
    if message == ''.join(decrypted):
        print('Podpis jest zgodny!')
    else:
        print('Podpis jest zły!')

if __name__ == '__main__':
    print('Co chcesz zrobić?')
    print('1) generuj klucze')
    print('2) podpisz wiadomość')
    print('3) zweryfikuj wiadomość')
    opt = int(input())
    if opt == 1:
        genKeys()
    if opt == 2:
        encrypt()
    if opt == 3:
        decrypt()

#Klucz publiczny: n=842713 d=438297
#Klucz prywatny: n=842713 e=965 830534 767975 830534