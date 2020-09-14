# anush, 116801027

import numpy as np

def ch_enc(ch, V):
    val = ord(ch)
    K = ord(V) - 97
    enc_ch = chr((val + K - 97)%26 + 97)
    return enc_ch

def ch_dec (ch, V):
    val = ord(ch)
    K = ord(V) - 97
    dec_ch = chr((val - K - 97)%26 + 97)
    return dec_ch

# Vigenere encryption function
def vigenere_enc(keyword, plaintext):
    c = ''
    for i in range(0, len(plaintext)):
        c = c + ch_enc(plaintext[i], keyword[i%len(keyword)])
    
    return c


# Vigenere decryption function
def vigenere_dec(keyword, ciphertext):
    p = ''
    for i in range(0, len(ciphertext)):
        p = p + ch_dec(ciphertext[i], keyword[i%len(keyword)])
    
    return p
    


def matrixinvmod26(Marr):
    # Calculate Minv26
    Minv = np.linalg.inv(Marr)
    Mdet = np.linalg.det(Marr)
    
    Mod26invTable = {}
    for m in range(26):
        for n in range(26):
            if (m*n)%26==1:
                Mod26invTable[m] = n
    
    Mdet26 = Mdet%26
    if Mdet26 in Mod26invTable:
        Mdetinv26 = Mod26invTable[Mdet26]
    else:
        Mdetinv26 = None
        print("No inverse found")
        exit()
    
    Madj = Mdet*Minv
    Madj26 = Madj%26
    Minv26 = (Mdetinv26*Madj26)%26
    Minv26 = np.matrix.round(Minv26, 0)%26
    
    return Minv26


def hill_enc(M, plaintext):
    c = ''
    tmp = []
    if len(plaintext)%3 != 0:
        plaintext = plaintext + 'x'*(3-len(plaintext)%3)
        
    plaintext_list = [ord(p)-97 for p in plaintext]
    Marr = np.array(M)
    
    for i in range(0, len(plaintext_list), 3):
        sublist = plaintext_list[i:i+3]
        subarr = np.array(sublist)
        subarr_enc = np.matrix.round(np.matmul(M, subarr)%26, 0)%26
        sublist_enc = subarr_enc.tolist()
        tmp.extend(sublist_enc)
    
    c = c.join(chr(x+97) for x in tmp)
    return c


def hill_dec(M, ciphertext):
    p = ''
    tmp = []
    
    ciphertext_list = [ord(x)-97 for x in ciphertext]    
    Marr = np.array(M)
    Minv = matrixinvmod26(Marr)
    
    for i in range(0, len(ciphertext_list), 3):
        sublist = ciphertext_list[i:i+3]
        subarr = np.array(sublist)
        subarr_dec = np.matrix.round(np.matmul(Minv, subarr)%26, 0)%26
        sublist_dec = subarr_dec.tolist()
        tmp.extend(sublist_dec)
        
    p = p.join(chr(int(x)+97) for x in tmp)
    return p
    
