

BookInitPermOrder = [58,50,42,34,26,18,10,2,
                   60,52,44,36,28,20,12,4,
                   62,54,46,38,30,22,14,6,
                   64,56,48,40,32,24,16,8,
                   57,49,41,33,25,17,9,1,
                   59,51,43,35,27,19,11,3,
                   61,53,45,37,29,21,13,5,
                   63,55,47,39,31,23,15,7]

BookInvInitPermOrder = [40, 8, 48, 16, 56, 24, 64, 32,
                        39, 7, 47, 15, 55, 23, 63, 31,
                        38, 6, 46, 14, 54, 22, 62, 30,
                        37, 5, 45, 13, 53, 21, 61, 29,
                        36, 4, 44, 12, 52, 20, 60, 28,
                        35, 3, 43, 11, 51, 19, 59, 27,
                        34, 2, 42, 10, 50, 18, 58, 26,
                        33, 1, 41,  9, 49, 17, 57, 25 ]

E_TABLE = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,
16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

SBOX = [
# Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# Box-2

[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],

# Box-3

[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

],

# Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],

# Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# Box-6

[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

],
# Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# Box-8

[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]

]

DECtoBIN4 = {0: '0000',
            1: '0001',
            2: '0010',
            3: '0011',
            4: '0100',
            5: '0101',
            6: '0110',
            7: '0111',
            8: '1000',
            9: '1001',
            10: '1010',
            11: '1011',
            12: '1100',
            13: '1101',
            14: '1110',
            15: '1111'}

PermBook = [16, 7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26, 5, 18, 31, 10,
             2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25]

PC1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]

shift = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

KeyList = []



def byteseq2binstr(byteseq):
    # first convert to a list string binary representations of each byte
    bitslist2 = [bin(int(b))[2:].zfill(8) for b in byteseq]
    
    # then merge all those strings
    allbitsstr = ''.join(bitslist2)
    
    return allbitsstr



def Permutation(bitstr, permorderlist):
    permedbitstr = ''.join([bitstr[b] for b in [x-1 for x in permorderlist]])
    return permedbitstr



def Expansion(inputbitstr32, e_table):
    # the input string is 32 bits long and the output string will be 48 bits long or
    # to be more exact, it will be as long as the e_table (which is 48 bits for DES)
    
    # create output empty string
    outputbitstr48 = ''.join([inputbitstr32[b] for b in [x-1 for x in e_table]])

    # add proper elements from the inputbitstr32 according to the e_table
    
    return outputbitstr48



def XORbits(bitstr1,bitstr2):
    # Both bit strings should be the same length
    # output will be a string with the same length
    B1 = [int(q) for q in bitstr1]
    B2 = [int(w) for w in bitstr2]
    xor_result = ''.join([str(d^f) for d,f in zip(B1, B2)])
    
    return xor_result


def sbox_lookup(input6bitstr, sboxindex):
    # find the row index (0-3)
    # find the col index (0-7)
    row = int(input6bitstr[0]+input6bitstr[5], base=2)
    col = int(input6bitstr[1:5],base=2)
    sbox_value = SBOX[sboxindex][row][col]
    
    # Need to convert to 4 bits binary string    
    return DECtoBIN4[sbox_value]



def functionF(bitstr32, keybitstr48):
    
    # return the result
    e = Expansion(bitstr32, E_TABLE)
#     print("Expansion: ",e)
    x = XORbits(e, keybitstr48)
#     print("XOR: ",x)
    sub6list = [x[i:i+6] for i in range(0,len(x), 6)]
#     print("sub6list: ", sub6list)
    s = ''.join([sbox_lookup(a, ind) for a,ind in zip(sub6list, [0,1,2,3,4,5,6,7])])
#     print("SBOX: ", s)
    outbitstr32 = Permutation(s, PermBook)
    return outbitstr32

# functionF('00010010111110101010101000001111', '000000000000000000010010111110101010101000001111')




def des_keygen(C_inp, D_inp, roundindex):
    # Implement Figure 6
    C_out, D_out = C_inp[shift[roundindex]:]+C_inp[0:shift[roundindex]], D_inp[shift[roundindex]:]+D_inp[0:shift[roundindex]]
    key48 = Permutation(C_out+D_out, PC2)
    return key48, C_out, D_out

# des_keygen('0100100001001000010010001111', '0100100001001000010010001010', 2)



def des_round(LE_inp32, RE_inp32, key48):
    # LEinp and REinp are the outputs of the previous round
    # k is the key for this round which usually has a different 
    # value for different rounds
    LE_out32 = RE_inp32
    RE_out32 = XORbits(LE_inp32, functionF(RE_inp32, key48))
#     print("LE_out32: ", LE_out32)
#     print("RE_out32: ", RE_out32)
    return LE_out32, RE_out32

# des_round('01001000010010000100100011110011', '01001000010010000100100010101110', '001100110000110011100000001010001000101101000100')



