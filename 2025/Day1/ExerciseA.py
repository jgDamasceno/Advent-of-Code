def read_file(name):
    listA=[]
    with open(name,"r") as file:
        for line in file:
            linha=line.strip()
            if(linha[0]=="R"):
                listA.append(int(linha[1:]))
            else:
                listA.append(-int(linha[1:]))
    return listA

def calulate_mod(listA):
    set=50
    count=0
    for item in listA:
        set+=item
        mod=set%100
        if mod==0:
            count+=1
    return count

if __name__=="__main__":
    listA=read_file("ExerciseA_List.txt")
    print("result: "+str(calulate_mod(listA)))