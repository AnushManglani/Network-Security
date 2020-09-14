# anush, 116801027

from Crypto.Cipher import AES

def byteseq2binstr(byteseq):
    # first convert to a list string binary representations of each byte
    bitslist2 = [bin(int(b))[2:].zfill(8) for b in byteseq]
    
    # then merge all those strings
    allbitsstr = ''.join(bitslist2)
    
    return allbitsstr



def XORbits(bitstr1,bitstr2):
    # Both bit strings should be the same length
    # output will be a string with the same length
    B1 = [int(q) for q in bitstr1]
    B2 = [int(w) for w in bitstr2]
    xor_result = ''.join([str(d^f) for d,f in zip(B1, B2)])
    
    return xor_result


def invertbit(inputblock, b):
    inputblockstr = byteseq2binstr(inputblock)
    xorstr = '0'*(b) + '1' + '0'*(127-b)
    res = XORbits(inputblockstr, xorstr)
    return int(res, 2).to_bytes(len(res) // 8, byteorder='big')


def findbitdiff(originalcipher, newcipher):
    orig = byteseq2binstr(originalcipher)
    new = byteseq2binstr(newcipher)
    count = 0
    for i in range(0, len(orig)):
        if orig[i] != new[i]:
            count = count+1
    
    return count



def aes_input_av_test(inputblock, key, bitlist):
    # inputblock and key are 16 byte values each
    # bitlist is a list of integers that define the position of the
    # bit in the inputblock that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    cipher = AES.new(key, AES.MODE_ECB)
    originalcipher = cipher.encrypt(inputblock)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the inputblock (doesn't have to be in this exact
        # function form)
        newinput = invertbit(inputblock, b)
        
        # perform encryption
        newcipher = cipher.encrypt(newinput)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        # Use any method you like to find the difference. 
        numbitdifferences = findbitdiff (originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list

# aes_input_av_test(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10', b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98', [0, 7, 6, 25, 78, 127])


# We also perform similar experiment by keeping the inputblocl fixed and changing the
# selected bits of the key
def aes_key_av_test(inputblock, key, bitlist):
    # inputblock and key are 16 byte values each
    # bitlist is a list of integers that define the position of the
    # bit in the key that needs to be inverted, one at a time, for example
    # [0, 3, 6, 25, 78, 127]
    
    # 1- any initializations necessary
    diff_list = []
    
    # 2- perform encryption of the original values
    #    anyway you like. It doesn't have to be with 
    #    with this exact function form
    cipher = AES.new(key, AES.MODE_ECB)
    originalcipher = cipher.encrypt(inputblock)
    
    # 3- for every value given in the bitlist:
    for b in bitlist:
        #invert the value of the corresponding bit in the key (doesn't have to be in this exact
        # function form)
        newkey = invertbit(key, b)
        cipher = AES.new(newkey, AES.MODE_ECB)
        # perform encryption
        newcipher = cipher.encrypt(inputblock)
        
        # find the number of bit differences between the two ciphertexts (doesn't have to be exactly in
        # this function form)
        numbitdifferences = findbitdiff (originalcipher, newcipher)
        
        # add it to the list
        diff_list.append(numbitdifferences)
        
    # return the list of numbers
    return diff_list

# aes_key_av_test(b'\x01\x23\x45\x67\x89\xab\xcd\xef\xfe\xdc\xba\x98\x76\x54\x32\x10', b'\x0f\x15\x71\xc9\x47\xd9\xe8\x59\x0c\xb7\xad\xd6\xaf\x7f\x67\x98', [0, 7, 6, 25, 78, 127])

