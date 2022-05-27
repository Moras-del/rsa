from utils import generateKeys, saveKeyToFile, saveCodeToFile, get_input, readFromFile, transformToBlocks, moduloPower

def genKeys():
    bitsLen = int(get_input("Podaj liczbę bitów klucza: "))
    n, e, d = generateKeys(bitsLen)
    saveKeyToFile('klucz_publiczny.txt', n, e)
    saveKeyToFile('klucz_prywatny.txt', n, d)
    print('Klucze pomyślnie zapisano do plików')

def encrypt():
    filePath = get_input('Podaj ścieżkę do pliku: ')
    blocks_num = int(get_input('Podaj długość bloku: '))
    n = int(get_input('Podaj n: '))
    e = int(get_input('Podaj e: '))
    data = readFromFile(filePath)
    blocks = transformToBlocks(data, blocks_num, 8)
    code = map(lambda block: moduloPower(block, e, n), blocks)
    saveCodeToFile(f'{filePath}_encoded', code)

def decrypt():
    filePath = get_input('Podaj ścieżkę do pliku: ')
    blocks_num = int(get_input('Podaj długość bloku: '))
    n = int(get_input('Podaj n: '))
    d = int(get_input('Podaj d: '))
    data = readFromFile(filePath).splitlines()
    decrypted = map(lambda num: moduloPower(int(num), d, n), data)
    saveCodeToFile(f'{filePath.replace("encoded", "decoded")}', decrypted)



if __name__ == '__main__':
    print('Co chcesz zrobić?')
    print('1) generuj klucz')
    print('2) zaszyfruj')
    print('3) odszyfruj')
    opt = int(input())
    if opt == 1:
        genKeys()
    if opt == 2:
        encrypt()
    if opt == 3:
        decrypt()