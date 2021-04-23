import random
def cria_baralho():
    naipes=['♠', '♥','♦','♣']
    numeros=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    baralho=[]
    for na in naipes:
        for nu in numeros:
            baralho.append(nu+na)
    return baralho

def extrai_naipe(carta):
    if '♦' in carta:
        return '♦'
    elif'♥' in carta:
        return '♥'
    elif'♣' in carta:
        return '♣'
    elif'♠' in carta:
        return '♠'

def extrai_valor(carta):
    if '10' in carta:
        return '10'
    else:
        return carta[0]

def lista_movimentos_possiveis(baralho,i):
    result=[]
    if i>0:
        if extrai_naipe(baralho[i])==extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i])==extrai_valor(baralho[i-1]) :
            result.append(1)
        if i>2:
            if extrai_naipe(baralho[i-3])==extrai_naipe(baralho[i]) or extrai_valor(baralho[i-3])==extrai_valor(baralho[i]):
                result.append(3)
    return result

def empilha(baralho,origem,destino):
    baralho[destino]=baralho[origem]
    del baralho[origem]
    return baralho

def possui_movimentos_possiveis(baralho):
    result=False
    i=1
    while i < len(baralho) and result==False:
        if i>0:
            if extrai_naipe(baralho[i])==extrai_naipe(baralho[i-1]) or extrai_valor(baralho[i])==extrai_valor(baralho[i-1]) :
                result=True
            if i>2:
                if extrai_naipe(baralho[i-3])==extrai_naipe(baralho[i]) or extrai_valor(baralho[i-3])==extrai_valor(baralho[i]):
                    result=True
        i+=1
    return result