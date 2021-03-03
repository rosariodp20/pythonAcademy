def scambiaEstremi(stringa:str):
    l=stringa.split(" ")
    tmp=l[0]
    l[0]=l[len(l)-1]
    l[len(l)-1]=tmp
    delimitatore = " "
    stringa=delimitatore.join(l)
    return stringa

print(scambiaEstremi("Donald Trump"))
print(scambiaEstremi("Rosie O'Donnell"))
print(scambiaEstremi("Seymour Butts"))


