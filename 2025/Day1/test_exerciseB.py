from ExerciseB import read_file, calulate_mod

def test_original_input():
    listA = read_file("input.txt")
    assert calulate_mod(listA, False) == 6
def test_reddit_input():
    listA = read_file("ExerciseB_List.txt")
    assert calulate_mod(listA, False) == 24
def test_rotation1():
    listA = [-50,50]
    assert calulate_mod(listA, False) == 1
def test_rotation2():
    listA = [-50,-50]
    assert calulate_mod(listA, False) == 1
def test_rotation3():
    listA = [50,-50]
    assert calulate_mod(listA, False) == 1
def test_rotation4():
    listA = [50,50]
    assert calulate_mod(listA, False) == 1
def test_rotation5():
    listA = [-150,-50]
    assert calulate_mod(listA, False) == 2
def test_rotation6():
    listA = [-150,50]
    assert calulate_mod(listA, False) == 2
def test_rotation7():
    listA = [150,-50]
    assert calulate_mod(listA, False) == 2
def test_rotation8():
    listA = [150,50]
    assert calulate_mod(listA, False) == 2
def test_rotation9():
    listA = [1000]
    assert calulate_mod(listA, False) == 10
def test_rotation10():
    listA = [-1000]
    assert calulate_mod(listA, False) == 10
def test_input():
    listA=read_file("ExerciseA_List.txt")
    print("Challenge input result: "+str(calulate_mod(listA,False)))