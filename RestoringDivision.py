def spacer(strnum):
    newstr = ""
    for i in range(len(strnum)):
        if i % 4 == 0:
            newstr += " " + strnum[i]
        else:
            newstr += strnum[i]
    return newstr
def twos_complement(val, bits):                                                             
                                                                                            
                                                                        
    if (val & (1 << (bits - 1))) != 0:                                                      # if sign bit is set e.g., 
        val = val - (1 << bits)                                                             # 8bit: 128-255, compute the 
    return(val & ((2 ** bits) - 1))                                                         # negative value.

def decimal_to_binary_12bit(num):                                                            
                                                                                            
    
    if num < 0:                                                                             # If the number is negative, pass 
        return decimal_to_binary_12bit(twos_complement(num, 12))                              # it through the two's complement
                                                                                            # function.

    elif num > 4095:                                                                         # If the number is greater than 4095,
        return format(num, '012b')[1:]                                                       # i.e., 2^8 - 1, then ignore the MSB.
    
    else:
        return (format(num, '012b'))                                                         
    
def left_shift13bit(strnum):                                                                   
                                                                                        
    return strnum[1:13]

def left_shift12bit(strnum):

    return [strnum[1:13],strnum[0]]

def binary_adder(strnumA, strnumB):                                                         
    
    strsum = ''                                                                             # String storing the sum.
    
    carryover = 0                                                                           # Carryover from addition, if any.
    
    for i in range(len(strnumA)-1,-1,-1):                                                   # Iterating over the digits, doing
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

def restoring_division(a_register, quotient, divisor, divisor_complement):
    i = 0
    while(i < 12):
        a_register = left_shift13bit(a_register) + left_shift12bit(quotient)[1]
        quotient = left_shift12bit(quotient)[0]
        a_register = binary_adder(a_register, divisor_complement)
        if a_register[0] == '1':
            quotient += '0'
            a_register = binary_adder(a_register, divisor)
        else:
            quotient += '1'
        i += 1
    print("Remainder = " + a_register)
    print("Quotient = " + quotient)


a = '0' + decimal_to_binary_12bit(0)
q = decimal_to_binary_12bit(145)
b = '0' + decimal_to_binary_12bit(13)
b_comp = '1' + decimal_to_binary_12bit(-13)
restoring_division(a,q,b,b_comp)
