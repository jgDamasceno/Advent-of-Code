def read_file(name):
    lista=[]
    with open(name,"r") as file:
        for line in file:
            lista.append(line.strip())
    return lista

def get_joltages(bank):
    bateries=[-1]
    for b in range(1,13):
        bateries.append(bateries[b-1]+1)
        for i in range(bateries[b],len(bank)-12+b):
            if bank[i]> bank[bateries[b]]:
                bateries[b]=i
    on_bateries=[ bank[i] for i in bateries[1:]]
    return int("".join(on_bateries))


if __name__=="__main__":
    list=read_file("input.txt")
    sum=0
    for bank in list:
        sum+=get_joltages(bank)
    print("Result:",sum)