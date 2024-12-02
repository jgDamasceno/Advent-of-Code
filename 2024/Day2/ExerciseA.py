
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
    for index,level in enumerate(report):
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
    sum=0
    for result in status:
        if result:
            sum+=1
    print("Result: "+ str(sum))