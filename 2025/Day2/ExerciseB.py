
def split_digits_string(number):
    return [ str(d) for d in str(number)]

def group_digits_by_size(number, group_size):
    """
    Groups the digits of a number into chunks of the specified size.
    The last group may be smaller.
    """
    s = str(number)
    groups = []
    # Iterate through the string using the group_size as the step
    for i in range(0, len(s), group_size):
        # Slice the string from the current index (i) up to (i + group_size)
        chunk = s[i:i + group_size]
        if(len(split_digits_string(chunk))!=group_size):
            return []
        groups.append(int(chunk))
    return groups


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
                    lista.append(val)
    return lista

def check_invalid_IDs(list):
    invalid_ids=[]
    for id in list:
        digits=split_digits_string(id)
        for num in range(1,len(digits)+1):
            pattern=int("".join(digits[:num]))
            if(pattern!=id):
                id_remain="".join(digits[num:])
                groups=group_digits_by_size(id_remain,+len(digits[:num]))
                if groups!=[]:
                    if(set(groups)=={pattern}):
                        invalid_ids.append(id)
                        """print("Invalid ID found")
                        print(" Checking ID:",id)
                        print("     Pattern size:",pattern)
                        print("         Remaining groups:",groups)
                        input("----------------------")"""
    return invalid_ids

if __name__=="__main__":
    list=read_file("input.txt")
    invalid_ids=check_invalid_IDs(list)
    sum=0
    for id in set(invalid_ids):
        sum+=id
    print("Result:",sum)