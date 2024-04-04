#the authors' names are Abby Newton and Viviana Antimo
class_names={"Newton":"Abigail","Lopez":"Abigail","Aguirre":"Anastacia","Lombardo":"Emma","Macrowski":"Allison","Eidelbes":"Sydney","Burns":"Therese","Guo":"Mandy","Patin":"Samantha","Antimo":"Viviana","Ward":"Elise","Bradley":"Leena"}

def name_frequency(dict,want):
    list=[]
    for keys in dict:
        if dict[keys]==want:
            list.append(want)
    return list

print(name_frequency(class_names,"Abigail"))
