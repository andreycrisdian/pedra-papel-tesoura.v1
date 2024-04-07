import random

print("------------------------")
print("Seja Bem Vindo ao jogo!")
print("------------------------")

opcoes = ["pedra", "papel", "tesoura"]
escolha = random.choice(opcoes)

usuarioEscolha = input("Faça a sua jogada\n Digite 'Pedra', 'Papel' ou 'Tesoura': ").lower()

resultados = {
    "pedra": {"pedra": "Empate!", "papel": "Você perdeu!", "tesoura": "Você ganhou!"},
    "papel": {"pedra": "Você ganhou!", "papel": "Empate!", "tesoura": "Você perdeu!"},
    "tesoura": {"pedra": "Você perdeu!", "papel": "Você ganhou!", "tesoura": "Empate!"}
}

print(resultados[usuarioEscolha][escolha])
