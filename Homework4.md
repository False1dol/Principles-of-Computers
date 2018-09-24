Q1) The two's complement integer division algorithm discussed in class is known as the restoring method because the value in the A register must be restored following unsuccessful subtraction.  A slightly more complex approach, known as non restoring, avoids the unnecessary subtraction and addition.  Propose an algorithm for this approach.  

Ans.  

>   ![alt text](https://github.com/MrReese0/IFT510-Problems/blob/master/images/nonrestoring2.png)  
>   ![alt text](https://github.com/MrReese0/IFT510-Problems/blob/master/images/nonrestoring1.png)  
>   
>   
>   1) Put x in register A, d in register B, 0 in register P, and perform n divide steps (n is the quotient word length)  
>  
>   2) If P is negative  
>  (i-a) Shift the register pair (P,A) one bit left  
>  (ii-a) Add the contents of register B to P 
>  
>   3) If P is positive  
>  (i-b) Shift the register pair (P,A) one bit left  
>  (ii-b) Subtract the contents of register B from P  
>  (iii) If P is negative, set the low-order bit of A to 0,  
>     otherwise set it to 1  
>  
>    4) After n cycles  
>   (a) The quotient is in A  
>   (b) If P is positive, it is the remainder, otherwise it has to be restored  
>   (c) (add B to it) to get the remainder  



Q2) Divide -145 by 13 in binary twos complement, using 12-bit words.  Use the restoring method algorithm.  
Ans.  
  
> Since restoring method only works for unsigned integers, we'll divide 145 by 13 first. Then we'll take the two's complement of the quotient.
>  
>
>| Cycle | Operation      | A                                    | Q              | Q<sub>0</sub> |
>|-------|----------------|--------------------------------------|----------------|----|
>| 0     | Initialization |  0 0000 0000 0000                    | 0000 1001 0001 | -  |
>| 1     | Shift A        |  0 0000 0000 0000                    | 0001 0010 001  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0001 0010 001  | -  |
>|       | Set Q<sub>0</sub>         |= 1 1111 1111 0011                    | 0001 0010 001  | 0  |
>|       | Restore B      |+ 0 0000 0000 1101                    | 0001 0010 001  | 0  |
>|       |                |= 0 0000 0000 0000 (MSB = 1, ignored) | 0001 0010 001  | 0  |
>| 2     | Shift A        |  0 0000 0000 0000                    | 0010 0100 010  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0010 0100 010  | -  |
>|       | Set Q<sub>0</sub>         |= 1 1111 1111 0011                    | 0010 0100 010  | 0  |
>|       | Restore B      |+ 0 0000 0000 1101                    | 0010 0100 010  | 0  |
>|       |                |= 0 0000 0000 0000 (MSB = 1, ignored) | 0010 0100 010  | 0  |
>| 3     | Shift A        |  0 0000 0000 0000                    | 0100 1000 100  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0100 1000 100  | -  |
>|       | Set Q<sub>0</sub>         |= 1 1111 1111 0011                    | 0100 1000 100  | 0  |
>|       | Restore B      |+ 0 0000 0000 1101                    | 0100 1000 100  | 0  |
>|       |                |= 0 0000 0000 0000                    | 0100 1000 100  | 0  |
>| 4     | Shift A        |  0 0000 0000 0000                    | 1001 0001 000  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 1001 0001 000  | -  |
>|       | Set Q<sub>0</sub>         |+ 1 1111 1111 0011                    | 1001 0001 000  | 0  |
>|       | Restore B      |+ 0 0000 0000 1101                    | 1001 0001 000  | 0  |
>|       |                |= 0 0000 0000 0000                    | 1001 0001 000  | 0  |
>| 5     | Shift A        |  0 0000 0000 0001                    | 0010 0010 000  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0010 0010 000  | -  |
>|       | Set Q<sub>0</sub>         |= 1 1111 1111 0100                   | 0010 0010 000  | 0  |
>|       | Restore B      |+ 0 0000 0000 1101                    | 0010 0010 000  | 0  |
>|       |                |= 0 0000 0000 0001 (MSB = 1, ignored) | 0010 0010 000  | 0  |
>| 6     | Shift A        |  0 0000 0000 0010                    | 0100 0100 000  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0100 0100 000  | -  |
>|       | Set Q<sub>0</sub>         |= 1 1111 1111 0101                    | 0100 0100 000  | 0  |
>|       | Restore B      |+ 0 0000 0000 1101                    | 0100 0100 000  | 0  |
>|       |                |= 0 0000 0000 0010                    | 0100 0100 000  | 0  |
>| 7     | Shift A        |  0 0000 0000 0100                    | 1000 1000 000  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 1000 1000 000  | -  |
>|       | Set Q<sub>0</sub>         |= 1 1111 1111 0111                    | 1000 1000 000  | 0  |
>|       | Restore B      |+ 0 0000 0000 1101                    | 1000 1000 000  | 0  |
>|       |                |= 0 0000 0000 0100                    | 1000 1000 000  | 0  |
>| 8     | Shift A        |  0 0000 0000 1001                    | 0001 0000 000  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0001 0000 000  | -  |
>|       | Set Q<sub>0</sub>         |= 1 1111 1111 1100                    | 0001 0000 000  | 0  |
>|       | Restore B      |+ 0 0000 0000 1101                    | 0001 0000 000  | 0  |
>|       |                |= 0 0000 0000 1001                    | 0001 0000 000  | 0  |
>| 9     | Shift A        |  0 0000 0001 0010                    | 0010 0000 000  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0010 0000 000  | -  |
>|       | Set Q<sub>0</sub>         |= 0 0000 0000 0101 (MSB = 1, ignored) | 0010 0000 000  | 1  |
>| 10    | Shift A        |  0 0000 0000 1010                    | 0100 0000 001  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0100 0000 001  | -  |
>|       | Set Q<sub>0</sub>         |= 1 1111 1111 1101                    | 0100 0000 001  | 0  |
>|       | Restore B      |+ 0 0000 0000 1011                    | 0100 0000 001  | 0  |
>|       |                |= 0 0000 0000 1010 (MSB = 1, ignored) | 0100 0000 001  | 0  |
>| 11    | Shift A        |  0 0000 0001 0100                    | 1000 0000 010  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 1000 0000 010  | -  |
>|       | Set Q<sub>0</sub>         |= 0 0000 0000 0111                    | 1000 0000 010 | 1  |
>| 12    | Shift A        |  0 0000 0000 1111                    | 0000 0000 101  | -  |
>|       | Subtract B     |+ 1 1111 1111 0011                    | 0000 0000 101  | -  |
>|       | Set Q<sub>0</sub>         |= 0 0000 0000 0010 (MSB = 1,ignored)  | 0000 0000 101  | 1  |
>
>
> Quotient = 0000 0000 1011 (11)  
> 2's complement of Quotient = 1111 1111 0101 (-11)  
> Remainder = 0000 0000 0010 (2)  
> -145 / 13 = -11(Q) + 2(R)  
