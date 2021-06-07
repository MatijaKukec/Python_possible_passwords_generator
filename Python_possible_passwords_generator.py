import sys

# opening a file for export
f = open("file.txt", "a+")

def generate(slova, i, s, len): 
  
    # base case 
    if (i == 0): # when len has 
                 # been reached 
      
        # print it out
        if (pref): 
            f.write(pref + s +"\n")
            print(pref + s + "\t") 
        else :
            f.write(s+"\n")
            print(s + "\t") 
        return
      
    # iterate through the array 
    for j in range(0, len): 
  
        # Create new string with  
        # next character Call  
        # generate again until  
        # string has reached its len 
        appended = s + slova[j] 
        generate(slova, i - 1, appended, len) 
  
    return


def crack0(slova, len): 

    # call for required length
    for i in range(len, len + 1):  
        generate(slova, i, "", len) 
  
# function to generate  
# all possible passwords 
def crack1(slova, len): 
  
    # call for all required lengths 
    for i in range(1 , len + 1):  
        generate(slova, i, "", len)

def crack2(slova, len): 

    # call for required length
    for i in range(xlen):  
        generate(slova, i, "", len)

# creating an empty list 
slova = [] 
string = []
s = []
pref=0
xlen=0


inn=True
while(inn):
    prefTrue = str(input("Želite li unijeti prefiks? (da/ne, yes/no) : "))
    if prefTrue[:1]=="y" or prefTrue[:1]=="d" or prefTrue[:1]=="D" or prefTrue[:1]=="Y":
        pref = str(input("Unesite prefiks koji će se spajati: "))
        inn=False
    elif prefTrue[:1]=="n" or prefTrue[:1]=="N" : inn=False



# number of elements as input 
brSlov = int(input("Koliko elemenata želite unijeti?: "))
# mesta = int(input("Koliko mjesta za moguću kombinaciju: "))
  
# iterating till the range 
for i in range(0, brSlov): 
    ele = str(input("Upišite " +str(i+1)+ ". element: "))
    f.write(ele)
    slova.append(ele) # dodavanje elementa
    
x=len(slova)
q=x^brSlov

print (str(q) + " mogućih kombinacija.\n")


inn=True
while(inn):
    fixTrue = str(input("Želite li da se ispisuju lozinke od apsolutno svih kombinacija ili samo fiksne duljine, Fixsno/Ne?"))
    if fixTrue[:1]=="F" or fixTrue[:1]=="f" : 
        lenTrue = str(input("Želite li da se ispisuju lozinke određene duljine? (da/ne, yes/no) :"))
        if lenTrue[:1]=="y" or lenTrue[:1]=="d" or lenTrue[:1]=="D" or lenTrue[:1]=="Y":
            crack2(slova, x)
            xlen = int(input("Upišite željenu duljinu?"))
        else: crack0(slova, x)
        inn=False
    else: crack1 (slova, x)

print(slova)

f.close()