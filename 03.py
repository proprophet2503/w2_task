def fun1():
    testfun = input("Enter T for true or F for false :")
    if(testfun == "T"):
        return 1
    else:
        return 0
        


def fun2():
    print("fun2 executed")
    return 1


def main():

    a = fun1()
    b = fun2() 
    print("Testing &&")

    if (bool(a) == True and bool(b) == True):
        print("Test of && complete")

    print("Testing ||")
    if (bool(a) == True or bool(b) == True):
        print("The test of || complete")

main()





