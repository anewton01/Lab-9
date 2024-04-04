#the authors' names are Abby Newton and Viviana Antimo
class_names=["Abigail","Newton","Abigail","Lopez","Anastacia","Aguirre","Emma","Lombardo","Allison","Macrowski","Sydney","Eidelbes","Therese","Burns","Samantha","Patin","Mandy","Guo","Leena","Bradley","Elise","Ward","Viviana","Antimo"]
def frequency_first_letter(namelist):
    dictionary={}
    for thing in namelist[1::2]:
        if thing[0] not in dictionary:
            dictionary[thing[0]]=1
        else:
            dictionary[thing[0]]+=1
    return dictionary

print(frequency_first_letter(class_names))
