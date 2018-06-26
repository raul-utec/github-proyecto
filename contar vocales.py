cad =input()
a=[]
e=[]
i=[]
o=[]
u=[]
def contar_vocales(x):

    voc=0
    for z in x:
        if z in ["a"]:
            a.append(z)
            voc=voc+1
        if z in ["e"]:
            e.append(z)
            voc=voc+1
        if z in ["i"]:
            i.append(z)
            voc=voc+1
        if z in ["o"]:
            o.append(z)
            voc=voc+1
        if z in ["u"]:
            u.append(z)
            voc=voc+1

    print("a=",len(a)+1)
    print("e=",len(e))
    print("i=",len(i))
    print("o=",len(o))
    print("u=",len(u))

contar_vocales(cad)

