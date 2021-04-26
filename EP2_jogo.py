import EP2_funçoes
import random
baralho=EP2_funçoes.cria_baralho()
baralho=random.sample(baralho,52)

def imprime_jogo():
    i=0
    while i<len(baralho):
        print('{}: {}'.format(i+1,baralho[i]))
        i+=1
    return ''
    
quer_jogar=input('Quer jogar ? ')
while quer_jogar!='sim':
    quer_jogar=input('Quer jogar ? ')
else:
    estado_do_jogo=EP2_funçoes.possui_movimentos_possiveis(baralho)
    while estado_do_jogo :
        print(imprime_jogo())
        numero=int(input('Escolha o número de uma carta: '))
        indice=numero-1
        while indice<0 or indice>len(baralho) or indice==len(baralho) or EP2_funçoes.lista_movimentos_possiveis(baralho,indice)==[] : #Consertar se o usuário escolher a ultima carta
            print('Carta Inválida')
            numero=int(input('Escolha o número de uma carta: '))
            indice=numero-1
        if EP2_funçoes.lista_movimentos_possiveis(baralho,indice)==[1]:
            baralho=EP2_funçoes.empilha(baralho,indice,indice-1)
        elif EP2_funçoes.lista_movimentos_possiveis(baralho,indice)==[3]:
            baralho=EP2_funçoes.empilha(baralho,indice,indice-3)
        elif EP2_funçoes.lista_movimentos_possiveis(baralho,indice)==[1,3]:
            numero_escolha=int(input('Escolha o número da carta de destino: {}: {} ou {}: {} ? '.format(numero-1,baralho[indice-1],numero-3,baralho[indice-3])))
            if numero_escolha == (numero-1):
                baralho=EP2_funçoes.empilha(baralho,indice,indice-1)
            else:
                print('Escolha Inválida')
                numero_escolha=int(input('Escolha o número da carta de destino: {}: {} ou {}: {} ? '.format(numero-1,baralho[indice-1],numero-3,baralho[indice-3])))
            if numero_escolha == (numero-1):
                baralho=EP2_funçoes.empilha(baralho,indice,indice-3)
            else:
                print('Escolha Inválida')
                numero_escolha=int(input('Escolha o número da carta de destino: {}: {} ou {}: {} ? '.format(numero-1,baralho[indice-1],numero-3,baralho[indice-3])))
        estado_do_jogo=EP2_funçoes.possui_movimentos_possiveis(baralho)
    if len(baralho)==1:
        print('Ganhou')
    elif len(baralho)>1:
        print('Perdeu')

