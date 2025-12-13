
def split_digits_string(number):
    return [ str(d) for d in str(number)]
def read_file(name):
    lista=[]
    with open(name,"r") as file:
        for line in file:
            linha=line.strip().split(',')
            for item in linha:
                it=item.split('-')
                first_val=int(it[0])
                second_val=int(it[1])
                for val in range(first_val,second_val+1):
                    digits=split_digits_string(val)
                    if(len(digits)%2==0):
                        lista.append(val)
    return lista

def check_invalid_IDs(list):
    invalid_ids=[]
    for id in list:
        digits=split_digits_string(id)
        half_way=len(digits)//2
        first_half=int("".join(digits[:half_way]))
        second_half=int("".join(digits[half_way:]))
        if(first_half==second_half):
            invalid_ids.append(id)
    return invalid_ids

if __name__=="__main__":
    list=read_file("input.txt")
    invalid_ids=check_invalid_IDs(list)
    sum=0
    for id in invalid_ids:
        sum+=id
    print("Result:",sum)