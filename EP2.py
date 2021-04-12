def cria_baralho():
    naipes=['♠', '♥','♦','♣']
    numeros=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    baralho=[]
    for na in naipes:
        for nu in numeros:
            baralho.append(nu+na)
    return baralho