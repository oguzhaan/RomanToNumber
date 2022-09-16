
def romentonumber():
    harf = input("Romen rakamını giriniz: ")
    toplam = 0
    #Burada sonuna string olarak 0 ekledik ki son iki rakamı karşılaştırırken son rakamı da sayıya çevirebilsin
    harf = harf + "0"
    romandict = {"0":0, "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    #String içerisindeki iki değeri karşılaştıran döngü
    for i in range(1,len(harf)):
        if(romandict[harf[i]] > romandict[harf[i-1]]):
            toplam -= romandict[harf[i-1]]
        else:
            toplam += romandict[harf[i-1]]

    return toplam

print(romentonumber())
