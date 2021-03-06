###############################################################################
##Afvinkopdracht 1, Blok 3, Richard Jansen HAN University Of Applied Sciences##
##3-03-2015####################################################################
###############################################################################

file = open ("m_p53.gb", mode='r')
lijst = []

def main():
    x = startread(file)
    gimmeinfo(x)
    print (lijst)
    
def startread(seq):
    raw_data = ""
    startReading = False
    for regel in seq:
        if startReading:
            raw_data += regel[10:]
        if "ORIGIN" in regel:
            startReading = True
    sequence = raw_data.replace(' ','').replace('\n','').replace('\r','')
    #print(sequence)    
    return sequence

def gimmeinfo(seq):
    z, s = 0, 3
    codonseq = ""
    #print(seq)
    startindex = seq.index("atg")
    print('Startcodon on location: ' +str(startindex))
    for z in range (startindex, (len(seq)-startindex)):
        vanafstart = seq[startindex:]        
        codon = vanafstart[s-3:s]
        codonseq += codon
        if codon in ('taa', 'tga', 'tag'):
            print('Stopcodon on location: ' +str(z//3+startindex))
            break
        else:
            s += 3
    for i in range(0, len(codonseq),3):
        lijst.append(codonseq[i:i+3])

main()

