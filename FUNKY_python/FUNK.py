import os

"""Mac OS X"""
"""#1"""
def stink(person="", stink_type=""):
    print(""+person+" stinks like "+stink_type+".")

"""#2"""
def twinprint(text=""):
    print(text *2)

"""#3"""
def stinker(person=""):
    print(""+person+"is awesome!")

"""#4"""
def installPYTHONmodule(module=""):
    os.system(module)

"""#5"""
def keypass(key=""):
    input = input()
    if input == key:
        print("Welcome.")
    print("You failed.")

"""#6"""
def solve():
    print("Solve:")
    print("1+2")
    input = input("")
    if input == "3":
        print("3-2")
        input2 = input()
        if input2 == "1":
            print("10*100/2+287+1245678900")
            if input3 == "1245679687":
                print("You finished!")
            print("You failed!")
        print("You failed!")
    print("You failed!")


"""future updates will be made"""
"""v1.0"""
