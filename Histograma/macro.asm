
.macro print_inteiro(%x)
    add a0, %x, zero	#add 0 a um registrador que possui um valor a ser printado 
    li a7, 1
    ecall
.end_macro

.macro print_string_from_label(%s)
    la a0, %s		#pega a label que possui uma string demarcada e printa
    li a7, 4
    ecall
.end_macro

.macro print_newline
    addi a0, zero, 10	#função para quebra de linha
    li a7, 11
    ecall
.end_macro

.macro fill_zero(%pointer, %count)
    addi sp, sp, -12	#preencher os espaçços (lixo) com zeros
    sw t1, (sp)
    sw t2, 4(sp)	#usa os reg e depois devolve eles
    sw t0, 8(sp)
    li t0, 0
    li t2, %count
    
fill_zero_loop:
   beq t2, t0, exit_fill_zero	#usando para verificar os espaços da memoria 
   slli t1, t0, 2
   add t1, t1, %pointer
   sw zero, (t1)
   addi t0, t0, 1 
   j fill_zero_loop
   
exit_fill_zero:
    lw t1, (sp)			#devolver os reg
    lw t2, 4(sp)
    lw t0, 8(sp)
    addi sp, sp, 12
.end_macro
