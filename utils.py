import random

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def func(n):
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count, n

def moduloPower(a, b, n):
    bits = bin(b)[2:]
    result = 1
    curr = a % n
    for i in range(len(bits)-1, -1, -1):
        if bits[i] == '1':
            result = (result*curr) % n
        curr = (curr * curr) % n
    return result

def rabin(n, k):
    if n == 2:
        return True
    count, m = func(n-1)
    for i in range(k):
        val = random.randint(2, n-1)
        if moduloPower(val, m, n) == 1:
            continue
        temp = []
        for j in range(1, count+1):
            temp.append(moduloPower(val, m*(2**j), n))
        if 1 not in temp:
            return False
        else:
            if temp[-1] == 1:
                continue
            else:
                return False
    return True

def generateNum(r):
    x = random.randrange(1 << (r-1), 1 << r)
    while not rabin(x, 5):
        x = random.randrange(1 << (r-1), 1 << r)
    return x

def getInversed(a, b):
    for i in range(b):
        if (i*a) % b == 1:
            return i
    return None

def generateKeys(r):
    p = generateNum(r)
    q = generateNum(r)
    n = p*q
    euler = (p-1)*(q-1)
    e = random.randrange(1 << (r-1), 1 << r)
    while gcd(e, euler) != 1:
        e = random.randrange(1 << (r-1), 1 << r)
    d = getInversed(e, euler)
    return n, e, d

def saveKeyToFile(fileName, n, m):
    with open(fileName, 'w') as file:
        file.write(f'{n}, {m}')

def saveCodeToFile(fileName, code):
    with open(fileName, 'w') as file:
        for i in code:
            file.write(f'{str(i)}\n')

def get_input(txt):
    print(txt, end='')
    return input()

def readFromFile(filePath):
    with open(filePath, 'r') as file:
        return file.read()

def transformToBlocks(data, blocksNum, const):
    remainder = len(data) % blocksNum
    result = []
    for i in range(0, len(data)-remainder, blocksNum):
        summed = 0
        for j in range(blocksNum):
            summed += ord(data[i+j])*const**j
        result.append(summed)
    summed = 0
    for i in range(len(data)-remainder, len(data)):
        summed += ord(data[i])*const**(i-(len(data)-remainder))
    if summed != 0:
        result.append(summed)
    return result
