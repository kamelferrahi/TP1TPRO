def ProblemeduSac(Objets,wmax):
    T = list()
    for i in range(len(Objets)+1):
        T.append(list())
        for j in range(wmax+1):
        
            if (i==0 or j==0):
                T[i].append([0,list()])
              
            else:
                if (j<Objets[i-1]["poid"]): T[i].append(T[i-1][j])
                else:
                    if (T[i-1][j-Objets[i-1]["poid"]][0]+Objets[i-1]["valeur"]>=T[i-1][j][0]):
                        
                        newlist = T[i-1][j-Objets[i-1]["poid"]][1].copy()
                        newlist.append(i-1)
                        newval = T[i-1][j-Objets[i-1]["poid"]][0]+Objets[i-1]["valeur"]
                        T[i].append([newval,newlist])
                        
                    else:
                        T[i].append(T[i-1][j])
                    

    return T[len(Objets)][wmax]