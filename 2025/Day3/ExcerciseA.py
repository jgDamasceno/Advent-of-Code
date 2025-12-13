def read_file(name):
    lista=[]
    with open(name,"r") as file:
        for line in file:
            lista.append(line.strip())
    return lista

def get_joltages(list):
    joltages=[]
    
    for bank in list:
        print("Bank:",bank)
        max_joltage=0
        for first_baterry in range(len(bank)):
            for second_baterry in range(first_baterry+1,len(bank)):
                joltage=int(bank[first_baterry])*10+int(bank[second_baterry])
                if(joltage>max_joltage):
                    max_joltage=joltage
        joltages.append(max_joltage)
    return joltages


if __name__=="__main__":
    list=read_file("input.txt")
    joltages=get_joltages(list)
    sum=0
    for joltage in joltages:
        sum+=joltage
    print("Result:",sum)