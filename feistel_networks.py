# anush, 116801027

import numpy as np
import random
import hmac, hashlib
def xor(byteseq1, byteseq2):
    # First we convert each byte to its int value
    l1 = [b for b in byteseq1]
    l2 = [b for b in byteseq2]

    l1xorl2 = [bytes([elem1^elem2]) for elem1,elem2 in zip(l1,l2)]
    result = b''.join(l1xorl2)

    return result


def F(byteseq, k):
    h = hmac.new(k, byteseq, hashlib.sha1)
    return h.digest()[:4]


def feistel_block(LE_inp, RE_inp, k):
    LE_out = RE_inp
    f = F(RE_inp, k)
    RE_out = xor(LE_inp, f)
    
    return LE_out, RE_out
    


def gen_keylist(keylenbytes, numkeys, seed):
    # We need to generate numkeys keys each being keylen bytes long
    keylist = []
    np.random.seed(seed)

    for i in range(0, numkeys):
        keylist.append(b''.join([x.to_bytes(1, byteorder='big') for x in np.random.randint(255, size=(keylenbytes,)).tolist()]))
        
    return keylist

# gen_keylist(4, 8, 80)


def feistel_enc(inputblock, num_rounds, seed):
    keylist = gen_keylist(4, num_rounds, seed)
    LE, RE = inputblock[:4], inputblock[4:]
    for i in range(0, num_rounds):
        LE, RE = feistel_block(LE, RE, keylist[i])
        
    cipherblock = RE+LE
    return cipherblock

# print("The ciphertext is: ", feistel_enc(b'anush123', 8, 80))


def feistel_enc_test(input_fname, seed, num_rounds, output_fname):
    
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    inpbyteseq = inpbyteseq[:-1]
    
    fout = open(output_fname, 'wb')
#     print(inpbyteseq)

    if len(inpbyteseq)%8 != 0:
        inpbyteseq = inpbyteseq + b'\x20'*(8-len(inpbyteseq)%8)
#     print(inpbyteseq)
    for i in range(0, len(inpbyteseq), 8):
        inputbytelist = inpbyteseq[i:i+8]
#         print("plaintext block is: ", inputbytelist)
        encbytes = feistel_enc(inputbytelist, num_rounds, seed)
#         print("encryption block is: ", encbytes)
        fout.write(encbytes)
    
    fout.close()

# feistel_enc_test('plaintext.txt', 80, 8, 'ciphertext.txt')



def feistel_dec(inputblock, num_rounds, seed):
    
    keylist = gen_keylist(4, num_rounds, seed)
#     print(keylist)
    LE, RE = inputblock[:4], inputblock[4:]
    for i in range(0, num_rounds):
        LE, RE = feistel_block(LE, RE, keylist[num_rounds-1-i])
#         print("after round " + str(i) + " the block is: ", (LE+RE), " with key :", keylist[num_rounds-1-i])
    
    plainblock = RE+LE
    return plainblock

# feistel_dec(b'\x1d\xc9\xff\xbb\xc8wO\xcc', 8, 80)



def feistel_dec_test(input_fname, seed, num_rounds, output_fname):
    
    # First read the contents of the input file as a byte sequence
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
#     inpbyteseq = inpbyteseq[:-1]
    fout = open(output_fname, 'wb')
    
#     print(inpbyteseq)
    # Then break the inpbyteseq into blocks of 8 bytes long and 
    # put them in a list
    # Pad the last element with spaces b'\x20' until it is 8 bytes long
    # blocklist = [list of 8 byte long blocks]
    
    # Loop over al blocks and use the feistel_dec to generate the plaintext block
    # append all plainblocks together to form the output byte sequence
    # plainbyteseq = b''.join([list of plain blocks])
    
    # write the plainbyteseq to output file
    
    for i in range(0, len(inpbyteseq), 8):
        inputbytelist = inpbyteseq[i:i+8]
#         print("ciphertext block is: ", inputbytelist)
        decbytes = feistel_dec(inputbytelist, num_rounds, seed)
#         print("plaintext block is: ", decbytes)
        fout.write(decbytes)
        
    fout.close()
   


# feistel_enc_test('plaintext.txt', 80, 8, 'ciphertext.txt')

# feistel_dec_test('ciphertext.txt', 80, 8, 'output_plaintext.txt')

