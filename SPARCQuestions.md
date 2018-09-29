15. 11 SPARC is lacking a number of instructions commonly found on CISC machines.

Some of these are easily simulated using either register R0, which is always set to 0,

or a constant operand. These simulated instructions are called pseudo instructions and

are recognized by the SPARC assembler. Show how to simulate the following pseudo instructions,

each with a single SPARC instruction. In all of these, src and dst refer

to registers. (Hint: A store to R0 has no effect.)

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

1. OR src with Go and store the result in dst.
2. SUBCC src2 from src1 and store the result in G0.
3. ORCC src1 with G0 and store the result in G0.
4. XNOR dst with G0.
5. SUB dst from G0 and store in dst.
6. ADD 1 to dst (immediate operand).
7. SUB 1 from dst (immediate operand).
8. OR G0 with G0 and store in dst.
9. SETHI G0 with 0.















15.12 Consider the following code fragment:

if K \&gt; 10

L := K + 1

Else

L := K - 1;

A straightforward translation of this statement into SPARC assembler could take the

following form:

Sethi  %hi(K), %r8    ;load high-order 22 bits of address of

;location K into register r8

ld   [%r8 + %lo(K)], %r8   ;load contents of location K into r8

cmp   %r8, 10    ;compare contents of r8 with 10

ble   L1     ;branch if (r8) \&lt;= 10

nop

sethi   %hi(K), %r9

ld   [%r9 + %lo(K)], %r9   ;load contents of location K into r9

inc   %r9     ;add 1 to (r9)

sethi   %hi(L), %r10

st   %r9, [%r10 + %lo(L)]   ;store (r9) into location L

b   L2

Nop

L1:  sethi   %hi(K), %r11

ld   [%r11 + %lo(K)], %r12  ;load contents of location K into r12

dec   %r12     ;subtract 1 from (r12)

sethi   %hi(L), %r13

st   %r12, [%r13 + %lo(L)]  ;store (r12) into location L

L2:

The code contains a nop after each branch instruction to permit delayed branch

Operation.

a. Standard compiler optimizations that have nothing to do with RISC machines are

generally effective in being able to perform two transformations on the foregoing

code. Notice that two of the loads are unnecessary and that the two stores can be

merged if the store is moved to a different place in the code. Show the program

after making these two changes.

b. It is now possible to perform some optimizations peculiar to SPARC. The nop

after the ble can be replaced by moving another instruction into that delay slot

and setting the annul bit on the ble instruction (expressed as ble,a L1). Show the

program after this change.

c. There are now two unnecessary instructions. Remove these and show the resulting

program.

Ans.

1.

sethi  %hi(K), %r8    ;load high-order 22 bits of address of

;location K into register r8

ld   [%r8 + %lo(K)], %r8   ;load contents of location K into r8

cmp   %r8, 10    ;compare contents of r8 with 10

ble   L1     ;branch if (r8) \&lt;= 10

nop

inc   %r8    ;add 1 to (r8)

b   L2

nop

L1:  dec   %r8    ;subtract 1 from (r12)

L2: sethi   %hi(K), %r10

 st   %r8, [%r10 + %lo(L)]  ;store (r8) into location L.

1.

sethi  %hi(K), %r8    ;load high-order 22 bits of address of

;location K into register r8

ld   [%r8 + %lo(K)], %r8   ;load contents of location K into r8

cmp   %r8, 10    ;compare contents of r8 with 10

ble.a  L1     ;branch if (r8) \&lt;= 10

dec   %r8    ;subtract 1 from (r8)

inc   %r8    ;add 1 to (r8)

b   L2

nop

L1:

L2: sethi   %hi(L), %r10

 st   %r8, [%r10 + %lo(L)]   ;store (r8) into location L.



1.

sethi  %hi(K), %r8    ;load high-order 22 bits of address of

;location K into register r8

ld   [%r8 + %lo(K)], %r8   ;load contents of location K into r8

cmp   %r8, 10    ;compare contents of r8 with 10

ble.a  L1     ;branch if (r8) \&lt;= 10

dec   %r8    ;subtract 1 from (r8)

inc   %r8    ;add 1 to (r8)

L2: sethi   %hi(L), %r10

 st   %r8, [%r10 + %lo(L)]   ;store (r8) into location L.
