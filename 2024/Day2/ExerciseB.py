
def read_file(name):
    reports=[]
    with open(name,"r") as file:
        for line in file:
            line=line.strip().split(" ")
            reports.append(line)
    return reports

def check_status(report):
    last_level=-1
    last_inc=None
    for level in report:
        level=int(level)
        if last_level!=-1:
            if last_level<level:
                inc=True
            elif last_level>level:
                inc=False
            else:
                return False
            if not last_inc==None:
                if last_inc != inc:
                    return False
            
            count=last_level-level
            dif=abs(count)
            if dif>3:
                return False
            else:
                last_inc=inc
                last_level=level
        else:
            last_level=level
    return True


if __name__=="__main__":
    reports=read_file("input.txt")
    status=[]
    for report in reports:
        stat=check_status(report)
        status.append(stat)
        print(report,end=" -> ")
        print(stat)
    print("______________________________________")
    sum=0
    for index,result in enumerate(status):
        if result:
            sum+=1
        else:
            report=reports[index]
            print(report)
            for index in range(len(report)):
                rep = report[:index] + report[index+1:]
                check=check_status(rep)
                print(rep,end=" -> ")
                print(check)
                if(check):
                    sum+=1
                    break
             
                
    print("Result: "+ str(sum))