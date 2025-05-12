.include "macro.asm"

.data
buffer:        .space 21120                # Buffer de 1KB
newline:       .string "\n"
.align 2
filename_green:      .string "freque_green.bin"
.align 2
output_green:        .string "histograma_equalizador_green.txt" 
.align 2
output_bin_green:    .string "bin_bytes_green.bin"
.align 2

pixel:         .string  "Pixel \0"
.align 2
frequencia:     .string  " - ocorrencia "
.align 2
total_acumulado:.word 0
pixel_count: 	.space 1024
success_msg:   .string "\nLeitura concluída. Bytes lidos: "
.align 2
error_open:    .string "\nErro ao abrir o arquivo!" 
.align 2
error_read:    .string "\nErro ao ler o arquivo!"
.align 2

.macro equalized_histogram(%filename_bin, %output_txt, %output_bin)
    li t0, 0
    la t1, total_acumulado
    sw t0, 0(t1)

    j main
open_error:
    la a0, error_open
    li a7, 4
    ecall
    j exit

read_error:
    la a0, error_read
    li a7, 4
    ecall
    # Fechar arquivo se aberto
    li a7, 57
    mv a0, s0
    ecall
    
main:
    open_file(%filename_bin, 0)
    bltz a0, open_error      # Tratar erro de abertura
    mv s0, a0                			# Salvar descritor


    read_file(s0, buffer, 21120)          #recebe o descritor do arquivio/ ponteiro / tamanho 
    bltz a0, read_error      # Tratar erro de leitura
    mv s1, a0                # Salvar número de bytes lidos


    close_file(s0)
    # Mensagem de sucesso
    print_string_from_label(success_msg)
    # Mostrar quantidade de bytes
    print_int(s1)
    print_newline()
    
    # Loop de impressão dos bytes
    li t0, 0                 # Contador
    la t1, buffer            # Ponteiro
    la s0, pixel_count
    fill_zero(s0, 256)
    
calcular_freq:
    bge t0, s1, CDF
    lbu t6, 0(t1)            # Carregar byte sem sinal
    slli t3,t6, 2
    add t4, s0, t3
    lw t5, 0(t4)
    addi t5,t5,1
    sw t5,0(t4)
    addi t1, t1, 1           
    addi t0, t0, 1          
    j calcular_freq

CDF:
    li t0, 0                        # Contador
    la t1, buffer            # Ponteiro12
    la s0, pixel_count
    
CDF_loop:
    bge t0, s1, equalizer
    slli a3, t0, 2			
    add t6, s0, a3
    lw t3, total_acumulado
    lw t6, (t6)
    add t2, s0, a3
    add t4, t6, t3
    sw t4, total_acumulado, t5
    sw t4, (t2)
    addi t0, t0, 1
    j CDF_loop
 
equalizer:
    li t0, 0
    li t2, 255
    la s0, pixel_count

loop:
    bge t0, s1, result
    slli t3, t0, 2
    add t4, s0, t3
    lw t5, 0(t4)
    mul t5, t5, t2				#multiplico 255 pela CDF e 
    div t5, t5, s1				#divido por 21120
    sw t5, (t4)				#guarda onde antes estava CDF
    #print_int(t5)
    #print_newline()
    addi t0, t0, 1
    j loop


result:						#pega o pixel, mult por 4, soma com o topo da pilha, o valor é o mapa de frequencia, acessando o pixel equalizado e coloco onde esta o pixel normal , onde o buffer terá agora os pixels equalizados
    li t0, 0                 		# Contador
    la t1, buffer            # Ponteiro12
    la s0, pixel_count
result_loop:
    bge t0, s1, calcular_freq2
    #print_int(t1)
    lbu  t3, 0(t1)			#guarda em t3, o valor que esta no end de memoria de t1, em byte      #o 0 é o imediato 
    #print_int(t3)
    slli t4, t3, 2
    add t3, t4, s0
    lw t5, 0(t3)
    #print_int(t5)
    sb t5, (t1)				#guarda o valor em byte de t5 em t1
    addi t0, t0, 1 			
    addi t1, t1, 1
    j result_loop
   
calcular_freq2:
    li t0, 0                 # Contador
    la t1, buffer            # Ponteiro12
    la s0, pixel_count
    fill_zero(s0, 256)
calcular_freq2_loop:
    bge t0, s1, exit
    lbu t6, 0(t1)            # Carregar byte sem sinal
    slli t3,t6, 2
    add t4, s0, t3
    lw t5, 0(t4)
    addi t5, t5, 1
    sw t5,0(t4)
    #print_int(t4)
    # Imprimir valor decimal
    #li a7, 1
    #ecall
    addi t1, t1, 1           
    addi t0, t0, 1          
    j calcular_freq2_loop
    
exit:
    la s0, pixel_count
    escrever_frequencias(s0, %output_txt)
    create_file(%output_bin)
    open_file(%output_bin, 9)
    
    mv s0, a0
    write_string_addr(buffer, s0, 21120)
    print_string_from_label(success_msg)
    close_file(s0)
.end_macro

.text
    equalized_histogram(filename_green, output_green, output_bin_green)
    #equalized_histogram(filename_blue, output_blue, output_bin_blue)
    #equalized_histogram(filename_red, output_red, output_bin_red)
    li a7, 10
    ecall
