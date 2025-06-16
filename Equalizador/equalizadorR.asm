 .include "macro.asm"

.data
buffer:        .space 21120     
newline:       .string "\n"
.align 2
end_red:      .string "freque_red.bin"
.align 2
saida_txt_red:        .string "histograma_equalizado_red.txt" 
.align 2
saida_bin_red:    .string "bin_bytes_red.bin"
.align 2

pixel:         .string  "Pixel \0"
.align 2
frequencia:     .string   " - calc  ocorrencia  "
.align 2
total_acumulado:.word 0
cont_pixel: 	.space 1024
msg_concluida:   .string "\nLeitura realizada: "
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
    la a0, error_open						#erro de abertura
    li a7, 4
    ecall
    j exit

read_error:
    la a0, error_read						#erro de leitura
    li a7, 4
    ecall
   													 # fechar arq
    li a7, 57
    mv a0, s0
    ecall
    
main:
    open_file(%filename_bin, 0)     # Abre o arquivo de entrada (%filename_bin) no modo leitura (0)
    bltz a0, open_error             # Se a abertura do arquivo falhar (a0 < 0), desvia para 'open_error'
    mv s0, a0                       # Salva o descritor do arquivo aberto em s0

    read_file(s0, buffer, 21120)    # Lê os 21120 bytes (tamanho da imagem) do arquivo para o 'buffer'
    bltz a0, read_error             # Se ocorrer erro ao ler o arquivo (a0 < 0), desvia para 'read_error'
    mv s1, a0                       # Salva a quantidade de bytes lidos em s1

    close_file(s0)                  # Fecha o arquivo após a leitura

    # Printar que a leitura foi concluída
    print_string_from_label(msg_concluida)  # Imprime a mensagem "Leitura realizada"
    print_int(s1)                   # Imprime a quantidade de bytes lidos (número de pixels)
    print_newline()                 # Imprime uma nova linha

    li t0, 0                        # Zera o contador 't0' (índice dos pixels)
    la t1, buffer                   # 't1' aponta para o início do buffer (onde os pixels estão armazenados)
    la s0, cont_pixel               # 's0' aponta para o vetor 'cont_pixel' (onde a frequência dos pixels será armazenada)
    fill_zero(s0, 256)              # Zera as 256 posições do vetor 'cont_pixel' para armazenar as frequências

calcular_freq:
    bge t0, s1, CDF                # Se t0 >= s1 (quantidade de pixels), vai para 'CDF'
    lbu t6, 0(t1)                  # Carrega o valor do pixel atual (byte sem sinal) em t6
    slli t3,t6, 2                  # Calcula o offset (multiplica o valor do pixel por 4 para acessar o vetor de frequências)
    add t4, s0, t3                 # 't4' agora contém o endereço de 'cont_pixel[t6]'
    lw t5, 0(t4)                   # Carrega o valor atual de 'cont_pixel[t6]' (frequência acumulada)
    addi t5,t5,1                   # Incrementa a frequência (contagem do pixel encontrado)
    sw t5,0(t4)                    # Armazena o novo valor da frequência de 'cont_pixel[t6]'
    addi t1, t1, 1                 # Avança para o próximo byte no buffer (próximo pixel)
    addi t0, t0, 1                 # Incrementa o índice 't0'
    j calcular_freq                # Repete o loop para o próximo pixel

# Cálculo do CDF (Cumulative Distribution Function)
CDF:
    li t0, 0                       # Zera o contador 't0'
    li t1, 256                     # 't1' agora é 256, que é o número de intensidades possíveis de pixel
    la s0, cont_pixel              # 's0' aponta para o vetor 'cont_pixel' (frequências)

loop_CDF:
    bge t0, t1, equalizador        # Se t0 >= 256 (todos os 256 níveis de intensidade processados), vai para 'equalizador'
    slli a3, t0, 2                 # Calcula o offset no vetor 'cont_pixel' (t0 * 4)
    add t6, s0, a3                 # 't6' é o endereço de 'cont_pixel[t0]'
    lw t3, total_acumulado         # Carrega o valor acumulado de frequências (total acumulado)
    lw t6, (t6)                    # Carrega a frequência do pixel atual
    add t2, s0, a3                 # Calcula o endereço para armazenar o CDF
    add t4, t6, t3                 # Soma a frequência do pixel atual com o total acumulado
    sw t4, total_acumulado, t5     # Atualiza o total acumulado
    sw t4, (t2)                    # Armazena o valor acumulado do CDF no vetor de frequências
    addi t0, t0, 1                 # Incrementa o contador 't0'
    j loop_CDF                     # Repete para o próximo valor de pixel

