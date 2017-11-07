
word = 'криптосистема'

def isSimple(n):
   d = 2
   while n % d != 0:
       d += 1
   return d == n

def gcd(a, b): #greatest common divisor
    while b != 0:
        a, b = b, a % b
    return a

def s2b(s, offset=1071):
    return [(ord(i) - offset) for i in s]

def b2s(b, offset=1071):
    return ''.join([chr(i + offset) for i in b])

def checkG(g, p):
    Fn = p - 1
    if ((g ** Fn) % (Fn + 1) == 1) and (g < (Fn + 1)):
        for i in range(1, Fn - 1):
            if g ** i % (Fn + 1) == 1:
                return False
    else:
        return False
    return True


def genPrimeNumbers(nmin, nmax):
    a = [0] * nmax
    for i in range(nmax):
        a[i] = i
    a[1] = 0

    m = 2
    while m < nmax:
        if a[m] != 0:
            j = m * 2
            while j < nmax:
                a[j] = 0
                j = j + m
        m += 1

    return [i for i in a if (i >= nmin)]

while True:
    try:
        p = int(input('p: '))
        if isSimple(p):
            break
    except:
        pass

while True:
    try:
        g = int(input('g: '))
        if checkG(g, p):
            break
    except:
        pass

while True:
    try:
        x = int(input('x: '))
        if x < p:
            break
    except:
        pass

y = g**x%p
print('y: ' + str(y))

while True:
    try:
        k = int(input('k: '))
        if k <= p - 1:
            break
    except:
        pass

a = g ** k % p
print('a: ' + str(a))

nword = s2b(word)
print(word + ' - ' + str(nword))

encrypted_nword = [(y**k * i % p) for i in nword]
print(b2s(encrypted_nword) + ' - ' + str(encrypted_nword))

decrypted_nowrd = [((i * a) ** (p - 1 - x) % p) for i in encrypted_nword]
print(b2s(decrypted_nowrd) + ' - ' + str(decrypted_nowrd))