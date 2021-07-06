def my_funcation():
    print("Hello world this is funcation")
my_funcation()


def my_funcation(frame):
    print(frame + " Refues")

my_funcation("Email")
my_funcation("Id")
my_funcation("NCC")

def my_funcation(country = "Norway"):
  print("I am from "  + country)

my_funcation()
my_funcation("Bangladesh")
my_funcation("Lebanon")
my_funcation()
my_funcation("Saudi Arabia")

def my_funcation(food):
    for a in food:
        print(a)
fruites = ["apple","banana","orange"]
my_funcation(fruites)

def my_funcation(x):
    return 5 * x
print(my_funcation(3))
print(my_funcation(5))
print(my_funcation(9))

def fname(arg3,arg2,arg1):
    print("the youngest child is " + arg3)
fname(arg1="ppp", arg2 = "kkk",arg3="lll")

def fname(*arg):
    print("the youngest child is " + arg[2])

fname("alif","lam","mim")
