import random

print("------------------------");
print("Seja Bem Vindo ao jogo!");
print("------------------------");

opcoes = ["pedra", "papel", "tesoura"];

escolha = random.choice(opcoes);

usuarioEscolha = input("Faça a sua jogada\n Digite 'Pedra' 'papel' ou 'tesoura': ")
print(usuarioEscolha)

if usuarioEscolha == "pedra" and escolha == "pedra":
    print("Empate!");

elif usuarioEscolha == "pedra" and escolha == "papel":
    print("Você perdeu!");    

elif usuarioEscolha == "pedra" and escolha == "tesoura":
    print("Você ganhou!");

elif usuarioEscolha == "papel" and escolha == "papel":
    print("Empate!");

elif usuarioEscolha == "papel" and escolha == "tesoura":
    print("Você perdeu!");    

elif usuarioEscolha == "papel" and escolha == "pedra":
    print("Você ganhou!");

elif usuarioEscolha == "tesoura" and escolha == "tesoura":
    print("Empate!");

elif usuarioEscolha == "tesoura" and escolha == "pedra":
    print("Você perdeu!");    

elif usuarioEscolha == "tesoura" and escolha == "papel":
    print("Você ganhou!");




