#lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave = int(input("Digite a chave secreta: "))

letra = input("Por favor, entre com uma letra para criptografar: ")

#encontre a posição da letra em alfabeto
#exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.
posicao = alfabeto.find(letra)

#some a chave secreta para encontrar a posição da letra criptografada
#% 26 significa 'volte para 0 quando você chegar no 26'
novaPosicao = (posicao + chave) % 26

#a letra criptografa está no alfabeto na nova posição
letraCriptografada = alfabeto[novaPosicao]

print("Sua letra criptografada é" , letraCriptografada)
