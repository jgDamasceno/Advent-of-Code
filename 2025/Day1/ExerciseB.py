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

def calulate_mod(listA,debug):
    dial_value=50
    previous_dial_value=50
    total=0
    for num,rotation in enumerate(listA):
        count=0
        passed_zero=0
        full_rotations=0


        if(rotation>100):
            full_rotations=abs(rotation)//100
            rotation=rotation-(full_rotations*100)
        elif(rotation<-100):
            full_rotations=abs(rotation)//100
            rotation=rotation+(full_rotations*100)

        dial_value+=rotation
        mod=dial_value%100
        
        if mod==0:
            count+=1
        elif(previous_dial_value> 0 and dial_value<0):
            passed_zero+=1
        elif(previous_dial_value<0 and dial_value>0):
            passed_zero+=1
        
        if dial_value>100:
            passed_zero+=1

        """if(abs(rotation)>100 or abs(rotation)<-100):
            full_rotations=abs(rotation)//100-passed_zero
            if(full_rotations<0):
                full_rotations=0"""
        

        total+=full_rotations+passed_zero+count
        if(debug):
            print("Rotation number: "+str(num+1))
            print("Dial value before rotation: "+str(previous_dial_value))
            print("Rotation: "+str(rotation))
            print("Dial value after rotation: "+str(dial_value))
            print("Modulo 100 value: "+str(mod))
            print("Passed zero count: "+str(passed_zero))
            print("Current count: "+str(count))
            print("Full Rotarions: "+str(full_rotations))
            print("Total Count: "+str(total))
            print("---------------------------------------------")
            if num>110:
                input("Press Enter to continue...\n\n")
        dial_value=mod
        previous_dial_value=dial_value
        
    return total

if __name__=="__main__":
    listA=read_file("ExerciseA_List.txt")
    print("Challenge input result: "+str(calulate_mod(listA,True)))
    
