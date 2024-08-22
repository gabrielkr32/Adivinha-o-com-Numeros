import random

def jogo_adivinhacao():
    print("Bem vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1,100)#A função random.randint(1, 100) gera um número aleatório entre 1 e 100.
    tentativas = 0


    while True:
        palpite = int(input("Adivinhe o numero entre 1 e 100: "))
        tentativas +=1
 #Dependendo do palpite, o jogo informa se o número é maior ou menor do que o número secreto.
        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente!")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente! ")
        else:
            print("ACERTOOOOU MIZARAVI !!! numero de tentativas:", tentativas ) 
            break        

if __name__ == "__main__":
    jogo_adivinhacao()
#Esse condicional é usado para garantir que um certo bloco de código (no caso, jogo_adivinhacao()) 
# seja executado apenas quando o script é executado diretamente, e não quando ele é importado como um módulo.
#isso é útil quando você quer que o código funcione tanto como um programa executável quanto como um módulo reutilizável.