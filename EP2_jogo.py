import EP2_funçoes
import random
baralho=EP2_funçoes.cria_baralho()
baralho=random.sample(baralho,52)

def imprime_jogo():
    i=0
    while i<len(baralho):
        print('{}: {}'.format(i+1,baralho[i]))
        i+=1
    if  not EP2_funçoes.possui_movimentos_possiveis:
        return 'Perdeu'
    else:
        return ''
    
quer_jogar=input('Quer jogar ? ')
while quer_jogar!='sim':
    quer_jogar=input('Quer jogar ? ')
else:
    while EP2_funçoes.possui_movimentos_possiveis:
        print(imprime_jogo())
        indice=int(input('Escolha o número de uma carta: '))
        while EP2_funçoes.lista_movimentos_possiveis(baralho,indice)==[] or indice<1 or indice>len(baralho): #Consertar se o usuário escolher a ultima carta
            print('Carta Inválida')
            indice=int(input('Escolha o número de uma carta: '))
        if EP2_funçoes.lista_movimentos_possiveis(baralho,indice)==[1]:
            baralho=EP2_funçoes.empilha(baralho,indice,indice-1)
        elif EP2_funçoes.lista_movimentos_possiveis(baralho,indice)==[3]:
            baralho=EP2_funçoes.empilha(baralho,indice,indice-3)
        elif EP2_funçoes.lista_movimentos_possiveis(baralho,indice)==[1,3]:
            escolha=input('Escolha o número da carta de destino:{}: {} ou {} {} ? '.format(indice-1,baralho[indice-1],indice-3,baralho[indice-3]))
            if escolha == (indice-1):
                baralho=EP2_funçoes.empilha(baralho,indice,indice-1)
            elif escolha == (indice-3):
                baralho=EP2_funçoes.empilha(baralho,indice,indice-3)


