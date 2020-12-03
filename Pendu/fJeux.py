def Jouer(pMot,caché,vie,lfaux):
    a=0

    lettre=input("entrez lettre")
    if lettre in pMot:
         if lettre==pMot:
            a="gagné"
            return a
         position=[]
         for i in range (0,len(caché)):
             if pMot[i]==lettre:
                 position=position+[i]
         for i in position:
             caché[i]=lettre
         print(caché)
         if '_'  not in caché:
            # rejouer=input("vous avez gagné, appuyer sur 1 pour rejouer")
             return vie
             #if rejouer==1:

             #else:
               # return vie
         else:
             return Jouer(pMot,caché,vie,lfaux)

    else:
        if lettre in lfaux:
            print("lettre déjà joué")
            return Jouer(pMot, caché, vie, lfaux)
        else:
            lfaux=lfaux+[lettre]

        vie=vie-1
        print(vie)
        if vie==0:
             a="perdu"
             return(a)
        else:
            return Jouer(pMot,caché,vie,lfaux)