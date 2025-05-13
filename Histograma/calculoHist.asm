.include "macro.asm"
.data
filename:      .string "freque_red.bin"  
.align 2

buffer:        .space 21120                # Buffer de 1KB
frequencia: 	.space 1024
msg_concluida:   .string "\nLeituras realizadas: "
error_open:    .string "\nErro ao abrir o arquivo!"
error_read:    .string "\nErro ao ler o arquivo!"
newline:       .string "\n"
pixel:         .string "pixel "
ocorrencia:     .string " calc ocorrencia "
.text
.globl main

main:
  										# abrir arquivo 
    li a7, 1024            
    la a0, filename          
    li a1, 0                 					# read
    ecall
    
    bltz a0, open_error      		#  erro de abertura
    mv s0, a0                				# Salvar descritor

    # Ler arquivo (syscall 63)
    li a7, 63
    mv a0, s0                # Descritor
    la a1, buffer            # Endereço do buffer

    li a2, 21120              # Tamanho máximo
    ecall
    
    bltz a0, read_error      # Tratar erro de leitura
    mv s1, a0                			# salvar bytes

    # fechar arquivo
    li a7, 57
    mv a0, s0 					# passo o descritor que esta salvo em s0 para o a0, para poder fechar o arquivo 
    ecall

    la a0, msg_concluida
    li a7, 4
    ecall
    
    mv a0, s1						#qnt de bytes
    li a7, 1
    ecall
    
    la a0, newline
    li a7, 4
    ecall

    									# Loop de impressão dos bytes
    li t0, 0                 				# cont
    la t1, buffer            			# pointer
    la s0, frequencia        	#256 x 4
    
calcular_freq:
    bge t0, s1, result
    lbu t6, 0(t1)              			# carregar byte sem sinal
    slli t3,t6, 2 					#shift pra esquerda 2 vezes
    add t4, s0, t3 				# enderço de frequcia += a intensidade do pixel * 4		
    lw t5, 0(t4)
    addi t5,t5,1
    sw t5,0(t4)
    addi t1, t1, 1           
    addi t0, t0, 1          
    j calcular_freq

open_error:
    la a0, error_open
    li a7, 4
    ecall
    j exit

read_error:

    la a0, error_read
    li a7, 4
    ecall
  							  # fechar arquivo se aberto
    li a7, 57
    mv a0, s0
    ecall
    j exit
    
result:
    li t1,0
    li t2,256
print_freq:	
    beq t1,t2, exit				#chamando os labels com a string
    print_string_from_label(pixel)
    print_inteiro(t1)
    print_string_from_label(ocorrencia)
    slli t3, t1, 2
    add t4, t3, s0
    lw a0, 0(t4)
    li a7, 1
    ecall
    print_newline()
    addi t1,t1,1
    j print_freq
exit:
    li a7, 10               
    ecall
