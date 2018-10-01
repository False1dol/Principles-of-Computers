15. 11 SPARC is lacking a number of instructions commonly found on CISC machines. Some of these are easily simulated using either register R0, which is always set to 0, or a constant operand. These simulated instructions are called pseudo instructions and are recognized by the SPARC assembler. Show how to simulate the following pseudo instructions, each with a single SPARC instruction. In all of these, src and dst refer to registers. (Hint: A store to R0 has no effect.)  
    a. MOV src, dst  
    b. COMPARE src1, src2  
    c. TEST src1  
    d. NOT dst  
    e. NEG dst  
    f. INC dst  
    g. DEC dst  
    h. CLR dst  
    i. NOP  

    Ans.  

>    1. OR src with G0 and store the result in dst.
>    2. SUBCC src2 from src1 and store the result in G0.
>    3. ORCC src1 with G0 and store the result in G0.
>    4. XNOR dst with G0.
>    5. SUB dst from G0 and store in dst.
>    6. ADD 1 to dst (immediate operand).
>    7. SUB 1 from dst (immediate operand).
>    8. OR G0 with G0 and store in dst.
>    9. SETHI G0 with 0.

![alt text](https://github.com/MrReese0/IFT510-Problems/blob/master/images/Activity2Q2.png)  
  
  Ans.  
  
  
>    ![alt text](https://github.com/MrReese0/IFT510-Problems/blob/master/images/Activity2A2.png)    

