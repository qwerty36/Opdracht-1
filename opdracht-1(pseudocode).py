################################################################
##Richard Jansen, HAN University of Applied Sciences Nijmegen###
##3-2-2015, Blok 3 Python#######################################
################################################################
def main():
    iets = float(input("Geef een waarde: "))
    resultaat = bereken (iets)
    print (resultaat)

#################################################################
##Functie "bereken" deelt input door getal, zodra er geen rest###
##overblijft returned het een boolean############################
#################################################################
def bereken (a):
    try:
        if a % 400 == 0:
            return True
        if a % 100 != 0 and a% 4 == 0:
            return True
        else:
            return False
    except TypeError:
        print ("Datatypes komen niet overeen")
main ()