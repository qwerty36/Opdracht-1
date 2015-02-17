def main():
    bestand = open("m_p53.gb")
    sequentie = getSequentie(bestand)
    codons = maakCodons(sequentie)
    start = zoekStart(sequentie)
    eind = zoekStop(sequentie)
    print("Het startcodon ligt op positie: ",start+1)
    print("Het stopcodon ligt op positie: ",eind+1)
   
def getSequentie(bestand):
    DNA=["a","t","g","c"]          
    raw_data = ""  
    for regel in bestand:
        raw_data+=regel.lower()
    if "origin" in raw_data:
        seq1 = raw_data[raw_data.index("origin"):len(raw_data)]
        seq1 = seq1.strip("origin")
        seq1 = seq1.replace("\n","").replace("\t","").replace(" ","")
        for ch in seq1:
            if ch not in DNA:
                seq1 = seq1.replace(ch,"")
        return seq1
 
def maakCodons(seq):
    codons=[]
    count=0
    for x in range(int((len(seq)+1)/3)):
        codons.append(seq[count:count+3])
        count+=3
    return codons
 
def zoekStart(seq):
    start = seq.find("atg")
    return start
 
def zoekStop(seq):
    stop = seq.find("tag" or "taa" or "tga")
    return stop
 
main()