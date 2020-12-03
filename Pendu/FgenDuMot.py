def GenDuMot(pMot):
    t=["_"]
    MotCaché=[pMot[0]]
    i=1
    while i<len(pMot):
        MotCaché=MotCaché+t
        i=i+1
    return MotCaché