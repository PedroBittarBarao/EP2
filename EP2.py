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