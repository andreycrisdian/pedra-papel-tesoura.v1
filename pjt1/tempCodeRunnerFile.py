import random

print("------------------------");
print("Seja Bem Vindo ao jogo!");
print("------------------------");

opcoes = ["pedra", "papel", "tesoura"];

escolha = random.choice(opcoes);

usuarioEscolha = input("Faça a sua jogada\n Digite 'Pedra' 'papel' ou 'tesoura'")
print(usuarioEscolha)