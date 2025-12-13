def read_file(name):
    lista=[]
    with open(name,"r") as file:
        for line in file:
            lista.append(line.strip())
    return lista

def count_rolls(segment):
    rolls=0
    print(segment)
    for i in range(len(segment)):
        if(segment[i]=="@"):
            rolls+=1
        else:
            break
    return rolls

def reverse_count_rolls(segment):
    rolls=0
    print(" "+segment,end=("x"))
    for i in range(len(segment)-1,0,-1):
        if(segment[i]=="@"):
            rolls+=1
        else:
            break
    return rolls

def check_line(line):
    new_line=[]
    print(len(line))
    for i in range(len(line)):
        reachable=0
        if(line[i]=="@"):
            if(i==0):
                reachable=count_rolls(line[i+1:9])
                if reachable>4:
                    new_line.append("X")
                else:
                    new_line.append(line[i])
            elif i==1:
                reachable+=reverse_count_rolls(line[i-1])
                reachable+=count_rolls(line[i+1:9])
                if reachable>4:
                    new_line.append("X")
                else:
                    new_line.append(line[i])
            elif i==2:
                reachable+=reverse_count_rolls(line[i-2:i])
                reachable+=count_rolls(line[i+1:9])
                if reachable>4:
                    new_line.append("X")
                    
                else:
                    new_line.append(line[i])
            elif i==3:
                reachable+=reverse_count_rolls(line[i-3:i])
                reachable+=count_rolls(line[i+1:9])
                if reachable>4:
                    new_line.append("X")
                else:
                    new_line.append(line[i])
            elif i == len(line):
                reachable=reverse_count_rolls(line[i-9:])
                if reachable>4:
                    new_line.append("X")
                else:
                    new_line.append(line[i])
            elif i == len(line)-1:
                reachable+=reverse_count_rolls(line[i-9:i-1])
                reachable+=count_rolls(line[i+1])
                if reachable>4:
                    new_line.append("X")
                else:
                    new_line.append(line[i])
            elif i == len(line)-2:
                reachable+=reverse_count_rolls(line[i-9:i-1])
                reachable+=count_rolls(line[i+1:])
                if reachable>4:
                    new_line.append("X")
                else:
                    new_line.append(line[i])
            elif i == len(line)-3:
                reachable+=reverse_count_rolls(line[i-9:i-1])
                reachable+=count_rolls(line[i+1:])
                if reachable>4:
                    new_line.append("X")
                else:
                    new_line.append(line[i])
            else:
                reachable+=reverse_count_rolls(line[i-4:i])
                reachable+=count_rolls(line[i+1:i+5])
                if reachable>4:
                    new_line.append("X")
                else:
                        new_line.append(line[i])
        else:
            new_line.append(line[i])
    print("".join(new_line))
    input()
    return reachable


if __name__=="__main__":
    list=read_file("c:/Users/joaov/Documents/GitHub/Advent-of-Code/2025/Day4/test_input.txt")
    sum=0
    print("\n\n")
    for line in list:
        sum+=check_line(line)
    print("Result:",sum)