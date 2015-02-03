################################################################
##Richard Jansen, HAN University of Applied Sciences Nijmegen###
##3-2-2015, Blok 3 Python#######################################
################################################################
def main():
    iets = input ("Geef een waarde: ")
    resultaat = bereken (iets)
    print (resultaat)

#################################################################
##Functie "bereken" deelt input door getal, zodra er geen rest###
##overblijft returned het een boolean############################
#################################################################
def bereken (a):
    try:
        if (a%400) == 0:
             return True
        elif (a%100) == 0:
             return False
        elif (a%4) == 0:
             return True
    except TypeError:
        print ("datatypes komen niet overeen in de berekening")
main ()