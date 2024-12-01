import bisect

def read_file(name):
    listA=[]
    listB=[]
    with open(name,"r") as file:
        for line in file:
            line=line.strip().split(" ")
            listA.append(int(line[0]))
            listB.append(int(line[-1]))
    return listA,listB

def unique_values(list):
    unique=[]
    for elem in list:
        if elem not in unique:
            bisect.insort(unique,elem)
    return unique

def get_frequency(listA,listB):
    freq=[]
    for elemA in listA:
        count=0
        for elemB in listB:
            if(elemA==elemB):
                count+=1
        freq.append(count)
    return(freq)

def calc_similarity(listA,frequency):
    count=0
    for i in range(len(listA)):
        count+=listA[i]*frequency[i]
    return(count)
if __name__=="__main__":
    listA,listB=read_file("ExerciseA_List.txt")    
    frequency=get_frequency(listA,listB)
    print("result: "+str(calc_similarity(listA,frequency)))