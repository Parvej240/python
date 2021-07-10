class myclass:
    x=5
p1=myclass
print(p1.x)

class Persion:
    def __init__(self, age,name):
        self.age = age
        self.name = name

p1 = Persion("jhon",21)
print(p1.age)
print(p1.name)

class parvej(object):
    def __init__(self,name, age):
        self.age = age
        self.name=name

    def fname(self):
        print("Hello is a " + self.name)

p1 = parvej("jhon",21)
p1.fname()

class lalu(object):
    def __init__(pavel, arg):
        pavel.age = age
        pavel.name = name

    def fname(self):
        print("Hello is a " + self.name)

p1 = parvej("jhon",21)
p1.age=11
p1.fname()
print(p1.age)