# Equalização do histograma
equalizador:
    li t0, 0                       # Zera o contador 't0'
    li t2, 255                     # 't2' é 255, o valor máximo para um pixel (escala 0-255)
    la s0, cont_pixel              # 's0' aponta para o vetor de frequências

loop:
    bge t0, s1, result             # Se t0 >= s1 (todos os pixels processados), vai para 'result'
    slli t3, t0, 2                 # Calcula o offset no vetor 'cont_pixel' (t0 * 4)
    add t4, s0, t3                 # 't4' contém o endereço de 'cont_pixel[t0]'
    lw t5, 0(t4)                   # Carrega o valor do CDF do pixel atual
    mul t5, t5, t2                 # Multiplica o CDF pelo valor máximo (255) para normalizar
    div t5, t5, s1                 # Divide pelo número total de pixels (21120)
    sw t5, (t4)                    # Armazena o valor equalizado de volta no vetor de frequências
    addi t0, t0, 1                 # Incrementa o contador 't0'
    j loop                         # Repete para o próximo valor de pixel

# Substitui os valores do buffer com os pixels equalizados
result:
    li t0, 0                       # Zera o contador de pixels 't0'
    la t1, buffer                  # 't1' aponta para o buffer da imagem
    la s0, cont_pixel              # 's0' aponta para o vetor de frequências equalizadas

result_loop:
    bge t0, s1, calcular_freq2     # Se t0 >= s1 (todos os pixels processados), vai para 'calcular_freq2'
    lbu  t3, 0(t1)                 # Carrega o valor do pixel atual no buffer
    slli t4, t3, 2                 # Calcula o offset no vetor de frequências equalizadas
    add t3, t4, s0                 # Calcula o endereço de 'cont_pixel[t3]'
    lw t5, 0(t3)                   # Carrega o valor equalizado do CDF
    sb t5, (t1)                    # Substitui o pixel original com o valor equalizado
    addi t0, t0, 1                 # Incrementa o contador de pixels
    addi t1, t1, 1                 # Avança para o próximo pixel no buffer
    j result_loop                  # Repete para o próximo pixel

# Recalcula as frequências dos pixels após a equalização
calcular_freq2:
    li t0, 0                       # Zera o contador de pixels
    la t1, buffer                  # 't1' aponta para o buffer da imagem equalizada
    la s0, cont_pixel              # 's0' aponta para o vetor de frequências

calcular_freq2_loop:
    bge t0, s1, exit               # Se t0 >= s1, termina o loop
    lbu t6, 0(t1)                  # Carrega o valor do pixel atual do buffer
    slli t3, t6, 2                 # Calcula o offset no vetor 'cont_pixel'
    add t4, s0, t3                 # Calcula o endereço de 'cont_pixel[t6]'
    lw t5, 0(t4)                   # Carrega a frequência do pixel
    addi t5, t5, 1                 # Incrementa a frequência
    sw t5, 0(t4)                   # Armazena a nova frequência no vetor 'cont_pixel'
    addi t1, t1, 1                 # Avança para o próximo pixel no buffer
    addi t0, t0, 1                 # Incrementa o contador de pixels
    j calcular_freq2_loop          # Repete para o próximo pixel

exit:
    la s0, cont_pixel              # Pega o vetor de frequências
    escrever_frequencias(s0, %output_txt) # Escreve as frequências no arquivo de saída (TXT)
    create_file(%output_bin)        # Cria o arquivo binário de saída
    open_file(%output_bin, 9)       # Abre o arquivo binário para escrita

    mv s0, a0                      # Move o descritor do arquivo
    write_string_addr(buffer, s0, 21120)  # Escreve a imagem equalizada no arquivo binário
    print_string_from_label(msg_concluida)  # Imprime mensagem de conclusão
    close_file(s0)                  # Fecha o arquivo binário
.end_macro


.text
    equalized_histogram(end_red, saida_txt_red, saida_bin_red)
    li a7, 10
    ecall
