def dectobin8bit(num):
    if num < 0:
        return dectobin8bit(twos_complement(num, 8))
    elif num > 255:
        return format(num, '08b')[1:]
    else:
        return (format(num, '08b'))
    
def rightshift(strnum):
    print("oldstrm " + strnum)
    if strnum[0] == '0':
        strnum = '0' + strnum
    elif strnum[0] == '1':
        strnum = '1' + strnum
    print("newstrm " + strnum)
    return [strnum[:16],strnum[-1]]

def twos_complement(val, bits):
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return(val & ((2 ** bits) - 1))
     
def boothmultiply(multiplier, multiplicand, product, boothbit, i):
    while i < 8:                                                            #For 8-bit Multiplication,
                                                                            #there will be 8 iterations
                                                                            #of bit shifting                              
        opbits = product[-1] + boothbit
        print(opbits)
        if opbits == '00':                                                  #00 Op Code = No-op
            
            result = rightshift(product)                                    #Right shifting the Product
            
            product = result[0]                                             #Storing the result into
                                                                            #Product after right-
                                                                            #shifting the bits

            boothbit = result[1]                                            #Storing the Booth bit
            
        elif opbits == '10':                                                #10 Op Code = Subtract Multiplicand
            
            productsum = int(product[:8],2) - int(multiplicand,2)           #Integer subtraction of the first
                                                                            #8 bits of the Product from the
                                                                            #Multiplicand
            
            product = dectobin8bit(productsum) + product[8:]                #Storing the 8 bits of the Product
                                                                            #sum and the remaining 8 Bits of the
                                                                            #original Product
            
            result = rightshift(product)                                    #Right shifting the Product
            
            product = result[0]                                             #Storing the Result in Product
            
            boothbit = result[1]                                            #Storing the Booth bit
            
        elif opbits == '01':                                                #01 Op Code = Add Multiplicand
            
            productsum = int(product[:8],2) + int(multiplicand,2)           #Integet addition of the first 8
                                                                            #bits of the product and the
                                                                            #Multiplicand
            
            product = dectobin8bit(productsum) + product[8:]                #Storing the 8 bits of the Product
                                                                            #sum and remaining 8 bits of the
                                                                            #original Product
            
            result = rightshift(product)                                    #Right shifting the Product
            
            product = result[0]                                             #Storing the Result in Product
            
            boothbit = result[1]                                            #Storing the Booth bit
            
        elif opbits == '11':                                                #11 Op Code = No-op
            
            result = rightshift(product)                                    #Storing the result into Product
                                                                            #after right-shifting the bits
            
            product = result[0]                                             #Storing the Result in Product
            
            boothbit = result[1]                                            #Storing the Booth bit
            
        i += 1                                                              #Incrementing i value of the loop
    print(product)

boothmultiply(dectobin8bit(3),dectobin8bit(-6),'00000000'+dectobin8bit(3),str(0),0)
