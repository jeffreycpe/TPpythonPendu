def Trie(pMot): # fonction qui trie par taille, puis par odre alphabétique

    ListeFinal = []
    Ls=[]
    n=0
    while len(ListeFinal)<len(pMot)+n: #trie par taille
        MotLePlusGrand=pMot[0]
        for i in range(0,len(pMot)): #cherche le mot le plus grand puis le supprime

            if len(MotLePlusGrand)<len(pMot[i]) :
                MotLePlusGrand=pMot[i]

        n=n+1
        ListeFinal=[MotLePlusGrand]+ListeFinal
        pMot.remove(MotLePlusGrand)
    ListeFinal=ListeFinal+['nothing']
    i=0
    LF=[]
    while i<len(ListeFinal)-1:
        Ls=[ListeFinal[i]]
        while len(ListeFinal[i])==len(ListeFinal[i+1]) and i<len(ListeFinal)-2:
            Ls=Ls+[ListeFinal[i+1]]
            i=i+1
        LF=LF+[Ls]
        i=i+1
    for i in range(0,len(LF)):
        LF[i]=sorted(LF[i])





    return LF