votoScritto = int(input('Inserisci il voto per lo scritto: '))
while votoScritto<-8 or votoScritto>8:
    votoScritto = int(input('Inserisci il voto per lo scritto corretto: '))

votoPratica = int(input('Inserisci il voto per la prarica: '))
while votoPratica<0 or votoPratica>24:
    votoPratica = int(input('Inserisci il voto per la pratica corretto: '))

risFinale=votoScritto+votoPratica

if votoScritto<=0 and risFinale>18:
    print('BOCCIATO')
elif votoScritto<=0 and votoPratica<18:
    print('BOCCIATO')
elif votoScritto>0 and risFinale<18:
    print('BOCCIATO')
elif risFinale==31 or risFinale==32:
    print('CONGRATULAZIONI 30 E LODE')
else:
    print('PROMOSSO CON IL SEGUENTE VOTO: ', risFinale)