def des_enc(inputblock, num_rounds, inputkey64):
    # This is the function that accepts one bloc of plaintext
    # and applies all rounds of the DES cipher and returns the
    # cipher text block. 
    # Inputs:
    # inputblock: byte sequence representing input block
    # num_rounds: integer representing number of rounds in the feistel 
    # key: byte sequence (8 bytes)
    # Output:
    # cipherblock: byte sequence    
    byteSeq = Permutation(byteseq2binstr(inputblock), BookInitPermOrder)
    LE, RE = byteSeq[:32], byteSeq[32:]
    keystr = byteseq2binstr(inputkey64)
    key56 = Permutation(keystr, PC1)
    C, D = key56[:28], key56[28:]
    for i in range(0, num_rounds):
        key48, C, D = des_keygen(C, D, i)
        KeyList.append(key48)
    
    for i in range(0, num_rounds):
        LE, RE = des_round(LE, RE, KeyList[i])
    
    temp = Permutation(RE+LE, BookInvInitPermOrder)
    cipherblock = int(temp, 2).to_bytes(len(temp) // 8, byteorder='big')
#     print(len(cipherblock.hex()))
    return cipherblock

# des_enc(b'shreyans', 16, b'12345678')


def des_dec(inputblock, num_rounds, inputkey64):
    # This is the function that accepts one bloc of ciphertext
    # and applies all rounds of the DES cipher and returns the
    # plaintext text block. 
    # Inputs:
    # inputblock: byte sequence representing ciphertext block
    # num_rounds: integer representing number of rounds in the feistel 
    # key: byte sequence (8 bytes)
    # Output:
    # plainblock: byte sequence    
    byteSeq = Permutation(byteseq2binstr(inputblock), BookInitPermOrder)
    LE, RE = byteSeq[:32], byteSeq[32:]
    keystr = byteseq2binstr(inputkey64)
    key56 = Permutation(keystr, PC1)
    C, D = key56[:28], key56[28:]
    for i in range(0, num_rounds):
        key48, C, D = des_keygen(C, D, i)
        KeyList.append(key48)
    
    for i in range(0, num_rounds):
        LE, RE = des_round(LE, RE, KeyList[num_rounds-1-i])
    
    temp = Permutation(RE+LE, BookInvInitPermOrder)
    plainblock = int(temp, 2).to_bytes(len(temp) // 8, byteorder='big')
    
    return plainblock

# des_dec(b'WF\xa9\x1a\xef\xd7\xee\x92', 16, b'12345678')


def des_enc_test(input_fname, inputkey64, num_rounds, output_fname):
    
    # inputkey64: byte sequence (8 bytes)
    # numrounds: asked since your feistel already has it but we always use 16 for DES
    
    # First read the contents of the input file as a byte sequence
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    inpbyteseq = inpbyteseq[:-1]
    # Then break the inpbyteseq into blocks of 8 bytes long and 
    # put them in a list
    # Pad the last element with spaces b'\x20' until it is 8 bytes long
    # blocklist = [list of 8 byte long blocks]
    
    # Loop over al blocks and use the dec_enc to generate the cipher block
    # append all cipherblocks together to form the outut byte sequence
    # cipherbyteseq = b''.join([list of cipher blocks])
    
    # write the cipherbyteseq to output file
    fout = open(output_fname, 'wb')
    if len(inpbyteseq)%8 != 0:
        inpbyteseq = inpbyteseq + b'\x20'*(8-len(inpbyteseq)%8)
    
#     print(len(inpbyteseq))
    
    for i in range(0, len(inpbyteseq), 8):
        inputbytelist = inpbyteseq[i:i+8]
        encbytes = des_enc(inputbytelist, num_rounds, inputkey64)
        fout.write(encbytes)
      
    fout.close()
    




def des_dec_test(input_fname, inputkey64, num_rounds, output_fname):
    
    # inputkey64: byte sequence (8 bytes)
    # numrounds: asked since your feistel already has it but we always use 16 for DES
    
    # First read the contents of the input file as a byte sequence
    finp = open(input_fname, 'rb')
    inpbyteseq = finp.read()
    finp.close()
    
    # Then break the inpbyteseq into blocks of 8 bytes long and 
    # put them in a list
    # Pad the last element with spaces b'\x20' until it is 8 bytes long
    # blocklist = [list of 8 byte long blocks]
    
    # Loop over al blocks and use the dec_enc to generate the cipher block
    # append all cipherblocks together to form the outut byte sequence
    # cipherbyteseq = b''.join([list of cipher blocks])
    
    # write the cipherbyteseq to output file
    fout = open(output_fname, 'wb')
    
    for i in range(0, len(inpbyteseq), 8):
        inputbytelist = inpbyteseq[i:i+8]
#         print("ciphertext block is: ", inputbytelist)
        decbytes = des_dec(inputbytelist, num_rounds, inputkey64)
#         print("plaintext block is: ", decbytes)
        fout.write(decbytes)
        
    fout.close()
    




