#lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

mensagemDescriptografada = ' '

chave = int(input("Digite a chave secreta: "))

mensagem = input("Por favor, entre com a mensagem para descriptografar: ")

#encontre a posição de cada letra em alfabeto
#exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.
for l in range(len(mensagem)):
    letra = mensagem[l]
    posicao = alfabeto.find(letra)

    #some a chave secreta para encontrar a posição da letra criptografada
    #% 26 significa 'volte para 0 quando você chegar no 26'
    novaPosicao = (posicao - chave) % 26

    #a letra criptografa está no alfabeto na nova posição
    mensagemDescriptografada += alfabeto[novaPosicao]

print("Sua letra descriptografada é" , mensagemDescriptografada.strip())
