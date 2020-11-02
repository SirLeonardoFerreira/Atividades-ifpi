#lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#esta variável armazenará a mensagem criptografada
mensagemCriptografada = ' '

#capture a chave secreta
chave = int(input("Digite a chave secreta: "))

#capture a mensagem do usuário
mensagem = input("Por favor, entre com a mensagem para descriptografar: ").lower()

#percorrra cada caracter na mensagem
for char in mensagem:

    if char in alfabeto:
        #encontre a posição de caracter em alfabeto
        #por exemplo, 'a' está na posição 0, 'e' está na posição 4, etc.
        posicao = alfabeto.find(char)

        #some a chave secreta para encontrar a posição da letra criptografada
        #% 26 significa 'volte para 0 quando você chegar no 26'
        novaPosicao = (posicao + chave) % 26

        #acrescente a letra descriptografada à mensagem
        #a letra criptografa está no alfabeto na nova posição
        mensagemCriptografada += alfabeto[novaPosicao]

    else:
        #alguns caracteres (por exemplo: '?', '§') não estão no alfabeto,
        #então simplesmente adicione a letra criptografada à mensagem
        mensagemCriptografada += char

print("Sua mensagem criptografada é:" , mensagemCriptografada.strip())
