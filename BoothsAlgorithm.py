def twos_complement(val, bits):                                         # Function for finding the 2's
                                                                        # complement of a binary number.
                                                                        
    if (val & (1 << (bits - 1))) != 0:                                  # if sign bit is set e.g., 
        val = val - (1 << bits)                                         # 8bit: 128-255, compute the 
    return(val & ((2 ** bits) - 1))                                     # negative value.

def decimal_to_binary_8bit(num):                                        # Function for Converting Decimals
                                                                        # to 8-bit Binaries
    
    if num < 0:                                                         # If the number is negative, pass 
        return decimal_to_binary_8bit(twos_complement(num, 8))          # it through the two's complement
                                                                        # function.

    elif num > 255:                                                     # If the number is greater than 255,
        return format(num, '08b')[1:]                                   # i.e., 2^8 - 1, then ignore the MSB.
    
    else:
        return (format(num, '08b'))                                     # Else, just return the binary number.
    
def right_shift(strnum):                                                # Function for right shifting a
                                                                        # Binary number.
                                                                        
    if strnum[0] == '0':                                                # If MSB of the number is 1, the
        strnum = '0' + strnum                                           # first bit of the shifted number is
                                                                        # also 1 to maintain signed magnitude.
    elif strnum[0] == '1':
        strnum = '1' + strnum
        
    return [strnum[:16],strnum[-1]]

def binary_adder(strnumA, strnumB):                                     # Function to add two binary numbers
    
    strsum = ''                                                         # String storing the sum.
    
    carryover = 0                                                       # Carryover from addition, if any.
    
    for i in range(len(strnumA)-1,-1,-1):                               # Iterating over the digits, doing
                                                                        # bit-by-bit addition and taking care
                                                                        # of the carryover.
        if strnumA[i] == '0' and strnumB[i] == '0':
            if carryover == 0:
                strsum = '0' + strsum
                carryover = 0
            else:
                strsum = '1' + strsum
                carryover = 0
        elif (strnumA[i] == '0' and strnumB[i] == '1') or (strnumA[i] == '1' and strnumB[i] == '0'):
            if carryover == 0:
                strsum = '1' + strsum
                carryover = 0
            else:
                strsum = '0' + strsum
                carryover = 1
        elif strnumA[i] == '1' and strnumB[i] == '1':
            if carryover == 1:
                strsum = '1' + strsum
                carryover = 1
            else:
                strsum = '0' + strsum
                carryover = 1
                
    return strsum


     
def booth_multiply(multiplier, multiplicand, negative_multiplicand, product, boothbit, i):  # Function for performing the
                                                                                            # Booth's Algorithm.
    
    while i < 8:                                                                            # For 8-bit Multiplication,
                                                                                            # there will be 8 iterations
                                                                                            # of bit shifting.                            
        opbits = product[-1] + boothbit

        if opbits == '00':                                                                  # '00' Op Code = No operation.
            
            result = right_shift(product)                                                   # Right shifting the Product.
            
            product = result[0]                                                             # Storing the result into
                                                                                            # Product after right-
                                                                                            # shifting the bits.

            boothbit = result[1]                                                            # Storing the Booth bit.
            
        elif opbits == '10':                                                                # '10' Op Code = Subtract
                                                                                            # Multiplicand.
            
            productsum = binary_adder(product[:8], negative_multiplicand)                   #Binary addition of the first
                                                                                            #8 bits of the Product and the
                                                                                            #negative of the Multiplicand.
            
            product = productsum + product[8:]                                              # Storing the 8 bits of the 
                                                                                            # Product sum and the remaining 
                                                                                            # 8 Bits of the original
                                                                                            # Product.
            
            result = right_shift(product)                                                   # Right shifting the Product.
            
            product = result[0]                                                             # Storing the Result in Product.
            
            boothbit = result[1]                                                            # Storing the Booth bit.
            
        elif opbits == '01':                                                                # '01' Op Code = Add Multiplicand.
            
            productsum = binary_adder(product[:8], multiplicand)                            # Integet addition of the first 8
                                                                                            # bits of the product and the
                                                                                            # Multiplicand.
            
            product = productsum + product[8:]                                              # Storing the 8 bits of the Product
                                                                                            # sum and remaining 8 bits of the
                                                                                            # original Product.
            
            result = right_shift(product)                                                   # Right shifting the Product.
            
            product = result[0]                                                             # Storing the Result in Product.
            
            boothbit = result[1]                                                            # Storing the Booth bit.
            
        elif opbits == '11':                                                                # '11' Op Code = No operation.
            
            result = right_shift(product)                                                   # Storing the result into Product
                                                                                            # after right-shifting the bits.
            
            product = result[0]                                                             # Storing the Result in Product.
            
            boothbit = result[1]                                                            # Storing the Booth bit.
            
        i += 1                                                                              # Incrementing i value of the loop.
    print(product)

mplier = decimal_to_binary_8bit(-105)                                                       # Multiplier Variable.

mplicand = decimal_to_binary_8bit(-29)                                                      # Multiplicand Variable.

negative_mplicand = decimal_to_binary_8bit(29)                                              # Negative of the Multiplicand.

booth_multiply(mplier, mplicand, negative_mplicand, '00000000' + mplier, str(0), 0)
