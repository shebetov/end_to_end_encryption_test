
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

word = 'абрамов'

def isSimple(n):
   d = 2
   while n % d != 0:
       d += 1
   return d == n

def gcd(a, b): #greatest common divisor
    while b != 0:
        a, b = b, a % b
    return a

def s2b(s):
    return [alphabet.index(i) + 1 for i in s]

def b2s(b):
    return ''.join([alphabet[i - 1] for i in b])

def checkG(g, p):
    Fn = p - 1
    if ((g ** Fn) % (Fn + 1) == 1) and (g < (Fn + 1)):
        for i in range(1, Fn):
            if g ** i % (Fn + 1) == 1:
                return False
    else:
        return False
    return True

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

y = g**x % p
print('y: ' + str(y))

while True:
    try:
        k = int(input('k: '))
        if k < p:
            break
    except:
        pass

a = g ** k % p
print('a: ' + str(a))

nword = s2b(word)
print(word + ' - ' + str(nword))


encrypted_nword = [((y**k * i) % p) for i in nword]
try:
    print(b2s(encrypted_nword) + ' - ' + str(encrypted_nword))
except:
    print(encrypted_nword)

decrypted_nword = [(i * (a ** (p - 1 - x)) % p) for i in encrypted_nword]
print(b2s(decrypted_nword) + ' - ' + str(decrypted_nword))
