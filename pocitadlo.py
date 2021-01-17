
pocetRadku = 0
pocetZnaku = 0
pocetSlov = 0

cetnostZnaku={}

while True:
    radek=f.readline()
    if radek == '':  
        break       
    radek = radek.decode('utf-8') 
    pocetRadku = pocetRadku + 1
    delka=len(radek)
    pocetZnaku += delka         
    pocetSlov += len(radek.split()) 
    for znak in radek:  
        if znak in (' ','\t', '\n' ):
            continue    
        if cetnostZnaku.has_key(znak):
            cetnostZnaku[znak] += 1
        else:
            cetnostZnaku[znak] = 1          


for znak in cetnostZnaku.keys():
    pocet = 60 * cetnostZnaku[znak] / max(cetnostZnaku.values())
    graf = '*' * pocet
    print ("{0:2s}{1:10} |{2}".format( znak, cetnostZnaku[znak], graf )
    
print("pocet radku: "), pocetRadku
print("pocet slov: "), pocetSlov
print("pocet znaku: "), pocetZnaku
