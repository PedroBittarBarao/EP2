import EP2_funçoes
import random
baralho=EP2_funçoes.cria_baralho()
baralho=random.sample(baralho,52)
i=0
while i<len(baralho):
    print('{}: {}'.format(i+1,baralho[i]))
    i+=1