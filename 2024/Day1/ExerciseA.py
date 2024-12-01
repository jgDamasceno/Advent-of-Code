
def read_file(name):
    listA=[]
    listB=[]
    with open(name,"r") as file:
        for line in file:
            line=line.strip().split(" ")
            listA.append(int(line[0]))
            listB.append(int(line[-1]))
    return listA,listB

def calc_diff(listA,listB):
    dif=[]
    for i in range(len(listA)):
        valA=listA[i]
        dif.append(abs(listA[i]-listB[i]))
    return dif


if __name__=="__main__":
    listA,listB=read_file("ExerciseA_List.txt")    
    listA.sort()
    listB.sort()
    dif=calc_diff(listA,listB)
    print("result: "+str(sum(dif)))